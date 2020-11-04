<template>
  <mu-flex justify-content="center" style="padding: 25px">

    <div style="font-size: 50px">Trips</div>
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
          <mu-data-table border v-show="trips.length" selectable select-all :selects.sync="selects" checkbox :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="trips">
            <template slot-scope="scope">
              <td class="is-center">{{scope.row.id}}</td>
              <td class="is-center">{{scope.row.start_date}}</td>
              <td class="is-center">{{scope.row.end_date}}</td>
              <td class="is-center">{{scope.row.n_passengers}}</td>
              <td class="is-center">{{scope.row.price}}</td>
              <td class="is-center">{{scope.row.bus_id}}</td>
              <td class="is-center">{{scope.row.route_id}}</td>
            </template>

          </mu-data-table>
          </mu-paper>
        </mu-container>
    </mu-container>

      <mu-container>
        <mu-flex>
          <mu-expand-transition>
            <mu-container v-show="show.editmenu" class="add_menu">
              <div v-show="newtrip.new">New Trip</div>
              <div v-show="!newtrip.new">Edit Trip</div>
              <mu-text-field v-model="newtrip.id" placeholder="id"></mu-text-field><br>
              <mu-text-field v-model="newtrip.start_date" placeholder="Start date"></mu-text-field><br>
              <mu-text-field v-model="newtrip.end_date" placeholder="End date"></mu-text-field><br>
              <mu-text-field v-model="newtrip.n_passengers" placeholder="Number of passengers"></mu-text-field><br>
              <mu-text-field v-model="newtrip.price" placeholder="Price"></mu-text-field><br>
              <mu-text-field v-model="newtrip.bus_id" placeholder="Bus id"></mu-text-field><br>
              <mu-text-field v-model="newtrip.route_id" placeholder="Route id"></mu-text-field><br>
              <mu-button fab color="blue" @click="addTrip">
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
          { title: 'Start date', name: 'start_date'},
          { title: 'End date', name: 'end_date',},
          { title: 'Passengers', name: 'n_passengers', sortable: true},
          { title: 'Price', name: 'price', sortable: true},
          { title: 'Bus id', name: 'bus_id', sortable: true},
          { title: 'Route id', name: 'route_id', sortable: true},
        ],

      trips: [],
      newtrip: {
        id:null,
        start_date:null,
        end_date:null,
        n_passengers:null,
        price:null,
        bus_id:null,
        route_id:null,
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
        var nt = this.trips[this.selects[0]];
        this.newtrip.id = nt.id;
        this.newtrip.start_date = nt.start_date;
        this.newtrip.end_date = nt.end_date;
        this.newtrip.n_passengers = nt.n_passengers;
        this.newtrip.price = nt.price;
        this.newtrip.bus_id = nt.bus_id;
        this.newtrip.route_id = nt.route_id;
      }else{
        this.newtrip.id = null;
        this.newtrip.start_date = null;
        this.newtrip.end_date = null;
        this.newtrip.n_passengers = null;
        this.newtrip.price = null;
        this.newtrip.bus_id = null;
        this.newtrip.route_id = null;
      }
      if (this.show.editmenu) {
          this.icons.addmenu_button_icon = "add";
        } else {
          this.icons.addmenu_button_icon = "clear";
        }
        if(this.newtrip.new == isNew || !this.show.editmenu) {
          this.show.editmenu = !this.show.editmenu;
        }
      this.newtrip.new = isNew;


    },
    loadBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/completed_trips/ ",
          type: "GET",
          success: (response) => {
            this.trips = response.data.data
          }
      })
    },
    saveBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/completed_trips/ ",
          type: "POST",
          data: JSON.stringify(this.trips),
        contentType: "application/json",
          success: (response) => {

          }
      })
    },
    addTrip(){
      var bb = this.newtrip;
      if(bb.id==null) return;
      if(bb.new) {
        var exists = this.trips.some(function (field) {
          return parseInt(field.id) === parseInt(bb.id);
        });
      }
      if(exists){
        alert("Error: id already exists");
      }else {
        var bt = this.newtrip;
        if (this.newtrip.new) {
          this.trips.push({
            id: bt.id,
            start_date: bt.start_date,
            end_date: bt.end_date,
            n_passengers: bt.n_passengers,
            price: bt.price,
            bus_id: bt.bus_id,
            route_id: bt.route_id,
          })
        } else {
          this.trips[this.selects[0]] = {
            id: bt.id,
            start_date: bt.start_date,
            end_date: bt.end_date,
            n_passengers: bt.n_passengers,
            price: bt.price,
            bus_id: bt.bus_id,
            route_id: bt.route_id,
          }
        }
        this.show.editmenu = false;
        this.newtrip.new = false;
        this.selects.splice(0, this.selects.length);
      }
    },
    deleteSelected () {
      for(let i =0;i<this.selects.length;i++) {
        this.selects.forEach(((value,index) => {
          this.trips.splice(value,1);
        }))
      }
      this.selects.splice(0,this.selects.length);
    },
    handleSortChange ({name, order}) {
      this.trips = this.trips.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
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
