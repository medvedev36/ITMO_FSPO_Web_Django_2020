<template>

  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <Menu slot="left"></Menu>
      Автомобили
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1" align="center">
      <mu-data-table :columns="columns" :sort.sync="sort"
                     @sort-change="handleSortChange" :data="cars">
        <template slot-scope="scope">
          <td class="is-center">{{scope.row.license_plate}}</td>
          <td class="is-center">{{scope.row.model}}</td>
          <td class="is-center">{{scope.row.run}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Menu from "./Menu";

    export default {
        name: "Cars",
        components: {
            Menu
        },
        data() {
            return {
                cars: '',
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {
                        title: 'Государственный номер',
                        name: 'license_plate',
                        width: 200,
                        align: 'center',
                        sortable: true
                    },
                    {title: 'Модель', name: 'model', width: 150, align: 'center', sortable: true},
                    {title: 'Пробег', name: 'run', width: 150, align: 'center', sortable: true},
                ],
            }
        },
        created() {
            this.loadCars()
        },
        methods: {
            loadCars() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/cars/",
                    type: "GET",
                    success: (response) => {
                        this.cars = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Autopark"})
            },
            handleSortChange({name, order}) {
                if (name === 'license_plate' || name === 'model') {
                    this.cars = this.cars.sort(function (a, b) {
                            var nameA = a[name].toLowerCase(), nameB = b[name].toLowerCase()
                            if (order === 'asc') {
                                if (nameA < nameB) {
                                    return 1
                                }
                                if (nameA > nameB) {
                                    return -1
                                }
                                return 0
                            } else {
                                if (nameA < nameB)
                                    return -1
                                if (nameA > nameB)
                                    return 1
                                return 0
                            }
                        }
                    )
                } else {
                    this.cars = this.cars.sort((a, b) => order === 'asc' ? b[name] - a[name] : a[name] - b[name]);
                }
            },
        }
    }
</script>

<style scoped>

</style>
