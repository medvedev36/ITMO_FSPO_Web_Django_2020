<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Добавление автомобиля">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
    </mu-appbar>
    <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="200">
      <mu-form-item prop="input" label="Госномер">
        <mu-text-field v-model="form.state_number"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="input" label="Год выпуска">
        <mu-text-field v-model="form.year_of_issue"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="input" label="Номер техпаспорта">
        <mu-text-field v-model="form.date_sheet_number"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="select" label="Марка" >
        <mu-select v-model="form.model">
          <mu-option v-for="m in models" :key="m.id" :label="m.model_name" :value="m.id"></mu-option>
        </mu-select>
      </mu-form-item>
      <mu-form-item prop="select" label="Владелец" >
        <mu-select v-model="form.custumer">
          <mu-option v-for="c in custumers" :key="c.id" :label="c.full_name_c+' ('+c.passport+')'" :value="c.id"></mu-option>
        </mu-select>
      </mu-form-item>
    </mu-form>
    <mu-button color="primary" @click="addC">Добавить</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Car from "./Cars";

    export default {
      name: "AddCar",
      components: {Car},
      data () {
        return {
          cars:'', custumers:'', models:'',
          form: {
            state_number: '',
            year_of_issue: '',
            date_sheet_number: '',
            model: '',
            custumer: '',
          }
        }
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadcustumers()
        this.loadmodels()
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
        loadmodels(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/models/",
            type:"GET",
            success: (response) => {
              this.models = response.data.data
            }
          })
        },
        addC(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/cars/",
            type:"POST",
            data: {
              state_number:this.form.state_number,
              year_of_issue:this.form.year_of_issue,
              date_sheet_number:this.form.date_sheet_number,
              model_id:this.form.model,
              costumer_id:this.form.custumer
            },
            success:(response) => {
              alert("Данные успешно добавлены!")
            },
          })
        },
        goBack(){
          this.$router.push({name:"cars"})
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
