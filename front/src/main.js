import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import http from './axios'
import VueCookie from 'vue-cookie'

import './element-ui'
import './assets/scss/index.scss'


Vue.use(VueCookie)
Vue.config.productionTip = false
Vue.prototype.$http = http

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
