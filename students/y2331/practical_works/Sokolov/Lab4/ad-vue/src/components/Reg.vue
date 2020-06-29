<!--Интерфейс для регистрации-->
<template>
  <mu-container>
    <mu-row>
      <mu-appbar style="width: 100%;" color="primary">
        Регистрация
        <mu-button flat slot="right" @click="tologin">Войти</mu-button>
      </mu-appbar>
    </mu-row>
    <mu-text-field class="flex-wrapper1" v-model="login" placeholder="Логин"></mu-text-field><br/>
    <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field><br/>
    <mu-text-field v-model="email" placeholder="Электронная почта"></mu-text-field><br/>
    <mu-button small color="primary" @click="logingo" >Зарегистрироваться</mu-button>
  </mu-container>
</template>

<script>
    import $ from "jquery";
    import Login from "./Login";

    export default {
        name: "Reg",
        components: {Login,},
        data(){
          return{
              login: '',
              password: '',
              email: '',
            }
        },
        methods:{
          logingo() {
            $.ajax({
              url:"http://127.0.0.1:8000/auth/users/",
              type: "POST",
              data:{
                username: this.login,
                password: this.password,
                email: this.email,
              },
              success:(response) => {
                alert("Успешная регистрация!")
              },
              error:(response) => {
                alert("Ошибка регистрации!")
              }
            })
          },
          tologin(){
            this.$router.push({name:"login"})
          },
        }
    }
</script>

<style scoped>
.flex-wrapper1 {
  margin-top: 70px;
}
</style>
