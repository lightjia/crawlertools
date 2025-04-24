import re

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parser as time_parser

from db import TopicsDatabase


class V2ex():
    def __init__(self):
        self.topics = {}
        self.curPage = 1
        self.time_parser = time_parser()
        self.db = None

    def get_db(self):
        if self.db is None:
            self.db = TopicsDatabase()
        return self.db

    def parseImg(self, dom, result):
        headImg = dom.find('img')
        result['userImg'] = headImg.get('src')
        result['userName'] = headImg.get('alt')

    def LoadFromDb(self):
        # 1126213
        data = self.get_db().query_reply(1125983)
        newData = self.getTopicDetails(1125983)
        print(f'oldNum: {data['reply_num']} newNum: {len(newData)}')

    def GetTopics(self):
        topics = {}
        response = requests.get('https://global.v2ex.co/recent', params={
            'p': self.curPage,
        })

        soup = BeautifulSoup(response.text, 'html.parser')
        topics_div = soup.find_all('div', class_='cell item')
        if len(topics_div) > 0:
            for t in topics_div:
                topic = {
                    'time': int(self.time_parser.parse(timestr=t.find('span', title=True).get('title')).timestamp())
                }
                topic['content'] = t.find('a', class_='topic-link').get_text()
                topic_id = int(re.search(r'/t/(\d+)#', t.find('a', class_='topic-link').get('href')).group(1))
                topic['is_star'] = self.get_db().get_reply_num(topic_id)
                self.parseImg(t, topic)
                replys = t.find('a', class_='count_livid')
                topic['reply_num'] = replys.get_text() if replys else 0
                topics[topic_id] = topic
                print(f'topic: {topic}')
                # TopicsDatabase().insert_reply(topic['id'], topic['reply_num'], topic['content'], topic['time'],
                #                               topic['replys'])
        return topics

    def Refresh(self):
        self.curPage = 0
        return self.More()

    def More(self):
        self.curPage += 1
        topics = self.GetTopics()
        self.topics.update(topics)
        return topics

    def getTopicDetails(self, topic_id):
        p = 1
        replys = []
        while True:
            response = requests.get(f'https://global.v2ex.co/t/{topic_id}', params={
                'p': p,
            })
            soup = BeautifulSoup(response.text, 'html.parser')
            r_divs = soup.find_all('div', id=re.compile(r'^r_'))
            if len(r_divs) < 1:
                break

            p += 1
            for reply_div in r_divs:
                reply = {}
                reply['time'] = int(
                    self.time_parser.parse(timestr=reply_div.find('span', class_="ago").get('title')).timestamp())
                self.parseImg(reply_div, reply)
                reply['content'] = reply_div.find('div', class_="reply_content").get_text()
                replys.append(reply)

            page_input = soup.find('input', class_='page_input')
            if page_input is None or int(page_input.get('max')) < p:
                break
        return replys


V2ex().LoadFromDb()
# V2ex().GetTopics()
# pageNum = 1
# def getRecentTopic():
#     topics = {}
#     # 提取所有匹配项的正则表达式
#     pattern = r'<span class="item_title"><a href="([^"]+)"[^>]*>([^<]+)</a></span>'
#     for p in range(pageNum):
#         response = requests.get('https://global.v2ex.co/recent', params={
#             'pa': p,
#         })
#         # 使用re.findall找到所有匹配的字符串
#         matches = re.findall(pattern, response.text)
#         # 提取并打印结果
#         for match in matches:
#             href_value, text_value = match
#             print(f"链接: {href_value}, 文本: {text_value}")
#             topics[href_value] = text_value
#     return topics
#
#
# def getTopicDetails(topics):
#     details = {}
#     for k, v in topics.items():
#         # 100条一个翻页
#         response = requests.get(f'https://global.v2ex.co{k}', params={
#             'p': 1,
#         })
#         soup = BeautifulSoup(response.text, 'html.parser')
#         # 查找第一个<h1>标签
#         header = soup.find('div', class_='header')
#         if header:
#             r_divs = soup.find_all('div', id=re.compile(r'^r_'))
#             print(f'title {soup.find('h1').text} img: {header.find('img').get('src')} replynum: {len(r_divs)}')
#             if len(r_divs) > 0:
#                 for reply_div in r_divs:
#                     user = reply_div.find('strong')
#                     ago = reply_div.find('span', class_="ago")
#                     content = reply_div.find('div', class_="reply_content")
#                     print(
#                         f'title {soup.find('h1').text} user: {user.get_text()} img: {reply_div.find('img').get('src')}  replay_time: {ago.get('title')} reply: {content.get_text()}')
#     return details
