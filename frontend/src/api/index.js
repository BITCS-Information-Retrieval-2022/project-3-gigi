// import axios from './request.js'
import axios from 'axios'

// import store from '@/store'

// let baseUrl = 'http://39.106.132.154:8000/api/v1'
// const ip = 'http://39.106.132.154:8000'
// const ip = 'http://localhost:8100'
// const baseUrl = `${ip}/api/v1`
const baseUrl = 'http://mock/api'


export function getIP(){
  return ip
}
// http://localhost:8000/api/v1/search?q=xxxxx&p=yyyy
//获取搜索结果
export function getSearchResult(q, p) {
  return axios.get(`${baseUrl}/search?q=${q}&p=${p}`)
}
//根据输入的部分文本获取搜索建议
export function getSearchSuggest(someText) {
  return axios.get(`${baseUrl}/search/suggest?input=${someText}`)
}

