<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      Авторизация
    </mu-appbar>
    <mu-text-field v-model="login" type="text" placeholder="Логин"></mu-text-field> <br>
    <mu-text-field v-model="password" type="password" placeholder="Пароль"></mu-text-field> <br>
    <mu-button @click="setLogin">Войти</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password,
                    },
                    success: (response) => {
                        alert("Успешный вход")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "Autopark"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    },
                })
            },
        }
    }
</script>

<style scoped>

</style>
