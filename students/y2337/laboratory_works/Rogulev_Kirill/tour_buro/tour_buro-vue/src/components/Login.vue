<template>
  <mu-container>
  <mu-form ref="form" :model="loginForm" class="miniapp">
    <mu-form-item help-text="Login" prop="username">
      <mu-text-field v-model="loginForm.login" prop="username"></mu-text-field>
    </mu-form-item>
    <mu-form-item help-text="Password" prop="password">
        <mu-text-field
          type="password" v-model="loginForm.password"
          :action-icon="password_visibility ? 'visibility_off' : 'visibility'" :action-click="() => (password_visibility = !password_visibility)" :type="password_visibility ? 'text' : 'password'"
        >
        </mu-text-field>
    </mu-form-item>
    <mu-form-item>
      <mu-button color="primary" @click="setLogin">Login</mu-button>
    </mu-form-item>
  </mu-form>
</mu-container>
</template>

<script>
import $ from "jquery"

export default {
  name: "Login",
  data(){
      return{
        loginForm: {
          login: '',
          password: ''
        },
        password_visibility: false
      }
  },
  methods: {
    setLogin(){
      //console.log("Trying to log with " + this.loginForm.login + ":" + this.loginForm.password)
      $.ajax({
          url: "http://127.0.0.1:8000/auth/token/login/",
          type: "POST",
          data: {
              username: this.loginForm.login,
              password: this.loginForm.password
          },
          success: (response) => {
            alert("Successful login")
            sessionStorage.setItem("auth_token",response.data.attributes.auth_token)
            this.$router.go()
          },
          error: (response) => {
            switch(response.status){
              case 400:
                alert("Wrong login or password")
                break

              default:
                alert("Unknown error. See console log for detauils")
                console.log(response.status)
            }

          }
      })
    }
  }
}
</script>

<style scoped>

</style>
