<!--Интерфейс для добавления тв передачи-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="Добавление ТВ программы">
      <mu-button flat slot="left" @click="back">back</mu-button>
    </mu-appbar>
    <mu-form :model="form" class="mu-demo-form" label-width="250">
      <mu-form-item class="mu-demo-form1" prop="input" label="Название">
        <mu-text-field v-model="form.show_name"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="input" label="Время выхода в эфир">
        <mu-text-field v-model="form.time"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="input" label="Стоимость показа за минуту (руб.)">
        <mu-text-field v-model="form.cost"></mu-text-field>
      </mu-form-item>
      <mu-form-item class="mu-demo-form1" prop="select" label="Канал" >
        <mu-select v-model="form.idChannel">
          <mu-option v-for="с in channel" :key="с.id" :label="с.channel_name" :value="с.id"></mu-option>
        </mu-select>
      </mu-form-item>
    </mu-form>
    <mu-button color="secondary" @click="addshow">add</mu-button>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Shows from "./Shows";

    export default {
      name: "AddShow",
      components: {Shows},
      data () {
        return {
          shows:'',
          channel:'',
          form: {
            time: '',
            cost: '',
            show_name: '',
            idChannel: '',
          }
        }
      },
      created() {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.channels()
      },
      methods:{
        channels(){
          $.ajax({
            url:"http://127.0.0.1:8000/channels/",
            type:"GET",
            success: (response) => {
              this.channel = response.data.data
            }
          })
        },
        addshow(){
          $.ajax({
            url:"http://127.0.0.1:8000/addshow/",
            type:"POST",
            data: {
              time:this.form.time,
              cost:this.form.cost,
              show_name:this.form.show_name,
              idChannel:this.form.idChannel,
            },
            success:(response) => {
              alert("Успешное добавление!")
            },
          })
        },
        back(){
          this.$router.push({name:"shows"})
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
