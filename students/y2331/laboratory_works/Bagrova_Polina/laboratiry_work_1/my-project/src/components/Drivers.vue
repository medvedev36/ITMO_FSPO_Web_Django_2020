<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <Menu slot="left"></Menu>
      Водители
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
    </mu-appbar>
    <mu-paper :z-depth="1" align="center">
      <mu-data-table :columns="columns" :sort.sync="sort"
                     @sort-change="handleSortChange" :data="drivers">
        <template slot-scope="scope">
          <td>{{scope.row.last_name}}</td>
          <td>{{scope.row.first_name}}</td>
          <td class="is-center">{{scope.row.category}}</td>
          <td class="is-center">{{scope.row.experience}}</td>
          <td class="is-center">{{scope.row.birth_year}}</td>
          <td class="is-center">{{scope.row.address}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Menu from "./Menu";

    export default {
        name: "Drivers",
        components: {
            Menu
        },
        data() {
            return {
                drivers: '',
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Фамилия', name: 'last_name', width: 150, sortable: true},
                    {title: 'Имя', name: 'first_name', width: 150, sortable: true},
                    {title: 'Категория', name: 'category', width: 150, align: 'center', sortable: true},
                    {title: 'Опыт', name: 'experience', width: 150, align: 'center', sortable: true},
                    {title: 'Год рождения', name: 'birth_year', width: 150, align: 'center', sortable: true},
                    {title: 'Адрес', name: 'address', width: 300, align: 'center'},
                ],
            }
        },
        created() {
            this.loadDrivers()
        },
        methods: {
            loadDrivers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/drivers/",
                    type: "GET",
                    success: (response) => {
                        this.drivers = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Autopark"})
            },
            handleSortChange({name, order}) {
                if (name === 'category' || name === 'last_name' || name === 'first_name') {
                    this.drivers = this.drivers.sort(function (a, b) {
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
                    this.drivers = this.drivers.sort((a, b) => order === 'asc' ? b[name] - a[name] : a[name] - b[name]);
                }
            },
        }
    }
</script>

<style scoped>

</style>
