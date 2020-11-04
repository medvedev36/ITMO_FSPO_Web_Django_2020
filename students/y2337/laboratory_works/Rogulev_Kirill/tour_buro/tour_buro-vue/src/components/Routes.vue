<template>
  <mu-flex justify-content="center" style="padding: 25px">

    <div style="font-size: 50px">Routes</div>
    <mu-container>

        <mu-flex justify-content="end" class="button-wrapper">

              <mu-button v-show="!selects.length" fab color="blue" @click="editMenu(true)">
                <mu-icon v-model="icons.editmenu_button_icon" ></mu-icon>
              </mu-button>
               <mu-button v-show="selects.length == 1" fab color="blue" @click="editMenu(false)">
                <mu-icon value="edit"></mu-icon>
               </mu-button>
               <mu-button v-show="selects.length" fab color="red" @click="deleteSelected">
                <mu-icon value="delete_forever"></mu-icon>
              </mu-button>
               <mu-button fab color="teal" @click="saveBuses">
                <mu-icon value="save"></mu-icon>
              </mu-button>

          </mu-flex>

        <mu-container class="table_db">
          <mu-paper :z-depth="1">
          <mu-data-table border v-show="routes.length" selectable select-all :selects.sync="selects" checkbox :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="routes">
            <template slot-scope="scope">
              <td class="is-center">{{scope.row.id}}</td>
              <td class="is-center">{{scope.row.name}}</td>
              <td class="is-center">{{scope.row.start_location}}</td>
              <td class="is-center">{{scope.row.end_location}}</td>
              <td class="is-center">{{scope.row.length}}</td>
            </template>

          </mu-data-table>
          </mu-paper>
        </mu-container>
    </mu-container>

      <mu-container>
        <mu-flex>
          <mu-expand-transition>
            <mu-container v-show="show.editmenu" class="add_menu">
              <div v-show="newroute.new">New Route</div>
              <div v-show="!newroute.new">Edit Route</div>
              <mu-text-field v-model="newroute.id" placeholder="id"></mu-text-field><br>
              <mu-text-field v-model="newroute.name" placeholder="name"></mu-text-field><br>
              <mu-text-field v-model="newroute.start_location" placeholder="Start location"></mu-text-field><br>
              <mu-text-field v-model="newroute.end_location" placeholder="End location"></mu-text-field><br>
              <mu-text-field v-model="newroute.length" placeholder="Length"></mu-text-field><br>
              <mu-button fab color="blue" @click="addBus">
              <mu-icon value="done"></mu-icon>
            </mu-button>

            </mu-container>
          </mu-expand-transition>
        </mu-flex>
      </mu-container>


    </mu-flex>

</template>

<script>
import $ from "jquery"

export default {
  name: 'Main',
  data() {
    return {
      show: {
        editmenu: false,
      },
      icons: {
        editmenu_button_icon:"add",
      },
      selects: [],
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
          { title: 'id', name: 'id', sortable: true},
          { title: 'Name', name: 'name'},
          { title: 'Start location', name: 'start_location',},
          { title: 'End location', name: 'end_location'},
          { title: 'Length', name: 'length', sortable: true},
        ],

      routes: [],
      newroute: {
        id:null,
        name:null,
        start_location:null,
        end_location:null,
        length:null,
        new:null,
      }

    }
  },
  created() {
    if(sessionStorage.getItem("auth_token")) {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem("auth_token")},
      });
    }
    this.loadBuses()
  },

  methods:{
    editMenu(isNew){

      if(!isNew){
        var nr = this.routes[this.selects[0]];
        this.newroute.id = nr.id;
        this.newroute.name = nr.name;
        this.newroute.start_location = nr.start_location;
        this.newroute.end_location = nr.end_location;
        this.newroute.length = nr.length;
      }else{
        this.newroute.id = null;
        this.newroute.name = null;
        this.newroute.start_location = null;
        this.newroute.end_location = null;
        this.newroute.length = null;
      }
      if (this.show.editmenu) {
          this.icons.addmenu_button_icon = "add";
        } else {
          this.icons.addmenu_button_icon = "clear";
        }
        if(this.newroute.new == isNew || !this.show.editmenu) {
          this.show.editmenu = !this.show.editmenu;
        }
      this.newroute.new = isNew;


    },
    loadBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/excursion_routes/",
          type: "GET",
          success: (response) => {
            this.routes = response.data.data
          }
      })
    },
    saveBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/excursion_routes/",
          type: "POST",
          data: JSON.stringify(this.routes),
        contentType: "application/json",
          success: (response) => {

          }
      })
    },
    addBus(){
      var bb = this.newroute;
      if(bb.id==null) return;
      if(bb.new) {
        var exists = this.buses.some(function (field) {
          return parseInt(field.id) === parseInt(bb.id);
        });
      }
      if(exists){
        alert("Error: id already exists");
      }else {
        if (this.newroute.new) {
          this.routes.push({
            id: this.newroute.id,
            name: this.newroute.name,
            start_location: this.newroute.start_location,
            end_location: this.newroute.end_location,
            length: this.newroute.length,
          })
        } else {
          this.routes[this.selects[0]] = {
            id: this.newroute.id,
            name: this.newroute.name,
            start_location: this.newroute.start_location,
            end_location: this.newroute.end_location,
            length: this.newroute.length,
          }
        }
        this.show.editmenu = false;
        this.newroute.new = false;
        this.selects.splice(0, this.selects.length);
      }
    },
    deleteSelected () {
      for(let i =0;i<this.selects.length;i++) {
        this.selects.forEach(((value,index) => {
          this.routes.splice(value,1);
        }))
      }
      this.selects.splice(0,this.selects.length);
    },
    handleSortChange ({name, order}) {
      this.routes = this.routes.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },

  }
}
</script>

<style>

.button-wrapper {
  margin: 20px;
}
.add_menu{
  margin-top: 20px;
}
.table_db{
  width: 100%;
  max-width: 400px;
  max-height: 400px
}

</style>
