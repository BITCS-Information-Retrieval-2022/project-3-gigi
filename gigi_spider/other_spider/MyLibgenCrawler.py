import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import json
import time
import logging

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("monitor")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("monitor.log")
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)

url = 'http://libgen.rs/scimag/?'  # q=xxx

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

proxies = {'http': 'http://127.0.0.1:2388',
           'https': 'http://127.0.0.1:2388'}  # 爬取libgen需要设置代理

# 通过keyword搜索方式从网站中爬取电子书 q_list为query列表
q_list = [
    'transformer', 'deep+learning', 'machine+learning', 'neural+network', 'computer',
    'Computer+Vision', 'bert', 'gpt', 'artificial+Intelligence', 'natural+Language+Processing',
    'Information+Retrieval', 'database', 'computer+network', 'computer+science', 'software',
    'software+engineering', 'engineering', 'technology', 'robots', 'science',
    'Autopilot', 'big+data', 'cloud+computing', 'Quantum+physics', 'biology', 'Chemistry',
    'biochemistry', 'math', 'politics', 'China', 'America', 'data mining', 'Cluster computing',
    'File System', 'operating system', 'Finance', 'Grid computing', 'High Performance Computing',
    'Internet of Things', 'reinforcement learning', 'Western culture', 'africa',
    'Integrated circuit', 'assembly language', 'Compiler', 'discrete mathematics', 'Combinatorics',
    'Calculus', 'linear algebra', 'Probability statistics', 'data structure', 'python', 'java',
    'javascript', 'C language', 'C++', 'Computer Organization', 'world wide web', '5G networks',
    'Wi-Fi', 'economics', 'virtual reality', 'Marxism', 'political economics', 'Sociology',
    'Programming', 'Art', 'numerical analysis', 'matrix analysis', 'machine translation',
    'accounting', 'international trade', 'International Relations', 'convolution', 'automation',
    'Electronic information', 'Communication', 'electromagnetic', 'signal processing', 'photoelectricity',
    'Aerospace', 'astronavigation', 'space technology', 'rocket', 'cosmos', 'universe', 'Mechanics',
    'electromechanical', '56', 'history', 'military', 'football', 'basketball', 'sports',
    'eastern culture', 'ecology', 'environment protection', 'climate change', 'europe', 'asia',
    'relativity', 'fluid mechanics', 'solid mechanics', 'aerodynamics', 'architecture',
    'electrical engineering', 'Explosive mechanics'
]

if __name__ == "__main__":
    total = 0
    start = time.time()
    print('爬虫程序运行开始！')

    for q in q_list:
        for page in range(1, 5):  # 每次搜索结果小于等于4页，每页25条数据
            # print('q = {}, page = {}'.format(q, page))
            data = {
                'q': q,
                'page': str(page)
            }
            time.sleep(0.3)  # 主动延迟 防止爬取速度过快触发反爬机制
            response = requests.get(
                url=url, params=data, headers=headers, proxies=proxies)
            content = response.text
            # print(content)

            soup = BeautifulSoup(content, 'lxml')  # 利用BS4库解析网页内容
            tr_list = soup.select('tr')
            flag = 0
            for i in tr_list:
                if flag == 0:
                    flag = 1  # 第一个tr标签不是有效内容
                    continue
                dict = {
                    "author": i.find('td').text,  # 作者
                    "title": i.find('a').text,  # 标题
                    "url": 'http://libgen.rs' + i.find('a').get("href")  # 链接
                }
                # print(dict)
                total += 1
                data = json.dumps(dict, indent=1, ensure_ascii=False)
                with open('Libgen-Crawler.json', 'a', encoding='utf-8', newline='\n') as fp:
                    fp.write(data)

            if total % 100 == 0:  # 每爬取100条数据输出一次时间信息 并在日志中记录
                print(total)
                end = time.time()
                eplase = end - start
                print(eplase)
                logger.info(total)

    print('共爬取{}条文档数据！'.format(total))
    print('爬虫程序运行结束！')
    fp.close()
    end = time.time()
    eplase = end - start
    print(eplase)
