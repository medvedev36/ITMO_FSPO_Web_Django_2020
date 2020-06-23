import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import routes from './routes';
import axios from 'axios';
window.axios = axios;
const router = new VueRouter({
    routes
})
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)
new Vue({
  el: '#app',
  render: h => h(App),
  data: {
    loggedIn: false,
    isAdmin: false,
    user: {

    },
  },
  router
})
