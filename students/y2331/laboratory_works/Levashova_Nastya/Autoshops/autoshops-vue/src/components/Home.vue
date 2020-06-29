<template>
  <mu-container>
    <mu-row>
      <mu-appbar style="width: 100%;" color="primary">
        <mu-menu slot="left">
        <mu-button flat>Меню</mu-button>
        <mu-list slot="content">
          <mu-list-item button v-if="auth" @click="goShops">
            <mu-list-item-content>
              <mu-list-item-title>Автомастерские</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button v-if="auth" @click="goMasters">
            <mu-list-item-content>
              <mu-list-item-title>Мастера</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button v-if="auth" @click="goCustumers">
            <mu-list-item-content>
              <mu-list-item-title>Клиенты автомастерских</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button v-if="auth" @click="goCars">
            <mu-list-item-content>
              <mu-list-item-title>Автомобили</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button v-if="auth" @click="goWorks">
            <mu-list-item-content>
              <mu-list-item-title>Работы</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
        Сервис для автомастерских
        <mu-button flat slot="right" v-if="!auth" @click="goLogin">Войти</mu-button>
        <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
      </mu-appbar>
      <mu-flex class="flex-wrapper1" justify-content="start"><h2>Вы находитесь на сервисе автомастерских городской службы хозяйствования.</h2></mu-flex>
      <mu-flex class="flex-wrapper2" justify-content="start" v-if="auth"><h2>На сервисе предоставлена информация по следующим категориям:</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	автомастерские;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	работающие мастера;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	клиенты автомастерских;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	обслуживаемые автомобили;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	выполненные или ведущиеся работы.</h2></mu-flex>
      <mu-flex class="flex-wrapper2" justify-content="start" v-if="auth"><h2>Предоставлена возможность добавления следующих данных:</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	клиента автомастерских;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	обслуживаемого автомобиля;</h2></mu-flex>
      <mu-flex class="flex-wrapper3" justify-content="start" v-if="auth"><h2>•	выполненной или ведущийся работы.</h2></mu-flex>
      <mu-flex class="flex-wrapper2" justify-content="start" v-else><h2>Для получения доступа к информации авторизируйтесь.</h2></mu-flex>
    </mu-row>
  </mu-container>
</template>

<script>
  import Room from "./Room";
  import Masters from "./Masters";
  import Custumers from "./Custumers";
  import Cars from "./Cars";
  import Works from "./Works";

  export default {
    name: 'Home',
    components: {Room, Masters, Custumers, Cars, Works},
    computed:{
      auth(){
        if(sessionStorage.getItem("auth_token")){
          return true
        }
      }
    },
    methods:{
      goLogin(){
        this.$router.push({name:"login"})
      },
      goShops(){
        this.$router.push({name:"room"})
      },
      goMasters(){
        this.$router.push({name:"master"})
      },
      goCustumers(){
        this.$router.push({name:"custumer"})
      },
      goCars(){
        this.$router.push({name:"cars"})
      },
      goWorks(){
        this.$router.push({name:"works"})
      },
      logout(){
        sessionStorage.removeItem("auth_token")
        window.location = '/'
      }
    },
  }
</script>

<style scoped>
.flex-wrapper1 {
  width: 100%;
  height: 56px;
  margin-top: 50px;
  margin-left: 15px;
}
.flex-wrapper2 {
  width: 100%;
  height: 56px;
  margin-top: 1px;
  margin-left: 15px;
}
.flex-wrapper3 {
  width: 100%;
  height: 56px;
  margin-top: 1px;
  margin-left: 50px;
}
</style>
