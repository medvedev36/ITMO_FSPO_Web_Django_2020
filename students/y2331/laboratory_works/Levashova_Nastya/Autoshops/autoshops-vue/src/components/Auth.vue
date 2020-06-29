<template>
  <mu-container>
    <mu-text-field v-model="login" placeholder="Логин"></mu-text-field><br/>
    <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field><br/>
    <mu-text-field v-model="email" placeholder="Email"></mu-text-field><br/>
    <mu-button color="primary" @click="setLogin" v-if="login && password && email">Зарегистрироваться</mu-button>
    <h4 v-else>Заполните все поля!</h4>
  </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Auth",
        data(){
          return{
              login: '',
              password: '',
              email: '',
            }
        },
        methods:{
          setLogin() {
            $.ajax({
              url:"http://127.0.0.1:8000/auth/users/",
              type: "POST",
              data:{
                username: this.login,
                password: this.password,
                email: this.email,
              },
              success:(response) => {
                alert("Регистрация прошла успешно!")
              },
              error:(response) => {
                  alert("Ошибка регистрации! Возможно введённый пароль слишком короткий или слишком широко распространён. Он должен содержать как минимум 8 символов.")
              }
            })
          },
          goLogin(){
            this.$router.push({name:"login"})
          }
        }
    }
</script>

<style scoped>

</style>
