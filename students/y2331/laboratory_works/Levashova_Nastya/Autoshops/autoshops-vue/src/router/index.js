import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Room from "@/components/Room";
import Masters from "@/components/Masters";
import Custumers from "@/components/Custumers";
import Cars from "@/components/Cars";
import Works from "@/components/Works";
import AddCustumer from "@/components/AddCustumer";
import AddCar from "@/components/AddCar";
import AddWork from "@/components/AddWork";
import Auth from "@/components/Auth";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/room',
      name: 'room',
      component: Room
    },
    {
      path: '/master',
      name: 'master',
      component: Masters
    },
    {
      path: '/custumer',
      name: 'custumer',
      component: Custumers
    },
    {
      path: '/cars',
      name: 'cars',
      component: Cars
    },
    {
      path: '/works',
      name: 'works',
      component: Works
    },
    {
      path: '/addcustumer',
      name: 'addcustumer',
      component: AddCustumer
    },
    {
      path: '/addcar',
      name: 'addcar',
      component: AddCar
    },
    {
      path: '/addwork',
      name: 'addwork',
      component: AddWork
    },
    {
      path: '/auth',
      name: 'auth',
      component: Auth
    }
  ]
})
