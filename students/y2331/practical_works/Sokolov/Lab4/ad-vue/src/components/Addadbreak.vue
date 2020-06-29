<!--Интерфейс для добавления рекламного показа-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="Добавление рекламного показа">
      <mu-button flat slot="left" @click="back">back</mu-button>
    </mu-appbar>
    <mu-form :model="form" class="mu-demo-form" label-width="140">
      <mu-form-item class="mu-demo-form1" prop="input" label="Дата и время показа">
        <mu-text-field v-model="form.date"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="select" label="ТВ программа" >
        <mu-select v-model="form.idTVShow">
          <mu-option v-for="s in show" :key="s.id" :label="s.show_name" :value="s.id"></mu-option>
        </mu-select>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="select" label="Рекламный ролик" >
        <mu-select v-model="form.idAdvertising">
          <mu-option v-for="a in advertising" :key="a.id" :label="a.adName" :value="a.id"></mu-option>
        </mu-select>
      </mu-form-item>
    </mu-form>
    <mu-button color="secondary" @click="addbreak">add</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import AdBreak from "./AdBreak";

    export default {
      name: "Addadbreak",
      components: {AdBreak},
      data () {
        return {
          break:'',
          show:'',
          advertising:'',
          form: {
            date: '',
            idTVShow: '',
            idAdvertising: '',
          }
        }
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.advertisings()
        this.shows()
      },
      methods:{
        advertisings(){
          $.ajax({
            url:"http://127.0.0.1:8000/advertisings/",
            type:"GET",
            success: (response) => {
              this.advertising = response.data.data
            }
          })
        },
        shows(){
          $.ajax({
            url:"http://127.0.0.1:8000/shows/",
            type:"GET",
            success: (response) => {
              this.show = response.data.data
            }
          })
        },
        addbreak(){
          $.ajax({
            url:"http://127.0.0.1:8000/addbreak/",
            type:"POST",
            data: {
              date:this.form.date,
              idTVShow:this.form.idTVShow,
              idAdvertising:this.form.idAdvertising,
            },
            success:(response) => {
              alert("Успешное добавление!")
            },
          })
        },
        back(){
          this.$router.push({name:"adbreak"})
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
