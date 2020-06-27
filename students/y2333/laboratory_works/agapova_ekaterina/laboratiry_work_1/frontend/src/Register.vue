<template>
  <b-container>
    <b-row class="mt-3 justify-content-md-center">
      <b-col sm="12" md="6">
<!--        Форма для регистрации-->
        <b-card title="Регистрация">
          <b-form @submit.prevent="register">
            <b-form-group
              label="Имя пользователя:"
            >
              <b-form-input
                required
                placeholder="username"
                v-model="username"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Почта:"
            >
              <b-form-input
                required
                placeholder="email"
                v-model="email"
                type="email"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Номер карты:"
            >
              <b-form-input
                required
                placeholder="card"
                v-model="card"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Имя:"
            >
              <b-form-input
                required
                placeholder="Имя"
                v-model="first_name"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Фамилия:"
            >
              <b-form-input
                required
                placeholder="Фамилия"
                v-model="last_name"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Дата рождения:"
            >
              <b-form-input
                v-model="date_of_birth"
                type="text"
                placeholder="YYYY-MM-DD"
                autocomplete="off"
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

            <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "Register",
    data() {
      return {
        //Данные о регистрируемом пользователе
        username: '',
        password: '',
        email: '',
        date_of_birth: '',
        card: '',
        first_name: '',
        last_name: '',
      };
    },
    methods: {
      /**
       * Регистрация пользователя
       */
      register() {
        let bodyFormData = new FormData();
        bodyFormData.set('username', this.username);
        bodyFormData.set('password', this.password);
        bodyFormData.set('email', this.email);
        bodyFormData.set('date_of_birth', this.date_of_birth);
        bodyFormData.set('card', this.card);
        bodyFormData.set('first_name', this.first_name);
        bodyFormData.set('last_name', this.last_name);
        //Отправка запроса не регистрацию
        axios({
          method: 'post',
          url: '/user/register/',
          data: bodyFormData,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then(response => {
          //Переадресация на страницу входа в случае успеха
          this.$router.push('/login');
        }).catch(() => {
          alert('Что-то заполнено неверно, попробуйте еще раз!')
        });
      },
    }
  }
</script>

<style scoped>

</style>
