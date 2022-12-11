# project-3-gigi

## 分工

| 任务     | 成员1  | 成员2  |
| -------- | ------ | ------ |
| 爬虫模块 | 钱海   | 张成喆 |
| 检索模块 | 米昊天 | 张圃瑒 |
| 展示模块 | 徐正斐 | 杨欣运 |

## 爬虫模块

### 1 数据来源

| 类别   | 网站            | 网址                                    |
| ------ | --------------- | --------------------------------------- |
| Paper  | SciHub          | http://www.sci-hub.ac.cn/               |
| e-book | library genesis | http://gen.lib.rus.ec/                  |
| e-book | eBooks          | http://www.ebooks.com/en-us/free/       |
| PPT    | PPT Silver      | https://www.slideserve.com/tress/silver |
| Video  | Bilibili        | https://www.bilibili.com/               |
| Video  | Youtube         | https://www.youtube.com/                |

### 2 要求

* 一个**MongoDB**数据库
* 在仓库`README`中给出爬取数据的**统计信息**，例如每个数据源爬取的标签数、字段覆盖率等

### 3 爬取信息

......

## 检索模块

### 1 要求

* 从MongoDB中读取数据实现**综合检索**，要求无论是输入`论文`、`电子书`，都能得到相应的检索结果

* 需要可以查看论文和电子书对应的PPT和视频，设计方法**去杂去重**，保证对齐的准确率

* 可以自己实现搜索算法，也可以使用已有的搜索引擎工具，比如[Elasticsearch](https://www.elastic.co/)

* 要求展示模块提供`论文电子书检索列表`、`相关视频查看按钮`、`相关文档查看按钮`，后两者需要展示相应链接并可以实现跳转

* 要求说明筛选PPT和视频的方法原理


### 2 检索接口

......

## 展示模块

### 1 要求

* 设计并实现一个学术类综合搜索引擎网站，包括三个页面

  * 首页/搜索页
  * 检索结果列表页

  * 论文/电子书详情页面：
    * 包含论文标题、作者、摘要、视频、文档等相关信息

* 展示样例如下图所示：

  * 搜索页面
  
  ![image-20221211133524659](https://s2.loli.net/2022/12/11/MlfnszYwdrKjV7c.png)
  
  * 搜索结果列表
  
    ![image-20221211133639580](https://s2.loli.net/2022/12/11/KlWuoinjNSGOQwr.png)
  
  * 论文详情页

### 2 展示需求

### 3 API

* 分页搜索的 GET 请求

  * `${baseUrl}/search?q=${q}&p=${p}`    q：查询的query；p：查询第几页
  * http://localhost:8100/search?q={bert}&p=${1}

* 分页搜索的响应格式

  ```json
  {
      "code ": code,
      "data": {
          "page": page,                                   // 当前第几页（从1开始）
          "searchCostTime": search_cost_time, // 搜索用时（单位为秒）
          "totalNums": total_nums,                   // 总查询条目数
          "pageNums": page_nums,                  // 总页数
          "hitList": [                                        // 当前页的命中列表
              {
                  "id" : "1",
                  "title": "Multiplex Graph Neural Network ...",
                  "abstract": "Extractive text summarization aims at ...",
                  "authors": ["Baoyu Jing", "Zeyu You", "Tao Yang"],
                  "doi": "10.18653/v1/2021.emnlp-main.11",
                  "url": "https://sci-hub.ee/10.18653/v1/2021.emnlp-main.11",
                  "year": 2021,
                  "month": 11,
                  "type": "conference",
                  "volume": "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
                  "source_url": "https://aclanthology.org/2021.emnlp-main.11/",
                  "pdf_url": "https://aclanthology.org/2021.emnlp-main.11.pdf",
                  "ebook_url": "https://aclanthology.org/2021.emnlp-main.11.pdf",
                  "ppt_url": "https://www.slideserve.com/vera/text-summarization",
                  "video_url": "https://aclanthology.org/2021.emnlp-main.11.mp4",
                  "citations_num": 31,         // 被引次数
                  "reference_list": [          // 参考文献列表
                      {"id": "0", "title": "Multiplex ...", "year": "2021"}, 
                      {"id": "4", "title": "Multiplex ...", "year": "2021"}, 
                      {"id": "5", "title": "Multiplex ...", "year": "2021"}
                  ]
              }
          ],
      }
  }
  ```
  
* 论文详情页的 GET 请求
  * `${baseUrl}/detail?id=${id}`    id：论文 id
  * http://localhost:8100/detail?id={1}

* 论文详情的响应格式

  ```json
  {
      "id": "1",
      "title": "Multiplex Graph Neural Network for Extractive Text Summarization",
      "authors": ["Baoyu Jing", "Zeyu You", "Tao Yang"],
      "abstract": "Extractive text summarization aims at ...",
      "doi": "10.18653/v1/2021.emnlp-main.11",
      "year": 2021,
      "month": 11,
      "type": "Conference",
      "venue": "EMNLP",
      "volume": "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
      "source_url": "https://aclanthology.org/2021.emnlp-main.11/",
      "pdf_url": "https://aclanthology.org/2021.emnlp-main.11.pdf",
      "ebook_url": "https://aclanthology.org/2021.emnlp-main.11.pdf",
      "ppt_url": "https://www.slideserve.com/vera/text-summarization",
      "video_url": "https://aclanthology.org/2021.emnlp-main.11.mp4",
      "citations_num": 31,         // 被引次数
      "reference_list": [          // 参考文献列表
          {"id": "0", "title": "Multiplex ...", "year": "2021"}, 
          {"id": "4", "title": "Multiplex ...", "year": "2021"}, 
          {"id": "5", "title": "Multiplex ...", "year": "2021"}
      ]     
  }
  ```

  

