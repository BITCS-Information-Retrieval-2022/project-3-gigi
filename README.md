# project-3-gigi
## 项目介绍

本项目构建了学术资源爬虫系统，从 ACM 网站、library genesis 电子书网站、[YouTube](https://www.youtube.com/)、[PPT Silver](https://www.slideserve.com/tress/silver) 网站分别爬取了一定数据量的论文、电子书、学术视频和 PPT。并将这些数据保存在 MongoDB 中，之后通过 Elasticsearch 工具构建了针对这些学术资源的检索系统，通过 VueJs 前端框架构建了学术资源的综合检索展示平台。

## 小组分工

| 姓名   | 学号       | 分工                                                       |
| ------ | ---------- | ---------------------------------------------------------- |
| 钱海   | 3220220954 | 爬虫：实现YouTube、B站、library genesis 电子书网站爬虫       |
| 张成喆 | 3120220990 | 爬虫：实现ACM DL、SciHub、PPT Silver爬虫，进行MongoDB数据存取 |
| 米昊天 | 3120220959 | 后端：主要负责检索模块，实现后端与前端的通信和es检索结果的筛选、排序 |
| 张圃瑒 | 3120220994 | 后端：主要负责检索模块，创建index，将爬虫数据存入es，实现分页与id搜索 ｜               
| 徐正斐 | 3120220978 | 前端：构建前端的基本框架和组件，完成Vuex状态管理和路由交互 |
| 杨欣运 | 3120221010 | 前端：构建前端部分框架，修改一些bug                        |

## 功能特色

1. 分页查询
   * 每页显示固定数量的查询结果，解决一次查询结果过多的问题。
   * 能够减轻网络负担。
2. 视频与文档的对齐
3. ......

## 项目部署

### 1 爬虫环境配置

### 2 检索环境配置

### 3 前端环境配置

前端环境依赖于 NodeJs 环境和 Vue3框架，具体依赖的第三方库可参见 `frontend/package.json`

1. 前端环境可以部署在Windows、Linux、MacOS，以 Ubuntu 为例

2. 安装 nodejs

   ```bash
   sudo apt-get install nodejs
   sudo apt-get install npm
   ```

3. 配置项目依赖

   * 将仓库克隆至本地：`git clone https://github.com/BITCS-Information-Retrieval-2022/project-3-gigi.git`

   * 切换到 frondend 目录下：`cd project-3-gigi/fronted`

   * 安装依赖的第三方库：`npm install`

   * 启动前端程序：`npm run serve`

4. 前端部署

   * 

## 系统整体架构

图

## 各模块设计原理和效果展示

### 1 爬虫模块

#### 1.1 设计原理

#### 1.2 效果展示

### 2 检索模块

#### 2.1 设计原理

#### 2.2 效果展示


### 3 展示模块

#### 3.1 设计原理

#### 3.2 效果展示



