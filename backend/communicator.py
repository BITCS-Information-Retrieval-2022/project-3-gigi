from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from api.search_index import search_one_page
from api.search_index import search_one_paper

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/search', methods=['POST'])
@cross_origin()
def getSearchData():
    queryParams = json.loads(request.data)
    print("search: ", queryParams)
    res = search_one_page(queryParams['params']['q'], int(queryParams['params']['p']))
    # print("res: ", res)
    return res


@app.route('/detail', methods=['POST'])
@cross_origin()
def getDetailData():
    queryParams = json.loads(request.data)
    print("detail:", queryParams)
    res = search_one_paper(queryParams['params']['id'],)
    # print("res: ", res)
    return res


if __name__ == "__main__":
    print('run 0.0.0.0:12222')
    app.run(host='0.0.0.0', port=12222)
