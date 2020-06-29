<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Клиенты автомастерских">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
      <mu-button flat slot="right" @click="goAdd">Добавить</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="custumers">
        <template slot-scope="scope">
          <td>{{scope.row.full_name_c}}</td>
          <td class="is-center">{{scope.row.address_c}}</td>
          <td class="is-center">{{scope.row.phone_number_c}}</td>
          <td class="is-center">{{scope.row.passport}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import AddCustumer from "./AddCustumer";

    export default {
      name: "Custumers",
      components: {Home, AddCustumer},
      data(){
        return{
          custumers:'',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'ФИО', name: 'full_name_с', width: 340, sortable: true},
              { title: 'Адрес', name: 'address_c', width: 410, align: 'center', sortable: true},
              { title: 'Телефон', name: 'phone_number_c', width: 160, align: 'center'},
              { title: 'Серия и номер паспорта', name: 'passport', width: 210, align: 'center'},
          ],
        };
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadcustumers()
      },
      methods:{
        loadcustumers(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/custumers/",
            type:"GET",
            success: (response) => {
              this.custumers = response.data.data
            }
          })
        },
        goBack(){
          this.$router.push({name:"home"})
        },
        goAdd(){
          this.$router.push({name:"addcustumer"})
        },
        handleSortChange ({name, order}) {
          this.custumers = this.custumers.sort( (a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
          if (name === 'full_name_с' || name === 'address_c' || name === 'phone_number_c')
            this.custumers = this.custumers.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
        },
      }
    }
</script>

<style scoped>

</style>
