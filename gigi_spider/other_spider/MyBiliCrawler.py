import threading
import time
from concurrent import futures
import logging
import requests
import pyquery
import os
import json

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("monitor")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("monitor.log")
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

total = 1
result = []
lock = threading.Lock()


def run(url):
    # 启动爬虫
    global total, result
    req = requests.get(url, headers=headers, timeout=6).json()
    time.sleep(0.5)  # 主动延迟 防止爬取速度过快触发反爬机制
    try:
        data = req["data"]
        if data["view"] != "--" and data["aid"] != 0:

            vid_url = "https://www.bilibili.com/video/av{}".format(data["aid"])
            video = (
                vid_url,  # 视频url
                data["aid"],  # 视频编号
                data["view"],  # 播放量
                data["danmaku"],  # 弹幕数
                data["reply"],  # 评论数
                data["favorite"],  # 收藏数
                data["coin"],  # 硬币数
                data["share"]  # 分享数
            )
            # print(video)
            with lock:
                result.append(video)
                if total % 100 == 0:
                    print(total)
                    logger.info(total)
                total += 1
    except Exception:
        pass


if __name__ == "__main__":
    print("启动爬虫，开始爬取数据")
    for i in range(300000, 306000):  # 爬取B站视频av号范围300000000~306000000 每个av号对应一条视频
        begin = 1000 * i
        urls = [
            "http://api.bilibili.com/archive_stat/stat?aid={}".format(j)
            for j in range(begin, begin + 1000)
        ]
        with futures.ThreadPoolExecutor(64) as executor:
            executor.map(run, urls)  # 多线程爬取

        crawler_data = []
        for v in result[1:-1]:
            video_url = v[0]
            video_aid = v[1]
            # print(video_url)
            try:
                req2 = requests.get(video_url, headers=headers).text
                # 视频标题无法通过api获取 需要单独爬取
                q = pyquery.PyQuery(req2)
                v_name = q("h1[title]").text()

                dict = {"name": v_name, "url": v[0], "aid": v[1], "view": v[2], "danmaku": v[3],
                        "reply": v[4], "favorite": v[5], "coin": v[6], "share": v[7]}
                video_data = json.dumps(dict, indent=1, ensure_ascii=False)
                # print(video_data)
                with open('bili-crawler.json', 'a', encoding='utf-8', newline='\n') as fp:
                    fp.write(video_data)
            except Exception:
                print("fail!")
                logger.info(video_aid, total)  # 异常信息记录
                pass

    print("爬虫结束，共为您爬取到{}条数据".format(total))
    fp.close()
