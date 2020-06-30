import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Shows from '@/components/Shows'
import Advertising from '@/components/Advertising'
import AdBreak from "@/components/AdBreak";
import Login from "@/components/Login";
import Reg from "@/components/Reg";
import AddShow from "@/components/AddShow";
import AddAdvertising from "../components/AddAdvertising";
import Addadbreak from "../components/Addadbreak";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
     {
      path: '/shows',
      name: 'shows',
      component: Shows
    },
     {
      path: '/advertising',
      name: 'advertising',
      component: Advertising
    },
     {
      path: '/adbreak',
      name: 'adbreak',
      component: AdBreak
    },
     {
      path: '/login',
      name: 'login',
      component: Login
    },
     {
      path: '/reg',
      name: 'reg',
      component: Reg
    },
     {
      path: '/addshow',
      name: 'addshow',
      component: AddShow
    },
     {
      path: '/addadver',
      name: 'addadver',
      component: AddAdvertising
    },
     {
      path: '/addbreak',
      name: 'addbreak',
      component: Addadbreak
    }
  ]
})
