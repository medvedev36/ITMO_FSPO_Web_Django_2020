<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Автомастерские">
     <mu-button flat slot="left" @click="goBack">Назад</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="shops">
        <template slot-scope="scope">
          <td>{{scope.row.shop_name}}</td>
          <td class="is-center">{{scope.row.address}}</td>
          <td class="is-center">
            <li v-for="m in scope.row.car_models">
              {{m.model_name}}
            </li>
          </td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    export default {
      name: "Room",
      components: {Home},
      data(){
        return{
          shops:'',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Название', name: 'shop_name', width: 340, sortable: true },
              { title: 'Адрес', name: 'address', width: 540, align: 'center'},
              { title: 'Обслуживаемые марки', name: 'car_models', width: 240, align: 'center'},
          ],
        };
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadshops()
      },
      methods:{
        loadshops(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/shops/",
            type:"GET",
            success: (response) => {
              this.shops = response.data.data
            }
          })
        },
        goBack(){
          this.$router.push({name:"home"})
        },
        handleSortChange ({name, order}) {
          this.shops = this.shops.sort( (a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
          this.shops = this.shops.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
        }
      }
    }
</script>

<style scoped>

</style>
