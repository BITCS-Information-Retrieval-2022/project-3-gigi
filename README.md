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

  <img src="https://s2.loli.net/2022/11/04/YOKiMnTbyZVNhIk.png" alt="img" style="zoom:60%;" />

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

  <img src="https://s2.loli.net/2022/11/04/n2a5qh1CSuWKGPc.png" alt="微信图片 20221018190418" style="zoom:60%;" />

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
                  "id" : id,
                  "title": title,
                  "abstract": abstract,
                  "authors": [author1, author2, ...],
                  "doi": doi,
                  "url": url,
                  "year": year,
                  "month": month,
                  "type": type,
                  "volume": volume,
                  "source_url": source_url,
                  "pdf_url": pdf_url,
                  "ebook_url": ebook_url,
                  "ppt_url": ppt_url,
                  "video_url": video_url,
                  "citations_num": citations_num,         // 被引次数
                  "reference_list": [ref1, ref2, ...]     // 参考文献列表
              }
          ],
      }
  }
  ```

  

  

