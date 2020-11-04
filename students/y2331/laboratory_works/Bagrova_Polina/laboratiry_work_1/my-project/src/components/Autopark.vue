<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      Грузоперевозки
      <mu-button flat v-if="!auth" slot="right" @click="goLogin">Вход</mu-button>
      <mu-button flat v-else slot="right" @click="logout">Выход</mu-button>
    </mu-appbar>

    <mu-list textline="two-line">
      <mu-list-item avatar :ripple="false" button @click="goDrivers">
        <mu-list-item-content>
          <mu-list-item-title>Водители</mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">Посмотреть список водителей</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-divider></mu-divider>

      <mu-list-item avatar :ripple="false" button @click="goCars">
        <mu-list-item-content>
          <mu-list-item-title>Автомобили</mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">Посмотреть список атвомобилй
          </mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-divider></mu-divider>

      <mu-list-item v-if="auth" avatar :ripple="false" button @click="goClients">
        <mu-list-item-content>
          <mu-list-item-title>Клиенты</mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">Информация о клиентах</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-divider></mu-divider>

      <mu-list-item v-if="auth" avatar :ripple="false" button @click="goManifests">
        <mu-list-item-content>
          <mu-list-item-title>Путевые листы</mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">Информация о путевых листах</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
      <mu-divider></mu-divider>

      <mu-list-item v-if="auth" avatar :ripple="false" button @click="goOrders">
        <mu-list-item-content>
          <mu-list-item-title>Заказы</mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">Информация о заказах</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
  </mu-container>
</template>

<script>
    export default {
        name: "Autopark",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
             goDrivers() {
                this.$router.push({name: "Drivers"})
            },
            goCars() {
                this.$router.push({name: "Cars"})
            },
            goClients() {
                this.$router.push({name: "Clients"})
            },
            goManifests() {
                this.$router.push({name: "Manifests"})
            },
            goOrders() {
                this.$router.push({name: "Orders"})
            },
        },
    }
</script>

<style scoped>

</style>
