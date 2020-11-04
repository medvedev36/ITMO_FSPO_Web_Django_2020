<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Мастера">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="masters">
        <template slot-scope="scope">
          <td>{{scope.row.full_name_m}}</td>
          <td class="is-center">{{scope.row.phone_number}}</td>
          <td class="is-center">{{scope.row.shop_number.shop_name}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    export default {
      name: "Masters",
      components: {Home},
      data(){
        return{
          masters:'',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'ФИО', width: 360, name: 'full_name_m', sortable: true },
              { title: 'Телефон', name: 'phone_numbe', width: 300, align: 'center'},
              { title: 'Автомастерская', width: 463, name: 'shop_name', align: 'center'},
          ],
        };
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadmasters()
      },
      methods:{
        loadmasters(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/masters/",
            type:"GET",
            success: (response) => {
              this.masters = response.data.data
            }
          })
        },
        goBack(){
          this.$router.push({name:"home"})
        },
        handleSortChange ({name, order}) {
          this.masters = this.masters.sort( (a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
          this.masters = this.masters.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
        }
      }
    }
</script>

<style scoped>

</style>
