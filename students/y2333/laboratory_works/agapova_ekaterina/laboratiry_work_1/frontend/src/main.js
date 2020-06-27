//Испорт всех необходимых библеотек и файлов
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import routes from './routes';
import axios from 'axios';
window.axios = axios;
//Создание Vue Router
const router = new VueRouter({
    routes
})
//Подключение Bootstrap
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
//Подключение роутера
Vue.use(VueRouter)
new Vue({
  el: '#app',
  render: h => h(App),
  data: {
    //Произведен ли вход
    loggedIn: false,
    //Является ли пользователь администратором
    isAdmin: false,
    //Данные о пользователе
    user: {

    },
  },
  router
})
