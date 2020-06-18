<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <Menu slot="left"></Menu>
      Путевые листы
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
    </mu-appbar>
    <mu-container align="left">
      <mu-dialog title="Добавление путевого листа" width="500" :open.sync="openAdd">
        Путевой лист будет оформлен на данного пользователя.
        <mu-form :model="form" class="mu-demo-form" :label-position="top" label-width="100">
          <mu-form-item prop="date" label="Дата">
            <mu-date-input v-model="form.date" label-float full-width
                           :date-time-format="enDateFormat" type="date"></mu-date-input>
          </mu-form-item>
          <mu-form-item prop="select" label="Автомобиль">
            <mu-select v-model="form.car">
              <mu-option v-for="car in cars" :key="car.license_plate" :label="car.license_plate"
                         :value="car.license_plate"></mu-option>
            </mu-select>
          </mu-form-item>
        </mu-form>
        <mu-button slot="actions" color="green" @click="addManifest">Добавить</mu-button>
        <mu-button slot="actions" color="primary" @click="closeAddDialog">Закрыть</mu-button>
      </mu-dialog>
      <mu-button color="green" @click="openAddDialog">Добавить</mu-button>
    </mu-container>
    <mu-paper :z-depth="1" align="center">
      <mu-data-table :columns="columns" :sort.sync="sort"
                     @sort-change="handleSortChange" :data="manifests">
        <template slot="expand" slot-scope="prop">
          <div style="padding: 15px;">
            <mu-button small slot="actions" color="primary" @click="openOrderDialog(prop.row.id)">Список заказов
            </mu-button>
            <mu-button small slot="actions" color="primary"
                       @click="openEditDialog(prop.row.date, prop.row.driver.last_name, prop.row.car)">
              Редактировать
            </mu-button>
            <mu-button small slot="actions" color="red" @click="deleteManifest(prop.row.id)">Удалить</mu-button>
            <mu-dialog title="Редактирование путевого листа" width="500" :open.sync="openEdit">
              <mu-form :model="editForm" class="mu-demo-form" :label-position="top" label-width="100">
                <mu-form-item prop="date" label="Дата">
                  <mu-date-input v-model="editForm.date" label-float
                                 full-width :date-time-format="enDateFormat"></mu-date-input>
                </mu-form-item>
                <mu-form-item prop="select" label="Водитель">
                  <mu-select v-model="editForm.driver">
                    <mu-option v-for="driver in drivers" :key="driver.last_name" :label="driver.last_name"
                               :value="driver.id"></mu-option>
                  </mu-select>
                </mu-form-item>
                <mu-form-item prop="select" label="Автомобиль">
                  <mu-select v-model="editForm.car">
                    <mu-option v-for="car in cars" :key="car.license_plate" :label="car.license_plate"
                               :value="car.license_plate"></mu-option>
                  </mu-select>
                </mu-form-item>
              </mu-form>
              <mu-button slot="actions" color="green" @click="updateManifest(prop.row.id)">Сохранить</mu-button>
              <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
            <mu-dialog title="Заказы" width="600" scrollable :open.sync="openOrders">
              <mu-data-table :columns="columnsOrder" :sort.sync="sort"
                             @sort-change="handleSortChange" :data="orders">
                <template slot-scope="scope">
                  <td class="is-center">{{scope.row.direction}}</td>
                  <td>{{scope.row.second_point}}</td>
                  <td class="is-center">{{scope.row.kilometrage}}</td>
                  <td class="is-center">{{scope.row.weight}}</td>
                  <td class="is-center">{{scope.row.price}}</td>
                </template>
              </mu-data-table>
              <mu-button slot="actions" color="primary" @click="closeOrderDialog">Закрыть</mu-button>
            </mu-dialog>
          </div>
        </template>
        <template slot-scope="scope">
          <td class="is-center">{{scope.row.date}}</td>
          <td>{{scope.row.driver.last_name}} {{scope.row.driver.first_name}}</td>
          <td class="is-center">{{scope.row.car}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Menu from "./Menu";

    const dayAbbreviation = ['S', 'M', 'T', 'W', 'T', 'F', 'S'];
    const dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        'Oct', 'Nov', 'Dec'];
    const monthLongList = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];

    const enDateFormat = {
        formatDisplay(date) {
            return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`;
        },
        formatMonth(date) {
            return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`;
        },
        getWeekDayArray(firstDayOfWeek) {
            let beforeArray = [];
            let afterArray = [];
            for (let i = 0; i < dayAbbreviation.length; i++) {
                if (i < firstDayOfWeek) {
                    afterArray.push(dayAbbreviation[i]);
                } else {
                    beforeArray.push(dayAbbreviation[i]);
                }
            }
            return beforeArray.concat(afterArray);
        },
        getMonthList() {
            return monthList;
        }
    };

    export default {
        name: "Manifests",
        components: {
            Menu
        },
        data() {
            return {
                manifests: '',
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Дата', name: 'date', width: 150, sortable: true},
                    {title: 'Водитель', name: 'driver', width: 150, align: 'center'},
                    {title: 'Автомобиль', name: 'car', width: 150, align: 'center', sortable: true},
                ],
                columnsOrder: [
                    {title: 'Направление', name: 'direction', width: 100, sortable: true},
                    {title: 'Второй пункт', name: 'second_point', width: 150, align: 'center', sortable: true},
                    {title: 'Километраж', name: 'kilometrage', width: 100, align: 'center', sortable: true},
                    {title: 'Вес', name: 'weight', width: 100, align: 'center', sortable: true},
                    {title: 'Стоимость', name: 'price', width: 100, align: 'center', sortable: true},
                ],
                form: {
                    date: '',
                    car: '',
                },
                editForm: {
                    date: '',
                    driver: '',
                    car: '',
                },
                openAdd: false,
                openEdit: false,
                openOrders: false,
                cars: '',
                drivers: '',
                orders: '',
                enDateFormat
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadManifests()
            this.loadCars()
            this.loadDrivers()
        },
        methods: {
            loadManifests() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/",
                    type: "GET",
                    success: (response) => {
                        this.manifests = response.data.manifest
                    }
                })
            },
            addManifest() {
                var dateStr = new Date(this.form.date).getFullYear() + '-'
                dateStr += (new Date(this.form.date).getMonth() + 1) + '-'
                dateStr += new Date(this.form.date).getDate()
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/",
                    type: "POST",
                    data: {
                        date: dateStr,
                        car: this.form.car
                    },
                    success: (response) => {
                        alert("Путевой лист добавлен")
                        this.loadManifests()
                        this.closeAddDialog()
                        this.form = {
                            date: '',
                            car: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            updateManifest(id) {
                var dateStr = new Date(this.editForm.date).getFullYear() + '-'
                dateStr += (new Date(this.editForm.date).getMonth() + 1) + '-'
                dateStr += new Date(this.editForm.date).getDate()
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/" + id,
                    type: "PUT",
                    data: {
                        date: dateStr,
                        driver: this.editForm.driver,
                        car: this.editForm.car
                    },
                    success: (response) => {
                        alert("Путевой лист обновлен")
                        this.loadManifests()
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            deleteManifest(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Путевой лист удален")
                        this.loadManifests()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            loadOrders(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/" + id,
                    type: "GET",
                    success: (response) => {
                        this.orders = response.data.orders
                    }
                })
            },
            loadCars() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/cars/",
                    type: "GET",
                    success: (response) => {
                        this.cars = response.data.data
                    }
                })
            },
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
            openAddDialog() {
                this.openAdd = true
            },
            closeAddDialog() {
                this.openAdd = false;
            },
            openEditDialog(date, driver, car) {
                this.editForm.date = date
                this.editForm.driver = driver
                this.editForm.car = car
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            openOrderDialog(id) {
                this.openOrders = true
                this.loadOrders(id)
            },
            closeOrderDialog() {
                this.openOrders = false;
            },
            handleSortChange({name, order}) {
                this.manifests = this.manifests.sort(function (a, b) {
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
            },
        }
    }
</script>

<style scoped>

</style>
