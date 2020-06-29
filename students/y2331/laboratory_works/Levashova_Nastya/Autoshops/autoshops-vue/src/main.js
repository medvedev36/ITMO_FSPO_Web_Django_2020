// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'

import theme from 'muse-ui/lib/theme';

theme.add('teal', {
  primary: '#009688',
  secondary: '#e57373',
  success: '#4caf50',
  warning: '#f44336',
}, 'light');

theme.use('teal');

Vue.use(MuseUI)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
