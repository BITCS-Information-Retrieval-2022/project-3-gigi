import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ResultList from '../views/ResultList.vue'
import Detail from '../views/Detail.vue'

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

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
