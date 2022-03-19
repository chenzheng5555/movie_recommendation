import Vue from 'vue'
import Router from 'vue-router'

import Login from '../views/user/login'
import Register from '../views/user/register'
import Main from '../views/main/main'
import Home from '../views/content/home'
import RecList from '../views/content/rec-list'
import HisData from '../views/content/his-data'
import Detail from '../views/content/detail'
import ChangePwd from '../views/user/changePwd'

Vue.use(Router)

const globalRoutes = [
  { path: '/', component: Login, name: 'login' },
  { path: '/register', component: Register, name: 'register' },
  { path: '/changePwd', component: ChangePwd, name: 'changePwd' },
  // {path: '/home',component: Home, name:'home'},
  // {path: '/main',component: Main, name:'main'},
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //  // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const mainRoutes = {
  path: '/',
  component: Main,
  name: 'main',
  redirect: { name: 'home' },
  meta: { title: '主入口整体布局' },
  children: [
    // 通过meta对象设置路由展示方式
    // 1. isTab: 是否通过tab展示内容, true: 是, false: 否
    // 2. iframeUrl: 是否通过iframe嵌套展示内容, '以http[s]://开头': 是, '': 否
    // 提示: 如需要通过iframe嵌套展示内容, 但不通过tab打开, 请自行创建组件使用iframe处理!
    { path: '/home', component: Home, name: 'home', meta: { title: '首页' } },
    { path: '/rec_list', component: RecList, name: 'rec-list', meta: { title: '推荐列表', isTab: true } },
    { path: '/his_data', component: HisData, name: 'his-data', meta: { title: '历史数据分析', isTab: true } },
    { path: '/detail/:m_id', component: Detail, name: 'detail', meta: { title: '', isTab: true } }
  ],
  // beforeEnter (to, from, next) {
  //   let token = Vue.cookie.get('token')
  //   if (!token || !/\S/.test(token)) {
  //     clearLoginInfo()
  //     next({ name: 'login' })
  //   }
  //   next()
  // }
}

const router = new Router({
  routes: globalRoutes.concat(mainRoutes)
})

router.beforeEach((to, from, next) =>{
  next()
})

export default router
