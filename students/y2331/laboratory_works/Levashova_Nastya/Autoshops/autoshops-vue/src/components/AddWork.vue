<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Добавление работы">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
    </mu-appbar>
    <mu-tabs :value.sync="active" color="#80cbc4">
      <mu-tab>Отдельная работа</mu-tab>
      <mu-tab>Комплексный ремонт</mu-tab>
    </mu-tabs>
      <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="200" v-if="active === 0">
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
      <mu-button color="primary" @click="addW" v-if="active === 0">Добавить</mu-button>
      <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="200" v-if="active === 1">
        <mu-form-item prop="select" label="Госномер авто" >
          <mu-select v-model="form.state_number">
            <mu-option v-for="c in cars" :key="c.state_number" :label="c.state_number+' ('+c.model_id.model_name+')'" :value="c.state_number"></mu-option>
          </mu-select>
        </mu-form-item>
      </mu-form>
      <mu-button color="primary" @click="addCW" v-if="active === 1">Добавить</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Work from "./Works";

    export default {
      name: "AddWork",
      components: {Work},
      data () {
        return {
          active: 0,
          options: [
            'Замена отдельных элементов кузова', 'Подбор краски и покраска', 'Замена ремней', 'Регулировка клапанов',
            'Замена маслосъёмных колпачков', 'Замена ведущих и ведомых шестерен', 'Замена масел', 'Замена фильтров'
          ],
          works:'', shops:'', masters:'',cars:'',comworks:'',
          form: {
            type_of_repair: '',
            repair_completion_date: '',
            repair_cost: '',
            shop_number: '',
            state_number: '',
            master_id: '',
            comrepair_id: ''
          }
        }
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadworks()
        this.loadmasters()
        this.loadcars()
        this.loadcomworks()
      },
      methods:{
        loadworks(){
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
        addW(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/works/",
            type:"POST",
            data: {
              type_of_repair: this.form.type_of_repair,
              repair_completion_date:this.form.repair_completion_date,
              repair_cost:this.form.repair_cost,
              shop_number_w:this.form.shop_number,
              state_number_w:this.form.state_number,
              master_id:this.form.master_id,
              comrepair_id:this.form.comrepair_id
            },
            success:(response) => {
              alert("Данные успешно добавлены!")
            },
          })
        },
        addCW(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/comworks/",
            type:"POST",
            data: {
              state_number_r:this.form.state_number
            },
            success:(response) => {
              alert("Идентификатор комплексного ремонта: "+response.data.status.id)
              this.loadcomworks()
            },
          })
        },
        goBack(){
          this.$router.push({name:"works"})
        },
      }
    }
</script>

<style>
  .mu-demo-form {
    margin-top: 50px;
    width: 100%;
    max-width: 620px;
  }
</style>
