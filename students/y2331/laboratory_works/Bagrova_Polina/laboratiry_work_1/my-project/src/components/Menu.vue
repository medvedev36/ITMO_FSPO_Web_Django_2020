<template>
  <mu-menu slot="left">
    <mu-button icon flat color="primary">
      <mu-icon value="menu"></mu-icon>
    </mu-button>
    <mu-list slot="content">
      <mu-list-item button @click="goDrivers">
        <mu-list-item-title>Водители</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button @click="goCars">
        <mu-list-item-title>Автомобили</mu-list-item-title>
      </mu-list-item>
      <mu-list-item v-if="auth" button @click="goClients">
        <mu-list-item-title>Клиенты</mu-list-item-title>
      </mu-list-item>
      <mu-list-item v-if="auth" button @click="goManifests">
        <mu-list-item-title>Путевые листы</mu-list-item-title>
      </mu-list-item>
      <mu-list-item v-if="auth" button @click="goOrders">
        <mu-list-item-title>Заказы</mu-list-item-title>
      </mu-list-item>
    </mu-list>
  </mu-menu>
</template>

<script>
    export default {
        name: "Menu",
         computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
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
