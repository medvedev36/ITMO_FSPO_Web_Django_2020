<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Работы">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
      <mu-button flat slot="right" @click="goAdd">Добавить</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="works">
        <template slot="expand" slot-scope="prop">
          <mu-flex justify-content="start">
            <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="200" v-if="flag">
              <mu-form-item prop="select" label="Вид ремонта">
                  <mu-select v-model="form.type_of_repair">
                    <mu-option v-for="option, index in options" :key="option" :label="option" :value="option"></mu-option>
                  </mu-select>
              </mu-form-item>
              <mu-form-item prop="input" label="Дата окончания ремонта">
                <mu-text-field v-model="form.repair_completion_date"></mu-text-field>
              </mu-form-item>
              <mu-form-item prop="input" label="Стоимость">
                <mu-text-field v-model="form.repair_cost"></mu-text-field>
              </mu-form-item>
              <mu-form-item prop="select" label="Автомастерская" >
                <mu-select v-model="form.shop_number">
                  <mu-option v-for="s in shops" :key="s.id" :label="s.shop_name" :value="s.id"></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="Госномер авто" >
                <mu-select v-model="form.state_number">
                  <mu-option v-for="c in cars" :key="c.state_number" :label="c.state_number+' ('+c.model_id.model_name+')'" :value="c.state_number"></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="Мастер" >
                <mu-select v-model="form.master_id">
                  <mu-option v-for="m in masters" :key="m.id" :label="m.full_name_m+' ('+m.shop_number.shop_name+')'" :value="m.id"></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="Комплексный ремонт" >
                <mu-select v-model="form.comrepair_id">
                  <mu-option v-for="c in comworks" :key="c.id" :label="c.id+' ('+c.state_number_r+')'" :value="c.id"></mu-option>
                </mu-select>
              </mu-form-item>

            </mu-form>
            <mu-button flat slot="right" color=secondary @click="updateWork" v-if="flag">Редактировать</mu-button>
            <mu-button flat slot="right" @click="saveID(prop.row.id,prop.row.type_of_repair,prop.row.repair_completion_date,
            prop.row.repair_cost,prop.row.shop_number_w.id,prop.row.state_number_w,prop.row.master_id.id,prop.row.comrepair_id)" color=secondary v-else>Редактировать</mu-button>
          </mu-flex>
        </template>
        <template slot-scope="scope">
          <td @click="goFlag"> {{scope.row.type_of_repair}}</td>
          <td class="is-center" @click="goFlag">{{scope.row.receipt_date}}</td>
          <td class="is-center" v-if="scope.row.repair_completion_date" @click="goFlag">{{scope.row.repair_completion_date}}</td>
          <td class="is-center" v-else @click="goFlag">ведется</td>
          <td class="is-center" @click="goFlag">{{scope.row.repair_cost}}</td>
          <td class="is-center" @click="goFlag">{{scope.row.shop_number_w.shop_name}}</td>
          <td class="is-center" @click="goFlag">{{scope.row.state_number_w}}</td>
          <td class="is-center" @click="goFlag">{{scope.row.master_id.full_name_m}}</td>
          <td class="is-center" v-if="scope.row.comrepair_id" @click="goFlag">{{scope.row.comrepair_id.id}}</td>
          <td class="is-center" v-else @click="goFlag">-</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import AddWork from "./AddWork";

    export default {
      name: "Works",
      components: {Home, AddWork},
      data(){
        return{
          active: 0,
          works:'', shops:'', masters:'',cars:'',comworks:'',
          id:'',
          flag: 0,
          options: [
            'Замена отдельных элементов кузова', 'Подбор краски и покраска', 'Замена ремней', 'Регулировка клапанов',
            'Замена маслосъёмных колпачков', 'Замена ведущих и ведомых шестерен', 'Замена масел', 'Замена фильтров'
          ],
          form: {
            type_of_repair: '',
            repair_completion_date: '',
            repair_cost: '',
            shop_number: '',
            state_number: '',
            master_id: '',
            comrepair_id: ''
          },
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Вид ремонта', width: 300, name: 'type_of_repair', sortable: true},
              { title: 'Дата начала ремонта', name: 'receipt_date', width: 230, align: 'center'},
              { title: 'Дата завершения ремонта', name: 'repair_completion_date', width: 200, align: 'center'},
              { title: 'Стоимость ремонта (руб.)', name: 'repair_cost', width: 210, align: 'center', sortable: true},
              { title: 'Автомастрерская', name: 'shop_name', width: 220, align: 'center'},
              { title: 'Госномер авто', name: 'state_number_w', width: 120, align: 'center'},
              { title: 'ФИО мастера', name: 'full_name_m', width: 300, align: 'center'},
              { title: 'Номер комплексного ремонта', name: 'comrepair_id', width: 200, align: 'center'},
          ],
        };
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadworks()
        this.loadshops()
        this.loadmasters()
        this.loadcars()
        this.loadcomworks()
      },
      methods:{
        loadworks(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/works/",
            type:"GET",
            success: (response) => {
              this.works = response.data.data
            }
          })
        },
        loadshops(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/shops/",
            type:"GET",
            success: (response) => {
              this.shops = response.data.data
            }
          })
        },
        loadmasters(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/masters/",
            type:"GET",
            success: (response) => {
              this.masters = response.data.data
            }
          })
        },
        loadcars(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/cars/",
            type:"GET",
            success: (response) => {
              this.cars = response.data.data
            }
          })
        },
        loadcomworks(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/comworks/",
            type:"GET",
            success: (response) => {
              this.comworks = response.data.data
            }
          })
        },
        goBack(){
          this.$router.push({name:"home"})
        },
        goAdd(){
          this.$router.push({name:"addwork"})
        },
        updateWork(){
           $.ajax({
            url:'http://127.0.0.1:8000/autoshops/work/' + this.id,
            type:"PUT",
            data: {
              pk: this.id,
              type_of_repair: this.form.type_of_repair,
              repair_completion_date:this.form.repair_completion_date,
              repair_cost:this.form.repair_cost,
              shop_number_w:this.form.shop_number,
              state_number_w:this.form.state_number,
              master_id:this.form.master_id,
              comrepair_id:this.form.comrepair_id
            },
            success:(response) => {
              alert("Данные успешно изменены!")
              this.loadworks()
              this.flag=0
            },
             error:(response) => {
              alert("Не удалось изменить данные!")
             }
          })
        },
        saveID(ID, type_of_repair, repair_completion_date, repair_cost, shop_number, state_number, master_id, comrepair_id){
          this.flag=1
          this.id = ID
          this.form.type_of_repair = type_of_repair
          this.form.repair_completion_date = repair_completion_date
          this.form.repair_cost = repair_cost
          this.form.shop_number = shop_number
          this.form.state_number = state_number
          this.form.master_id = master_id
          this.form.comrepair_id = comrepair_id.id
        },
        goFlag(){
          this.flag=0
        },
        handleSortChange ({name, order}) {
          this.works = this.works.sort( (a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
          if (name === 'type_of_repair' || name === 'shop_name' || name === 'comrepair_id')
            this.works = this.works.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
        },
      }
    }
</script>

<style scoped>
.mu-demo-form {
    margin-left: 15px;
    width: 100%;
    max-width: 700px;
  }
</style>
