from elasticsearch import Elasticsearch, helpers
import os
import json
import pymongo
import re


es = Elasticsearch("http://0.0.0.0:9200")


def add_entity_index():
    mongo_uri = "mongodb://10.108.17.218:27017"
    mongo_db = "gigi"
    need_num = -1
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = ['acm_test']
    raw_data = []
    if need_num == -1:
        raw_data = db[collection[0]].find()
    else:
        raw_data = db[collection[0]].aggregate([{'$sample': {'size': need_num}}])
    need_keys = [
        "title", "authors", "abstract", "doi", "year", "month", "type", "venue", "volume",
        "source_url", "pdf_url", "ebook_url", "ppt_url", "video_url",
        "citations_num", "ppt_title", "video_title"
    ]
    id_cnt = 0
    for data in raw_data:
        id_cnt += 1
        final_data = {}
        for key in need_keys:
            try:
                val = data[key]
            except Exception:
                val = ""
            if key == "year" or key == "month":
                if val == "":
                    val = "2000"
                val = int(val)
            final_data[key] = val

        # id & ref_list
        final_data["id"] = str(id_cnt)
        final_data["reference_list"] = []
        ref_id = "-1"
        try:
            for ref in data["reference_list"]:
                try:
                    year = re.findall(r'[^0-9][0-9]{4}[^0-9]', ref)[0]
                except Exception:
                    year = ""
                final_ref = {
                    'id': ref_id,
                    'title': ref,
                    'year': year
                }
                final_data["reference_list"].append(final_ref)
        except Exception:
            pass
        result = es.create(index='paper', id=id_cnt, body=final_data)
        print(result)


def add_ebook_to_es():
    id_cnt = 54208
    with open('/data_1/xuzf/workspace/dev/search_engine/backend/Libgen-Crawler_1.json', 'r', encoding='utf-8') as fp:
        x = json.load(fp)
        for i in range(len(x)):
            data = x[i]
            final_data = {
                "title": data["title"],
                "authors": data["author"],
                "url": data["url"]
            }
            result = es.create(index='paper', id=id_cnt, body=final_data)
            print(result)
            id_cnt += 1


def add_video_to_mongodb():
    mongo_uri = "mongodb://10.108.17.218:27017"
    mongo_db = "gigi"
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    my_set = db["acm_test"]
    with open('/data_1/xuzf/workspace/dev/search_engine/backend/YouTube-Crawler(3).json', 'r', encoding='utf-8') as fp:
        x = json.load(fp)
        print(len(x))
        cnt = 0
        for i in range(len(x)):
            tmp = my_set.find_one({"title": x[i]['article']})
            if tmp is not None:
                tmp["video_url"] = x[i]['url']
                tmp["video_title"] = x[i]['title']
                my_set.update({"title": x[i]['article']}, tmp)
            else:
                cnt += 1
                print(cnt)
                print(i)


if __name__ == '__main__':
    es.indices.delete(index='paper', ignore=[400, 404])
    add_entity_index()
