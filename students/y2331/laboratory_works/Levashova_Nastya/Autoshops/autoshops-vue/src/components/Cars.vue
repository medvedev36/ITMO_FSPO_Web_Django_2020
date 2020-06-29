<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Автомобили">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
      <mu-button flat slot="right" @click="goAdd">Добавить</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="cars">
        <template slot-scope="scope">
          <td>{{scope.row.state_number}}</td>
          <td class="is-center">{{scope.row.year_of_issue}}</td>
          <td class="is-center">{{scope.row.date_sheet_number}}</td>
          <td class="is-center">{{scope.row.model_id.model_name}}</td>
          <td class="is-center">{{scope.row.costumer_id.full_name_c}}</td>
          <td class="is-center">{{scope.row.costumer_id.passport}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import AddCar from "./AddCar";

    export default {
      name: "Cars",
      components: {Home, AddCar},
      data(){
        return{
          cars:'',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Госномер', width: 120, name: 'state_number', sortable: true},
              { title: 'Год выпуска', name: 'year_of_issue', width: 120, align: 'center', sortable: true},
              { title: 'Номер техпаспорта', name: 'date_sheet_number', width: 120, align: 'center'},
              { title: 'Марка', name: 'model_name', width: 200, align: 'center'},
              { title: 'ФИО владельца', name: 'full_name_c', width: 330, align: 'center'},
              { title: 'Серия и номер паспорта владельца', name: 'passport', width: 230, align: 'center'},
          ],
        };
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadcars()
      },
      methods:{
        loadcars(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/cars/",
            type:"GET",
            success: (response) => {
              this.cars = response.data.data
            }
          })
        },
        goBack(){
          this.$router.push({name:"home"})
        },
        goAdd(){
          this.$router.push({name:"addcar"})
        },
        handleSortChange ({name, order}) {
          this.cars = this.cars.sort( (a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
          this.cars = this.cars.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
        }
      }
    }
</script>

<style scoped>

</style>
