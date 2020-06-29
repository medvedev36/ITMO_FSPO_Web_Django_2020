<template>
  <div>
<!--    Навигационная панель   -->
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/">Ювелирный магазин</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <!--      Основные кнопки профиля    -->
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-nav-item to="/login" v-if="!$root.loggedIn">Войти</b-nav-item>
            <b-nav-item to="/register" v-if="!$root.loggedIn">Зарегистрироваться</b-nav-item>
            <b-nav-item to="/user" v-if="$root.loggedIn">Профиль</b-nav-item>
            <b-nav-item to="/adminpanel" v-if="$root.isAdmin">Админка</b-nav-item>
            <b-nav-item @click="logout" v-if="$root.loggedIn">Выйти</b-nav-item>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
<!--    Представление для текущего пути    -->
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {}
    },
    /**
     * Проверка наличия токена и его валидности
     */
    created() {
      if (window.localStorage.getItem('token')) {
        const token = window.localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
        axios.get('/user/').then(response => {
          this.$root.user = response.data;
          this.$root.loggedIn = true;
          this.$root.isAdmin = response.data.is_superuser;
        }).catch(() => {
          this.logout()
        })
      }
    },
    methods: {
      /**
       * Выход, удаление токена
       */
      logout() {
        window.localStorage.removeItem('token');
        axios.defaults.headers.common['Authorization'] = '';
        this.$root.loggedIn = false;
        this.$root.isAdmin = false;
        this.$router.push('/');
      }
    }
  }
</script>

<style lang="scss">

</style>
