import { createStore } from 'vuex'
// 接口引入

export default createStore({
    state: {
        SearchValue: '',
        SearchResult: {
            hitList: [],
        },
        DetailResult: {
            item: {}
        },
        Jwt: JSON.parse(localStorage.getItem("jwt")) || '',
    },
    mutations: {
        SetSearchValue(state, value) {
            state.SearchValue = value
            // 同时保存到本地
            let historyList = JSON.parse(localStorage.getItem("historyList")) || [];
            // 不添加重复值及空值
            if (historyList.indexOf(value) == -1 && value) {
                historyList.push(value)
                localStorage.setItem("historyList", JSON.stringify(historyList));
            }

        },
        SetSearchResult(state, value) {
            state.SearchResult = value['data']
        },
        SetDetailResult(state, value) {
            state.DetailResult.item = value
        },
        SetJwt(state, value) {
            console.log("将jwt提交到了vuex")
            state.Jwt = value
            localStorage.setItem("jwt", JSON.stringify(value));
        }
    },
    actions: {
        // TODO 这些方法放在vuex里面有什么作用，其他地方直接调用api里面的不好吗
    },
    modules: {
    }
})
