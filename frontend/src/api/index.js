import axios from 'axios'


let baseUrl = 'http://10.108.17.218:12222'
// const baseUrl = 'http://mock/api'


export function getIP() {
    return ip
}
// http://localhost:8000/api/v1/search?q=xxxxx&p=yyyy
//获取搜索结果
export function getSearchResult(q, p) {
    console.log("getSearchResult")
    return axios.post(`${baseUrl}/search`, {
        params: {
            q: q,
            p: p
        }
    })
}

//获取单篇论文具体信息
export function getDetail(id) {
    console.log('getDetail')
    return axios.post(`${baseUrl}/detail`, {
        params: {
            id: id
        }
    })
}

//根据输入的部分文本获取搜索建议
export function getSearchSuggest(someText) {
    console.log("getSearchSuggest")
    return axios.get(`${baseUrl}/search/suggest`, {
        params: {
            input: someText
        }
    })
}

