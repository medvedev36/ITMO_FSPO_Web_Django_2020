<template>
  <b-container>
<!--    Хлебные крошки    -->
    <b-breadcrumb class="mt-4" exact active-class="active">
      <b-breadcrumb-item to="/">Магазин</b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel">Админ панель</b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel/users" v-if="isActive('/adminpanel/users')">
        Пользователи
      </b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel/fabrics" v-if="isActive('/adminpanel/fabrics')">
        Производители
      </b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel/products" v-if="isActive('/adminpanel/products')">
        Товары
      </b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel/deliveries" v-if="isActive('/adminpanel/deliveries')">
        Поставки
      </b-breadcrumb-item>
      <b-breadcrumb-item to="/adminpanel/sales" v-if="isActive('/adminpanel/sales')">
        Продажи
      </b-breadcrumb-item>
    </b-breadcrumb>
    <div>
<!--  Представление для текущего пути  -->
      <router-view></router-view>
    </div>
  </b-container>
</template>

<script>
  export default {
    name: "Admin",
    data() {
      return {

      };
    },
    methods: {
      /**
       * Определение, является ли путь текущим
       * @param path Путь
       * @returns {boolean} Является/не является
       */
      isActive(path) {
        return this.$route.fullPath === path;
      }
    },
  }
</script>

<style scoped>

</style>
