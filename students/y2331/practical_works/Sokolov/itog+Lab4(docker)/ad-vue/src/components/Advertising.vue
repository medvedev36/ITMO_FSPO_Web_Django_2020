<!--Интерфейс с информацией о всех рекламных роликах-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="Рекламные ролики">
     <mu-button flat slot="left" @click="back">back</mu-button>
      <mu-button flat slot="right" v-if="auth" @click="addad">add</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="advertising">
        <template slot="expand" slot-scope="prop">
          <mu-button flat slot="right" v-if="auth" color=primary @click="save(prop.row.id,prop.row.adName,prop.row.time,prop.row.idAdvertiser)">Редактировать</mu-button>
        </template>
        <template slot-scope="scope">
          <td>{{scope.row.adName}}</td>
          <td class="is-center">{{scope.row.time}}</td>
          <td class="is-center">{{scope.row.idAdvertiser.advertiser_name}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
    <mu-dialog title="Редактирование" width="360" :open.sync="openSimple">
      <mu-form :model="form" label-width="200">
        <mu-form-item prop="input" label="Название">
          <mu-text-field v-model="form.adName"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input" label="Продолжительность (сек.)">
          <mu-text-field v-model="form.time"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="select" label="Рекламная компания" >
          <mu-select v-model="form.idAdvertiser">
            <mu-option v-for="a in advertiser" :key="a.id" :label="a.advertiser_name" :value="a.id"></mu-option>
          </mu-select>
        </mu-form-item>
      </mu-form>
      <mu-button slot="actions" flat color="secondary" v-if="auth" @click="update">update</mu-button>
    </mu-dialog>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import AddAdvertising from "./AddAdvertising";

    export default {
      name: "Advertising",
      components: {Home, AddAdvertising},
      computed:{
        auth(){
          if(sessionStorage.getItem("auth_token")){
            return true
          }
        }
      },
      data(){
        return{
          openSimple: false,
          id:'',
          advertiser: '',
          advertising:'',
          form: {
            adName: '',
            time: '',
            idAdvertiser: '',
          },
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Название', name: 'adName', width: 410, sortable: true },
              { title: 'Продолжительность (сек.)', name: 'time', width: 272, align: 'center', sortable: true },
              { title: 'Рекламная компания', name: 'advertiser_name', width: 440, align: 'center', sortable: true },
          ],
        };
      },
      created() {
        this.loadad()
        this.advertisers()
      },
      methods:{
        advertisers(){
          $.ajax({
            url:"http://127.0.0.1:8000/advertiser/",
            type:"GET",
            success: (response) => {
              this.advertiser = response.data.data
            }
          })
        },
        loadad(){
          $.ajax({
            url:"http://127.0.0.1:8000/advertisings/",
            type:"GET",
            success: (response) => {
              this.advertising = response.data.data
            }
          })
        },
        addad(){
          this.$router.push({name:"addadver"})
        },
        update(){
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
           $.ajax({
            url:'http://127.0.0.1:8000/advertising/' + this.id,
            type:"PUT",
            data: {
              pk: this.id,
              adName: this.form.adName,
              time:this.form.time,
              idAdvertiser:this.form.idAdvertiser,
            },
            success:(response) => {
              alert("Данные успешно изменены!")
              this.openSimple = false;
              this.loadad()
            },
             error:(response) => {
              alert("Не удалось изменить данные!")
             }
          })
        },
        back(){
          this.$router.push({name:"home"})
        },
        save(id, adName, time, idAdvertiser){
          this.id = id
          this.form.adName = adName
          this.form.time = time
          this.form.idAdvertiser = idAdvertiser.id
          this.openSimple = true
          this.loadad()
        },
        handleSortChange ({name, order}) {
          if (name === "adName" || name === "advertiser_name") {
            if (name === "advertiser_name"){
              this.advertising = this.advertising.sort( (a, b) => order === 'asc' ? a.idAdvertiser[name].localeCompare(b.idAdvertiser[name]) : b.idAdvertiser[name].localeCompare(a.idAdvertiser[name]));
            }
            if (name === "adName"){
              this.advertising = this.advertising.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
            }
          }
          else{
            this.advertising = this.advertising.sort((a, b) => order === 'asc' ? b[name] - a[name] : a[name] - b[name]);
          }
        }
      }
    }
</script>

<style scoped>

</style>
