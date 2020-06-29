<template>
<!--  Список всех данных  -->
    <div>
      <b-list-group>
      <b-list-group-item to="/adminpanel/users">Пользователи</b-list-group-item>
      <b-list-group-item to="/adminpanel/fabrics">Производители</b-list-group-item>
      <b-list-group-item to="/adminpanel/products">Товары</b-list-group-item>
      <b-list-group-item to="/adminpanel/deliveries">Поставки</b-list-group-item>
      <b-list-group-item to="/adminpanel/sales">Продажи</b-list-group-item>
    </b-list-group>
    </div>
</template>

<script>
    export default {
        name: "List"
    }
</script>

<style scoped>

</style>
