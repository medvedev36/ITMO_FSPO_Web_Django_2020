<!--Интерфейс с информацией о всех рекламных показах-->
<template>
  <mu-container>
    <mu-appbar color="secondary" style="width: 100%;" title="Рекламные показы">
     <mu-button flat slot="left" @click="back">back</mu-button>
      <mu-button flat slot="right" v-if="auth" @click="addbreak">add</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1">
      <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="adbreak">
        <template slot-scope="scope">
          <td>{{scope.row.idAdvertising.adName}}</td>
          <td class="is-center">{{scope.row.idAdvertising.time}}</td>
          <td class="is-center" v-if="scope.row.date">{{scope.row.date}}</td>
          <td class="is-center" v-else>не назначено</td>
          <td class="is-center">{{scope.row.idTVShow.show_name}}</td>
          <td class="is-center">{{scope.row.idTVShow.idChannel.channel_name}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from "./Home";
    import Addadbreak from "./Addadbreak";

    export default {
      name: "AdBreak",
      components: {Home, Addadbreak},
      computed:{
        auth(){
          if(sessionStorage.getItem("auth_token")){
            return true
          }
        }
      },
      data(){
        return{
          adbreak:'',
          shows: '',
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
              { title: 'Название ролика', name: 'adName', width: 260, sortable: true},
              { title: 'Продолжительность (сек.)', name: 'time', width: 152, align: 'center', sortable: true},
              { title: 'Дата и время показа', name: 'date', width: 210, align: 'center'},
              { title: 'Программа', name: 'show_name', width: 270, align: 'center', sortable: true},
              { title: 'Канал', name: 'channel_name', width: 230, align: 'center', sortable: true},
          ],
        };
      },
      created() {
        this.loadbreak()
      },
      methods:{
        loadbreak(){
          $.ajax({
            url:"http://127.0.0.1:8000/adBreaks/",
            type:"GET",
            success: (response) => {
              this.adbreak = response.data.data
              this.shows = this.adbreak.idTVShow
            }
          })
        },
        addbreak(){
          this.$router.push({name:"addbreak"})
        },
        back(){
          this.$router.push({name:"home"})
        },
        handleSortChange({name, order}) {
          if (name === "adName" || name === "show_name" || name === "channel_name") {
            if (name === "adName")
              this.adbreak = this.adbreak.sort( (a, b) => order === 'asc' ? a.idAdvertising[name].localeCompare(b.idAdvertising[name]) : b.idAdvertising[name].localeCompare(a.idAdvertising[name]));
            if (name === "show_name")
              this.adbreak = this.adbreak.sort( (a, b) => order === 'asc' ? a.idTVShow[name].localeCompare(b.idTVShow[name]) : b.idTVShow[name].localeCompare(a.idTVShow[name]));
            if (name === "channel_name")
              this.adbreak = this.adbreak.sort( (a, b) => order === 'asc' ? a.idTVShow.idChannel[name].localeCompare(b.idTVShow.idChannel[name]) : b.idTVShow.idChannel[name].localeCompare(a.idTVShow.idChannel[name]));
          }
          else
            this.adbreak = this.adbreak.sort((a, b) => order === 'asc' ? b.idAdvertising[name] - a.idAdvertising[name] : a.idAdvertising[name] - b.idAdvertising[name]);
        },
      }
    }
</script>

<style scoped>

</style>
