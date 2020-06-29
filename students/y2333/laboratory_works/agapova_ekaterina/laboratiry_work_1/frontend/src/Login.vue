<template>
  <b-container>
    <b-row class="mt-3 justify-content-md-center">
      <b-col sm="12" md="6">
        <b-card title="Вход">
<!--          Форма для входа       -->
          <b-form @submit.prevent="login">
            <b-form-group
              label="Имя пользователя:"
            >
              <b-form-input
                required
                placeholder="username"
                v-model="username"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Пароль:">
              <b-form-input
                required
                v-model="password"
                type="password"
                placeholder="password"
              ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Войти</b-button>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        //логин
        username: '',
        //пароль
        password: '',
      };
    },
    methods: {
      /**
       * Аутентификация пользователя
       */
      login() {
        let bodyFormData = new FormData();
        bodyFormData.set('username', this.username);
        bodyFormData.set('password', this.password);
        //Отправка запроса на получение JWT токена
        axios({
          method: 'post',
          url: '/auth/jwt/create',
          data: bodyFormData,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then(response => {
          //Сохранение токена при успехе
          window.localStorage.setItem('token', response.data.access);
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
          axios.get('/user/').then(response => {
            this.$root.user = response.data;
            this.$root.loggedIn = true;
            this.$root.isAdmin = response.data.is_superuser;
            this.$router.push('/');
          })
        }).catch(() => {
          alert('Неверный логин или пароль!')
        });
      },
    }
  }
</script>

<style scoped>

</style>
