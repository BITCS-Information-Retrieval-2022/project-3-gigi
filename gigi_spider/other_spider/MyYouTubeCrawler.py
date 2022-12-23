import requests
import os
import json
import time
import logging

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("monitor")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("monitor.log")
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)

url = 'https://www.youtube.com/results?'  # search_query=xxx

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

proxies = {'http': 'http://127.0.0.1:2388', 'https': 'http://127.0.0.1:2388'}  # 爬取youtube需要设置代理

# "text":
# "videoId":
# "videoRenderer":
# example:"https://www.youtube.com/watch?v=22ktiQ6vF5E"

if __name__ == "__main__":
    start = time.time()
    total = 0
    print('爬虫程序运行开始！')
    f1 = open("wordOrder.data", 'rb')  # 读取论文数据

    for i in range(0, 20000):  # 爬取两万条数据
        try:
            line = f1.readline()
            s1 = str(line)
            s2 = s1[s1.find('"_id":'):]  # 解析论文数据 提取ID与论文标题
            id = s2[6:s2.find(',"title":')]
            s3 = s1[s1.find('"title":'):]
            title = s3[9:s3.find('","abstract":')]
            # print(id)
            # print(title)

            q = title
            data = {'search_query': q}  # 利用论文标题作为query
            time.sleep(0.3)  # 主动延迟 防止爬取速度过快触发反爬机制
            response = requests.get(url=url, params=data, headers=headers, proxies=proxies)
            content = response.text
            # print(content)
            str1 = content[content.find('"videoId":'):]  # 解析返回网页数据 获取视频标题与链接
            # print(str1)
            videoID = str1[11:str1.find('","')]
            # print(videoID)
            str3 = str1[str1.find('"text":'):]
            # print(str3)
            str4 = str3[8:str3.find('"}')]
            str5 = str3[8:str3.find('",')]
            title = str4
            if len(str4) > len(str5):
                title = str5
            # print(title)

            total += 1
            if total % 100 == 0:  # 每爬取100条数据输出一次时间信息 并在日志中记录
                print(total)
                end = time.time()
                eplase = end - start
                print(eplase)
                logger.info(total)

            dict = {
                "article": q,  # 论文标题
                "id": id,  # 论文id
                "num": total,  # 记录数
                "title": title,  # 视频标题
                "url": 'https://www.youtube.com/watch?v=' + videoID  # 视频链接
            }

            data = json.dumps(dict, indent=1, ensure_ascii=False)  # 将爬取数据写入文件
            with open('YouTube-Crawler.json', 'a', encoding='utf-8', newline='\n') as fp:
                fp.write(data)
        except Exception:
            print("{}, {}, fail!".format(q, total))  # 爬取异常输出并记录
            logger.info(q, total)
            pass

    print('共爬取{}条文档数据！'.format(total))
    print('爬虫程序运行结束！')
    fp.close()
    f1.close()
    end = time.time()
    eplase = end - start
    print(eplase)
