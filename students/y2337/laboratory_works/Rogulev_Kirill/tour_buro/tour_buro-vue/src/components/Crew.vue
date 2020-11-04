<template>
  <mu-flex justify-content="center" style="padding: 25px">
    <div style="font-size: 50px">Crew members</div>
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
          <mu-data-table border v-show="crew_members.length" selectable select-all :selects.sync="selects" checkbox :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="crew_members">
            <template slot-scope="scope">
              <td class="is-center">{{scope.row.id}}</td>
              <td class="is-center">{{scope.row.second_name}}</td>
              <td class="is-center">{{scope.row.exp}}</td>
              <td class="is-center">{{scope.row.category}}</td>
              <td class="is-center">{{scope.row.adress}}</td>
              <td class="is-center">{{scope.row.birth_year}}</td>
              <td class="is-center">{{scope.row.bus_id}}</td>
            </template>

          </mu-data-table>
          </mu-paper>
        </mu-container>
    </mu-container>

      <mu-container>
        <mu-flex>
          <mu-expand-transition>
            <mu-container v-show="show.editmenu" class="add_menu">
              <div v-show="new_crew_member.new">New Crew member</div>
              <div v-show="!new_crew_member.new">Edit Crew member</div>
              <mu-text-field v-model="new_crew_member.id" placeholder="id"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.second_name" placeholder="Second name"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.exp" placeholder="Experience"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.category" placeholder="Category"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.adress" placeholder="Adress"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.birth_year" placeholder="Birth_year"></mu-text-field><br>
              <mu-text-field v-model="new_crew_member.bus_id" placeholder="Bus id"></mu-text-field><br>

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
          { title: 'Second Name', name: 'second_name'},
          { title: 'Experience', name: 'exp', sortable: true},
          { title: 'Category', name: 'category', sortable: true},
          { title: 'Adress', name: 'adress',},
          { title: 'Birth year', name: 'birth_year', sortable: true},
          { title: 'Bus id', name: 'bus_id', sortable: true},
        ],

      crew_members: [],
      new_crew_member: {
        id:null,
        second_name:null,
        exp:null,
        category:null,
        adress:null,
        birth_year:null,
        bus_id:null,
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
        var bc = this.crew_members[this.selects[0]];
        this.new_crew_member.id = bc.id;
        this.new_crew_member.second_name = bc.second_name;
        this.new_crew_member.exp = bc.exp;
        this.new_crew_member.category = bc.category;
        this.new_crew_member.adress = bc.adress;
        this.new_crew_member.birth_year = bc.birth_year;
        this.new_crew_member.bus_id = bc.bus_id;
      }else{
        this.new_crew_member.id = null;
        this.new_crew_member.second_name = null
        this.new_crew_member.exp = null;
        this.new_crew_member.category = null;
        this.new_crew_member.adress = null;
        this.new_crew_member.birth_year = null;
        this.new_crew_member.bus_id = null;
      }
      if (this.show.editmenu) {
          this.icons.addmenu_button_icon = "add";
        } else {
          this.icons.addmenu_button_icon = "clear";
        }

        if(this.new_crew_member.new == isNew || !this.show.editmenu) {
          this.show.editmenu = !this.show.editmenu;
        }
          this.new_crew_member.new = isNew;


    },
    loadBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/crew_members/",
          type: "GET",
          success: (response) => {
            this.crew_members = response.data.data
          }
      })
    },
    saveBuses(){
      $.ajax({
        url: "http://127.0.0.1:8000/crew_members/",
          type: "POST",
          data: JSON.stringify(this.crew_members),
        contentType: "application/json",
          success: (response) => {

          }
      })
    },
    addBus(){
      var bb = this.new_crew_member;
      if(bb.id==null) return;
      if(bb.new) {
        var exists = this.crew_members.some(function (field) {
          return parseInt(field.id) === parseInt(bb.id);
        });
      }
      if(exists){
        alert("Error: id already exists");
      }else {
        const bc = this.new_crew_member;

        if (this.new_crew_member.new) {
          this.crew_members.push({
            id: bc.id,
            second_name: bc.second_name,
            exp: bc.exp,
            category: bc.category,
            adress: bc.adress,
            birth_year: bc.birth_year,
            bus_id: bc.bus_id,
          });
        } else {
          this.crew_members[this.selects[0]] = {
            id: bc.id,
            second_name: bc.second_name,
            exp: bc.exp,
            category: bc.category,
            adress: bc.adress,
            birth_year: bc.birth_year,
            bus_id: bc.bus_id,
          };
        }
        this.show.editmenu = false;
        this.new_crew_member.new = false;
        this.selects.splice(0, this.selects.length);
      }
    },
    deleteSelected () {
      console.log(this.selects);

      for(let i =0;i<this.selects.length;i++) {
        this.selects.forEach(((value,index) => {
          this.crew_members.splice(value,1);

        }))
      }
      this.selects.splice(0,this.selects.length);
    },
    handleSortChange ({name, order}) {
      this.crew_members = this.crew_members.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
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
