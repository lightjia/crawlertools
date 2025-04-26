import json
import os

from flask import Flask, send_from_directory, request
from flask_cors import CORS

from work import V2ex

app = Flask(__name__, static_folder='../view/dist', static_url_path='')
v2ex = V2ex()
CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有跨域请求


@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
        response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = headers or 'Content-Type'
        return response


@app.route('/api/op_code', methods=['POST'])
def op_code():
    opData = request.get_json()
    if opData['code'] == 'more':
        return json.dumps(v2ex.More())
    elif opData['code'] == 'detail':
        return json.dumps(v2ex.getTopicDetails(opData['topic_id']))
    return "ok"


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080, threaded=False)
