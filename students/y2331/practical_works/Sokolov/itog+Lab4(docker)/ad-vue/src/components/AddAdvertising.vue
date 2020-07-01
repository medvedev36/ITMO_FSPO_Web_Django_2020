<!--Интерфейс для добавления нового рекламного ролика-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="Добавление рекламного ролика">
      <mu-button flat slot="left" @click="back">back</mu-button>
    </mu-appbar>
    <mu-form :model="form" class="mu-demo-form" label-width="180">
      <mu-form-item class="mu-demo-form1" prop="input" label="Название">
        <mu-text-field v-model="form.adName"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="input" label="Продолжительность (сек.)">
        <mu-text-field v-model="form.time"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="select" label="Рекламная компания" >
        <mu-select v-model="form.idAdvertiser">
          <mu-option v-for="a in advertiser" :key="a.id" :label="a.advertiser_name" :value="a.id"></mu-option>
        </mu-select>
      </mu-form-item>
    </mu-form>
    <mu-button color="secondary" @click="addad">add</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Advertising from "./Advertising";

    export default {
      name: "AddAdvertising",
      components: {Advertising},
      data () {
        return {
          ad:'',
          advertiser:'',
          form: {
            adName: '',
            time: '',
            idAdvertiser: '',
          }
        }
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
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
        addad(){
          $.ajax({
            url:"http://127.0.0.1:8000/addadver/",
            type:"POST",
            data: {
              adName:this.form.adName,
              time:this.form.time,
              idAdvertiser:this.form.idAdvertiser,
            },
            success:(response) => {
              alert("Успешное добавление!")
            },
          })
        },
        back(){
          this.$router.push({name:"advertising"})
        },
      }
    }
</script>

<style>
  .mu-demo-form {
    margin-top: 60px;
    margin-left: 90px;
    width: 100%;
    max-width: 520px;
  }
  .mu-demo-form1 {
    text-align: left;
  }
</style>
