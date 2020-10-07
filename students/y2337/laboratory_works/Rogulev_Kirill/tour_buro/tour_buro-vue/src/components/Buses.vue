<template>
  <mu-flex justify-content="center" style="padding: 25px">
    <div style="font-size: 50px">Buses</div>
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
          <mu-data-table border v-show="buses.length" selectable select-all :selects.sync="selects" checkbox :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="buses">
            <template slot-scope="scope">
              <td class="is-center">{{scope.row.id}}</td>
              <td class="is-center">{{scope.row.name}}</td>
              <td class="is-center">{{scope.row.mileage}}</td>
            </template>

          </mu-data-table>
          </mu-paper>
        </mu-container>
    </mu-container>

      <mu-container>
        <mu-flex>
          <mu-expand-transition>
            <mu-container v-show="show.editmenu" class="add_menu">
              <div v-show="newbus.new">New Bus</div>
              <div v-show="!newbus.new">Edit Bus</div>
              <mu-text-field v-model="newbus.id" placeholder="id"></mu-text-field><br>
              <mu-text-field v-model="newbus.name" placeholder="name"></mu-text-field><br>
              <mu-text-field v-model="newbus.mileage" placeholder="mileage"></mu-text-field><br>
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
          { title: 'Name', name: 'name',},
          { title: 'Mileage', name: 'mileage', sortable: true},
        ],

      buses: [],
      newbus: {
        id:null,
        name:null,
        mileage:null,
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
        this.newbus.id = this.buses[this.selects[0]].id;
        this.newbus.name = this.buses[this.selects[0]].name;
        this.newbus.mileage = this.buses[this.selects[0]].mileage;
      }else{
        this.newbus.id = null;
        this.newbus.name = null;
        this.newbus.mileage = null;
      }
      if (this.show.editmenu) {
          this.icons.addmenu_button_icon = "add";
        } else {
          this.icons.addmenu_button_icon = "clear";
        }

        if(this.newbus.new == isNew || !this.show.editmenu) {
          this.show.editmenu = !this.show.editmenu;
        }
          this.newbus.new = isNew;


    },
    loadBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/buses/",
          type: "GET",
          success: (response) => {
            this.buses = response.data.data
          }
      })
    },
    saveBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/buses/",
          type: "POST",
          data: JSON.stringify(this.buses),
        contentType: "application/json",
          success: (response) => {

          }
      })
    },
    addBus(){
      var bb = this.newbus;
      if(bb.id==null) return;
      if(bb.new) {
        var exists = this.buses.some(function (field) {
          return parseInt(field.id) === parseInt(bb.id);
        });
      }
      if(exists){
        alert("Error: id already exists");
      }else {
        if (this.newbus.new) {
          this.buses.push({id: this.newbus.id, name: this.newbus.name, mileage: this.newbus.mileage})
        } else {
          this.buses[this.selects[0]] = {id: this.newbus.id, name: this.newbus.name, mileage: this.newbus.mileage};
        }
        this.show.editmenu = false;
        this.newbus.new = false;
        this.selects.splice(0, this.selects.length);
      }
    },
    deleteSelected () {
      console.log(this.selects);

      for(let i =0;i<this.selects.length;i++) {
        this.selects.forEach(((value,index) => {
          this.buses.splice(value,1);

        }))
      }
      this.selects.splice(0,this.selects.length);
    },
    handleSortChange ({name, order}) {
      this.buses = this.buses.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
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
