<template>
<div style="width: 100%">
  <div v-if="auth">
  <mu-appbar  class="main_appbar" color="primary">

    <mu-button flat slot="left" @click="menu_tab = 0">Routes</mu-button>
    <mu-button flat slot="left" @click="menu_tab = 1">Buses</mu-button>
    <mu-button flat slot="left" @click="menu_tab = 2">Crew members</mu-button>
    <mu-button flat slot="left" @click="menu_tab = 3">Completed trips</mu-button>

    <mu-button flat slot="right" v-if="auth" @click="logout">Logout</mu-button>
  </mu-appbar>


  <div v-show="menu_tab==0">
  <mu-flex justify-content="center" >
    <mu-expand-transition>
      <mu-paper :z-depth="1" class="miniapp" >
        <Routes></Routes>
      </mu-paper>
    </mu-expand-transition>
  </mu-flex>
  </div>

  <div v-show="menu_tab==1">
  <mu-flex justify-content="center" >
    <mu-expand-transition>
      <mu-paper :z-depth="1" class="miniapp" >
        <Buses></Buses>
      </mu-paper>
    </mu-expand-transition>
  </mu-flex>
  </div>

  <div v-show="menu_tab==2">
  <mu-flex justify-content="center" >
    <mu-expand-transition>
      <mu-paper :z-depth="1" class="miniapp" >
        <Crew></Crew>
      </mu-paper>
    </mu-expand-transition>
  </mu-flex>
  </div>

  <div v-show="menu_tab==3">
  <mu-flex justify-content="center" >
    <mu-expand-transition>
      <mu-paper :z-depth="1" class="miniapp" >
        <Trips></Trips>
      </mu-paper>
    </mu-expand-transition>
  </mu-flex>
  </div>
</div>
  <Login class="login" v-else ></Login>


</div>

</template>

<script>

import Buses from "./Buses";
import Login from "./Login";
import Routes from "./Routes";
import Crew from "./Crew";
import Trips from "./Trips";
import $ from "jquery";


export default {

  name: "Home",
  components: {Login, Buses,Routes,Crew,Trips},
  data() {
    return {
      menu_tab: 0
    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("auth_token")) {
        return true
      }
    }
  },
  methods: {
    goLogin(){
      this.$router.push({name: "login"})
    },
    logout() {
      sessionStorage.removeItem("auth_token")
      window.location = '/'
    },
  }
}
</script>

<style >
.main_appbar{
  width: 100%;
  min-height: 20%;
}

.miniapp {
  margin-top: 50px;
  width: 90%;
  height: 70%;
}

.login {
  max-width: 70%;
  align:center;
}
</style>
