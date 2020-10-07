<template>
  <div id="app">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <link rel="stylesheet" href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css">
    <link rel="stylesheet" href="https://unpkg.com/muse-ui/dist/muse-ui.css">

    <router-view/>
  </div>
</template>

<script>

import Vue from 'vue';
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import theme from 'muse-ui/lib/theme';

theme.add('my', {
  primary: '#ff8f00',
  secondary: '#FF0000',
  success: '#FF0000',
  warning: '#FF0000',
}, 'light');

theme.use('my');
Vue.use(MuseUI);



export default {
  name: 'App',

}
</script>

<style>
#app {
  font-family: "Roboto Thin", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0;
}

</style>
