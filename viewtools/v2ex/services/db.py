import json
import sqlite3
import zlib


class TopicsDatabase:
    def __init__(self, db_name='topics.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                '''\n                CREATE TABLE IF NOT EXISTS topics (\n                    topic_id INTEGER PRIMARY KEY,\n                    reply_num INTEGER NOT NULL,\n              time INTEGER NOT NULL,\n  content BLOB,\n                    replys BLOB\n                )\n            ''')

    def do_save(self, topic_id, reply_num, content, time, replys=None):
        save_reply_num = self.get_reply_num(topic_id)
        self.update_reply(topic_id, reply_num, content, time,
                          replys) if save_reply_num >= 0 and save_reply_num != reply_num else self.insert_reply(
            topic_id, reply_num, content, time, replys)

    def insert_reply(self, topic_id, reply_num, content, time, replys=None):
        print(f'insert table')
        replys_compressed = zlib.compress(json.dumps(replys or {}).encode('utf-8')) if replys else None
        with self.conn:
            self.conn.execute(
                '''\n                INSERT INTO topics (topic_id, reply_num, time, content, replys)\n                VALUES (?,?, ?, ?, ?)\n            ''',
                (topic_id, reply_num, time, zlib.compress(content.encode('utf-8')), replys_compressed))

    def get_reply_num(self, topic_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT reply_num FROM topics WHERE topic_id = ?', (topic_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return -1

    def query_reply(self, topic_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM topics WHERE topic_id = ?', (topic_id,))
        row = cursor.fetchone()
        if row:
            replys = zlib.decompress(row[4]).decode('utf-8') if row[4] else None
            return {
                'id': row[0],
                'reply_num': row[1],
                'time': row[2],
                'content': zlib.decompress(row[3]).decode('utf-8'),
                'replys': json.loads(replys)
            }
        return None

    def update_reply(self, topic_id, reply_num=None, content=None, time=None, replys=None):
        print(f'update table')
        replys_compressed = zlib.compress(json.dumps(replys or {}).encode('utf-8')) if replys else None
        updates = []
        params = []
        if reply_num is not None:
            updates.append('reply_num = ?')
            params.append(reply_num)
        if time is not None:
            updates.append('time = ?')
            params.append(time)
        if content is not None:
            updates.append('content = ?')
            params.append(zlib.compress(content.encode('utf-8')))
        if replys_compressed is not None:
            updates.append('replys = ?')
            params.append(replys_compressed)
        params.append(topic_id)
        with self.conn:
            self.conn.execute(
                f'''\n                UPDATE topics\n                SET {", ".join(updates)}\n                WHERE topic_id = ?\n            ''',
                tuple(params))

    def delete_reply(self, topic_id):
        with self.conn:
            self.conn.execute('DELETE FROM topics WHERE topic_id = ?', (topic_id,))

    def __del__(self):
        self.conn.close()
