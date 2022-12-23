import time
from elasticsearch import Elasticsearch, helpers
import os
import json


es = Elasticsearch("http://0.0.0.0:9200")

# 初始化索引的 Mappings; 字段: qid，title，alias。
page_size = 10


def search_one_page(q, p):
    start_time = int(round(time.time() * 1000))
    es_results = es.search(index='paper', body={'query': {'match': {'title': q}}, 'size': 1000})
    end_time = int(round(time.time() * 1000))
    results = []
    for result in es_results['hits']['hits']:
        print("scored: ", result['_score'])
        query_title = q.strip().lower()
        result_title = result["_source"]["title"].strip().lower()
        # 按title精准查询
        if query_title == result_title:
            print("mathced: ", query_title)
            results = []
            results.append({"entity": result['_source'], "priority": 3, "year":
                            (2022 - int(result['_source']['year'])) // 5,
                            "citations_num": int(result['_source']['citations_num'])})
            break
        # 部分匹配，title中包含查询字段
        if query_title in result_title:
            results.append({"entity": result['_source'], "priority": 2, "year":
                            (2022 - int(result['_source']['year'])) // 5,
                            "citations_num": int(result['_source']['citations_num'])})
        # 其他
        else:
            results.append({"entity": result['_source'], "priority": 1, "year":
                            (2022 - int(result['_source']['year'])) // 5,
                            "citations_num": int(result['_source']['citations_num'])})
    sort_results = sorted(results, key=lambda x: (-x['priority'], x['year'], -x['citations_num']))
    for tmp in sort_results:
        print("priority: ", tmp['priority'], "year: ", tmp['year'], "citations_num: ", tmp['citations_num'])
    totalNums = len(sort_results)
    pageNums = totalNums // page_size

    if (totalNums % page_size) > 0:
        pageNums = pageNums + 1
    ans = {
        "code ": 'code',
        "data": {
            "page": p,
            "searchCostTime": (end_time - start_time) / 1000.0,
            "totalNums": totalNums,
            "pageNums": pageNums,
            "hitList": []
        }
    }
    print("totalNums: ", totalNums)
    loop_start = page_size * (p - 1)
    loop_end = min(loop_start + page_size, len(sort_results))
    for i in range(loop_start, loop_end):
        ans['data']['hitList'].append(sort_results[i]['entity'])
    return ans


def search_one_paper(q):
    result = es.search(index='paper', body={'query': {'match': {'_id': q}}})
    print("result: ", result)
    res = result['hits']['hits'][0]['_source']
    return res


if __name__ == '__main__':
    search_one_paper(11)
