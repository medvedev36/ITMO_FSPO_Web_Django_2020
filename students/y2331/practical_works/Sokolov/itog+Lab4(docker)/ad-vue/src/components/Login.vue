<!--Интерфейс для авторизации-->
<template>
  <mu-container>
    <mu-row>
      <mu-appbar style="width: 100%;" color="primary">
        Авторизация
      </mu-appbar>
    </mu-row>
    <mu-text-field class="flex-wrapper1" v-model="login" type="text" placeholder="Логин"></mu-text-field><br/>
    <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field><br/>
    <mu-row>
      <mu-col span="2"><div class="grid-cell"></div></mu-col>
      <mu-col span="2"><div class="grid-cell"></div></mu-col>
      <mu-col span="1"><div class="grid-cell"></div></mu-col>
      <mu-col span="1"><div class="grid-cell">
        <mu-flex justify-content="center">
          <mu-button color="primary" @click="logingo" >Вход</mu-button>
        </mu-flex></div></mu-col>
        <mu-col span="1"><div class="grid-cell">
        <mu-button flat color="secondary" @click="reg">Регистрация</mu-button>
      </div></mu-col>
      <mu-col span="2"><div class="grid-cell"></div></mu-col>
      <mu-col span="2"><div class="grid-cell"></div></mu-col>
  </mu-row>
  </mu-container>
</template>

<script>
  import $ from 'jquery'
  import Reg from "./Reg";
  import Home from "./Home";

  export default {
    name: 'Login',
    components: {Reg, Home},
    data(){
      return{
        login: '',
        password: '',
      }
    },
    methods:{
      logingo() {
        $.ajax({
          url:"http://127.0.0.1:8000/auth/token/login/",
          type: "POST",
          data:{
            username: this.login,
            password: this.password
          },
          success:(response) => {
            sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
            this.$router.push({name:"home"})
          },
          error:(response) => {
            if(response.status === 400){
              alert("Неверный логин или пароль!")
            }
          }
        })
      },
      reg(){
        this.$router.push({name:"reg"})
      }
    }
  }
</script>

<style scoped>
.flex-wrapper1 {
  margin-top: 70px;
}
</style>
