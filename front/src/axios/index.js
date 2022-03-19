import Vue from 'vue'
import axios from 'axios'

axios.defaults.withCredentials = true;
const http = axios.create({
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    // 'Access-Control-Allow-Credentials': true,
  },
  baseURL: 'http://127.0.0.1:12345/',
})
/**
 * 请求拦截
 */
http.interceptors.request.use(config => {
  //config.headers['u_id'] = Vue.cookie.get('u_id') // 请求头带上token
  return config
}, error => {
  return Promise.reject(error)
})
export default http
