<template>
  <mu-container>
    <mu-appbar color="#4db6ac" style="width: 100%;" title="Добавление клиента">
      <mu-button flat slot="left" @click="goBack">Назад</mu-button>
    </mu-appbar>
    <mu-form :model="form" class="mu-demo-form" label-position="left" label-width="200">
      <mu-form-item prop="input" label="ФИО">
        <mu-text-field v-model="form.name"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="input" label="Адрес">
        <mu-text-field v-model="form.address"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="input" label="Телефон">
        <mu-text-field v-model="form.phone"></mu-text-field>
      </mu-form-item>
      <mu-form-item prop="input" label="Серия и номер паспорта">
        <mu-text-field v-model="form.passport"></mu-text-field>
      </mu-form-item>
    </mu-form>
    <mu-button color="primary" @click="addC">Добавить</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Custumers from "./Custumers";

    export default {
      name: "AddCustumers",
      components: {Custumers},
      data () {
        return {
          custumers:'',
          form: {
            name: '',
            address: '',
            phone: '',
            passport: '',
          }
        }
      },
      methods:{
        addC(){
          $.ajax({
            url:"http://127.0.0.1:8000/autoshops/custumers/",
            type:"POST",
            data: {
              full_name_c: this.form.name,
              address_c:this.form.address,
              phone_number_c:this.form.phone,
              passport:this.form.passport
            },
            success:(response) => {
              alert("Данные успешно добавлены!")
            },
          })
        },
        goBack(){
          this.$router.push({name:"custumer"})
        },
      }
    }
</script>

<style>
  .mu-demo-form {
    margin-top: 50px;
    width: 100%;
    max-width: 640px;
  }
</style>
