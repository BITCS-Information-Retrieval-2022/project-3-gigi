# project-3-gigi
## 项目介绍

本项目构建了学术资源爬虫系统，从 ACM 网站、library genesis 电子书网站、[YouTube](https://www.youtube.com/)、[PPT Silver](https://www.slideserve.com/tress/silver) 网站分别爬取了一定数据量的论文、电子书、学术视频和 PPT。并将这些数据保存在 MongoDB 中，之后通过 Elasticsearch 工具构建了针对这些学术资源的检索系统，通过 VueJs 前端框架构建了学术资源的综合检索展示平台。

## 小组分工

| 姓名   | 学号       | 分工                                                         |
| ------ | ---------- | ------------------------------------------------------------ |
| 钱海   | 3220220954 | 爬虫：实现YouTube、B站、library genesis 电子书网站爬虫       |
| 张成喆 | 3120220990 | 爬虫：实现ACM DL、SciHub、PPT Silver爬虫，进行MongoDB数据存取 |
| 米昊天 | 3120220959 | 后端：主要负责检索模块，实现后端与前端的通信和es检索结果的筛选、排序 |
| 张圃瑒 | 3120220994 | 后端：主要负责检索模块，创建index，将爬虫数据存入es，实现分页与id搜索 |
| 徐正斐 | 3120220978 | 前端：构建前端的基本框架和组件，完成状态管理、路由交互、网络请求和单元测试 |
| 杨欣运 | 3120221010 | 前端：构建前端部分框架，修改一些bug                          |

## 功能特色

1. 分页查询
   * 每页显示固定数量的查询结果，解决一次查询结果过多的问题。
   * 能够减轻网络负担。
2. 网页状态管理
   * 使用Vuex缓存查询结果，使得网页前后跳转时，不用多次请求数据。
3. 视频与文档的对齐
4. ......

## 项目部署

### 1 爬虫环境配置

### 2 检索环境配置

1. ElasticSearch配置

  * ElasticSearch安装并解压
   ```bash
     wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.2-linux-x86_64.tar.gz
     tar -zxvf elasticsearch-7.13.2-linux-x86_64.tar.gz -C /usr/local
   ```

### 3 前端环境配置

前端环境依赖于 NodeJs 环境和 Vue3框架，具体依赖的第三方库可参见 `frontend/package.json`

1. 前端环境可以部署在Windows、Linux、MacOS，以 Ubuntu 为例

2. 安装 nodejs

   ```bash
   sudo apt-get install nodejs
   sudo apt-get install npm
   ```

3. 配置项目依赖

   * 将仓库克隆至本地

   * 切换到 frondend 目录下：`cd project-3-gigi/fronted`

   * 安装依赖的第三方库：`npm install`

   * 启动前端程序：`npm run serve`

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

本项目前端基于Vue3框架开发，Vue是一款用于构建用户界面的 JavaScript 框架。它基于标准 HTML、CSS 和 JavaScript 构建，并提供了一套声明式的、组件化的编程模型，能够高效地开发用户界面。

* **组件树**

  本项目基于Vue的组件式编程，开发了相应的组件库和前端应用，其中前端界面主要包含三个，对应于`frontend/src/views/`目录下的三个文件

  * 主搜索页：对应 `Home.vue`，主要包含一个搜索框，能够输入关键词查询相关论文、电子书。
  * 搜索结果列表展示页：对应` ResultList.vue`，对搜索请求进行分页查询和展示，展示相关的论文和电子书列表，相关视频、PPT、PDF、来源、引用量、摘要等信息。
  * 详情页，对应 `Detail.vue`，查看论文或电子书的详情信息。

  上述三个界面分别包含各自的组件，项目前端部分的组件树如下图所示：

  <img src="https://s2.loli.net/2022/12/23/RmLfaSrwbKN9eQZ.png" alt="GigiScholar-frontend" style="zoom: 40%;" />

  组件式开发能够提高开发效率、方便代码复用、提高项目代码的可维护性。

* **路由交互**

  前端界面的路由跳转依赖 `Vue Router ` 库，已经通过组件构建了相关的应用，现在需要讲组件映射到路由上，因此使用了 `Vue Router `  库。`Vue Router ` 是 是 Vue 的官方路由库，能够模块化地进行导航控制，还支持 HTML5 的 history 和 hash 模式，能够实现网页应用的前进后退等操作。

  本项目的前端路由模块对应于 `frontend/src/router` ，具体的路由策略如下：

  ```javascript
  const routes = [
      {
          path: '/',
          name: 'home',
          component: Home
      },
      {
          path: '/search',
          name: 'search',
          component: ResultList
      },
      {
          path: '/detail',
          name: 'detail',
          component: Detail
      }
  ]
  ```

  在项目的入口 `App.vue`，通过路由视图标签 `<router-view />` 将上述路由规则和各个组件绑定。此外本项目还使用了声明式、编程式两种路由导航方式。

  * 声明式路由导航：使用 `<router-link></router-link>` 标签进行跳转，下面的例子表示点击搜索图标，根据路由规则跳转到 `/search` 对应的 `ResultList` 组件，参数为查询关键词 <u>searchQuery</u> 和请求的页码 <u>1</u> 。

    ```vue
    <router-link :to="{ path: '/search', query: { q: searchQuery, p: 1 } }">
    	<svg class="icon" aria-hidden="true">
    		<use xlink:href="#icon-sousuo"></use>
    	</svg>
    </router-link>
    ```

  * 编程式路由导航：使用 `router.push` 方法跳转到相应的URL。这个方法会向 history 栈添加一个新的记录，所以，当用户点击浏览器后退按钮时，会回到之前的 URL。当点击 `<router-link>` 时，内部会调用该方法，因此两者等价，上述跳转对应于下面语句：

    ```javascript
    router.push({ path: "/search", query: { q: searchQuery.value, p: 1 } });
    ```

  通过上述两种方法，我们实现了前端的页面跳转和参数传递。

* 状态管理

  本项目使用 Vuex 进行各组件的状态管理，状态管理的核心是 `store` 能够集中式存储管理应用中所有组件的状态，对应于代码 `frontend/src/store` ，本项目将 SearchValue、SearchResult、DetailResult 作为保存的组件状态，通过保存在 `store` 中，使得通过前进后退操作网页时，能够直接进行本地渲染，避免再次进行网络请求。

  通过使用 Vuex 进行前端状态管理，缩短了网页的延迟，减少了网页对后端的请求次数，降低了后端的并发压力。

* 网络请求

  本项目使用 `axios` 进行前端向后端发现 get 请求。`axios` 是一个流行的 ajax 库，支持异步的 ajax 请求。本项目中主要涉及两个网络请求，如下所示：

  ```javascript
  //获取搜索结果
  export function getSearchResult(q, p) {
      return axios.get(`${baseUrl}/search`, {
          params: {
              q: q,
              p: p
          }
      })
  }
  //获取单篇论文具体信息
  export function getDetail(id) {
      console.log('getDetail')
      return axios.get(`${baseUrl}/detail`, {
          params: {
              id: id
          }
      })
  }
  ```

  上述两个函数需要在异步 (`async` 关键词修饰的）的函数中，通过 `await` 等待异步方法执行完成。

* 单元测试

  本项目使用 `Mock.js` 进行单元测试，`Mock.js`是一个模拟数据生成器，可以在后端没有完成时进行自动化测试。通过 `Mock` 能够模拟 Ajax 请求，返回类型丰富的模拟数据，从而进行前后端开发的分离测试。

#### 3.2 效果展示

1. 主搜索页展示

   <img src="https://s2.loli.net/2022/12/23/QfvR9TbSJFGn7k4.png" alt="img" style="zoom:50%;" />

2. 搜索结果列表展示页

   <img src="https://s2.loli.net/2022/12/23/F7Zp61qultx5jQV.png" alt="img" style="zoom: 33%;" />

3. 搜索结果详情页

   <img src="https://s2.loli.net/2022/12/23/lj7wCqDhNWuHvx3.png" alt="img" style="zoom:20%;" />

   

