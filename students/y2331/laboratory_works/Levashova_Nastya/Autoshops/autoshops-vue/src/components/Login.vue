<template>
  <mu-container>
    <mu-text-field v-model="login" type="text" placeholder="Логин"></mu-text-field><br/>
    <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field><br/>
    <mu-flex justify-content="center">
      <mu-button color="primary" @click="setLogin">Вход</mu-button>
    </mu-flex>
    <mu-button flat color="primary" @click="goAuth">Регистрация</mu-button>
  </mu-container>
</template>

<script>
  import $ from 'jquery'
  import Auth from "./Auth";

  export default {
    name: 'Login',
    components: {Auth},
    data(){
      return{
        login: '',
        password: '',
      }
    },
    methods:{
      setLogin() {
        $.ajax({
          url:"http://127.0.0.1:8000/auth/token/login/",
          type: "POST",
          data:{
            username: this.login,
            password: this.password
          },
          success:(response) => {
            // alert("Вы вошли!")
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
      goAuth(){
        this.$router.push({name:"auth"})
      }
    }
  }
</script>

<style scoped>

</style>
