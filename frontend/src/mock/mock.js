/*
 * @File    :  /frontend/src/mock/mock.js
 * @Author  :  xuzf
 * @Contact :  xuzhengfei-email@qq.com
 * @Create  :  2022-11-12 10:54:23
 * @Update  :  2022-11-12 11:18:25
 * @Desc    :  None
 */
//引入mockjs
import { mock } from 'mockjs';   //安装的mockjs，并不是创建的mock.js

//使用mockjs模拟数据
mock(RegExp('http://mock/api/search' + '.*'), 'get', function () { //当post或get请求到/api/data路由时Mock会拦截请求并返回上面的数据
    let menu = [
        {
            title: "资料检索",
            list: ["条件检索", "关键字检索"],
            id: 1
        },
        {
            title: "借阅管理",
            list: ["条件检索", "关键字检索"],
            id: 2
        },
        {
            title: "统计分析",
            list: ["条件检索", "关键字检索"],
            id: 3
        },
        {
            title: "系统管理",
            list: ["条件检索", "关键字检索"],
            id: 4
        },
    ];
    console.log("sdasdasdasdasdadadasda!!!!!!!!")
    let hitList = [
        {
            page_url: "www.baidu.com",
            title: "百度",
            content: "后来加了参数，mockjs好像不能识别了，返回404.这个该怎么解决，真的不能加参数吗，但是我总感觉这个不太对"
        },
                {
            page_url: "www.baidu.com",
            title: "百度",
            content: "后来加了参数，mockjs好像不能识别了，返回404.这个该怎么解决，真的不能加参数吗，但是我总感觉这个不太对"
        }
    ]

    return {
        totalNums: 1,
        searchCostTime: 0.01,
        hitList: hitList
    }
})


// //使用mockjs模拟数据
// mock('http://mock/api/headimage', 'get', function () {//当post或get请求到/api/data路由时Mock会拦截请求并返回上面的数据
//     let imgUrl = ['http://122.114.62.128:8003/Images/banner0.png', 'http://122.114.62.128:8003/Images/banner1.png']

//     return {
//         data: imgUrl
//     }
// })