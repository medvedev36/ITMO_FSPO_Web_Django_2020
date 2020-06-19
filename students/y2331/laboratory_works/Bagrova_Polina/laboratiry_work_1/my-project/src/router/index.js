import Vue from 'vue'
import Router from 'vue-router'
import Autopark from '../components/Autopark'
import Login from "../components/Login"
import Clients from "../components/Clients"
import Drivers from "../components/Drivers"
import Cars from "../components/Cars"
import Manifests from "../components/Manifests"
import Orders from "../components/Orders"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Autopark',
      component: Autopark
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/clients',
      name: 'Clients',
      component: Clients
    },
    {
      path: '/drivers',
      name: 'Drivers',
      component: Drivers
    },
    {
      path: '/cars',
      name: 'Cars',
      component: Cars
    },
    {
      path: '/manifests',
      name: 'Manifests',
      component: Manifests
    },
    {
      path: '/orders',
      name: 'Orders',
      component: Orders
    },
  ]
})
