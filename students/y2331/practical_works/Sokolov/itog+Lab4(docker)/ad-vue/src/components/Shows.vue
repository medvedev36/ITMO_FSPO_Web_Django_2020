<!--Интерфейс с информацией о всех тв передачах-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="ТВ программы">
     <mu-button flat slot="left" @click="back">back</mu-button>
      <mu-button flat slot="right" v-if="auth" @click="addshow">add</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="shows">
        <template slot-scope="scope">
          <td>{{scope.row.show_name}}</td>
          <td class="is-center">{{scope.row.time}}</td>
          <td class="is-center">{{scope.row.cost}}</td>
          <td class="is-center">{{scope.row.idChannel.channel_name}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import AddShow from "./AddShow";

    export default {
      name: "Shows",
      components: {Home, AddShow},
      computed:{
        auth(){
          if(sessionStorage.getItem("auth_token")){
            return true
          }
        }
      },
      data(){
        return{
          shows:'',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Название', name: 'show_name', width: 310, sortable: true },
              { title: 'Время выхода в эфир', name: 'time', width: 240, align: 'center'},
              { title: 'Стоимость показа за минуту (руб.)', name: 'cost', width: 240, align: 'center', sortable: true },
              { title: 'Канал', name: 'channel_name', width: 333, align: 'center', sortable: true },
          ],
        };
      },
      created() {
        this.loadshows()
      },
      methods:{
        loadshows(){
          $.ajax({
            url:"http://127.0.0.1:8000/shows/",
            type:"GET",
            success: (response) => {
              this.shows = response.data.data
            }
          })
        },
        addshow(){
          this.$router.push({name:"addshow"})
        },
        back(){
          this.$router.push({name:"home"})
        },
        handleSortChange({name, order}) {
          if (name === "channel_name" || name === "show_name") {
            if (name === "channel_name"){
              this.shows = this.shows.sort( (a, b) => order === 'asc' ? a.idChannel[name].localeCompare(b.idChannel[name]) : b.idChannel[name].localeCompare(a.idChannel[name]));
            }
            if (name === "show_name"){
              this.shows = this.shows.sort( (a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
            }
          }
          else{
            this.shows = this.shows.sort((a, b) => order === 'asc' ? b[name] - a[name] : a[name] - b[name]);
          }
        },
      }
    }
</script>

<style scoped>

</style>
