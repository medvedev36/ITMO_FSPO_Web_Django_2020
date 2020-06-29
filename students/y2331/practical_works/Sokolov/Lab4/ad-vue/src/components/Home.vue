<!--Интерфейс главной страницы -->
<template>
  <mu-container>
    <mu-row>
      <mu-appbar style="width: 100%;" color="primary">
        Реклама на ТВ
        <mu-button flat slot="right" v-if="!auth" @click="login">Войти</mu-button>
        <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
        <mu-button flat slot="left" color="primary"></mu-button>
      </mu-appbar>
    </mu-row>
      <mu-flex class="flex-wrapper1" justify-content="center" align-items="center">
        <mu-button full-width color="secondary" @click="shows">ТВ программы</mu-button>
      </mu-flex>
      <mu-flex class="flex-wrapper1" align-items="center" text="left">
          <mu-button full-width color="secondary" @click="advertising">Рекламные ролики</mu-button>
        </mu-flex>
      <mu-flex class="flex-wrapper1" justify-content="center" align-items="center">
          <mu-button full-width color="secondary" @click="adBreak">Рекламные показы</mu-button>
        </mu-flex>
  </mu-container>
</template>

<script>
  import Shows from "./Shows";
  import Advertising from "./Advertising";
  import AdBreak from "./AdBreak";

    export default {
        name: "Home",
        components: {Shows, Advertising, AdBreak},
        computed:{
          auth(){
            if(sessionStorage.getItem("auth_token")){
              return true
            }
          }
        },
        methods:{
          shows(){
            this.$router.push({name:"shows"})
          },
          advertising(){
            this.$router.push({name:"advertising"})
          },
          adBreak(){
            this.$router.push({name:"adbreak"})
          },
          login(){
            this.$router.push({name:"login"})
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
  width: 98%;
  height: 56px;
  margin-top: 20px;
  margin-left: 10px;
  text-align: left;
}
</style>

