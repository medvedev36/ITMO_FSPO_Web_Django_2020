<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <Menu slot="left"></Menu>
      Заказы
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
    </mu-appbar>
    <mu-container align="left">
      <mu-dialog title="Добавление клиента" width="500" scrollable :open.sync="openAdd">
        <mu-form :model="form" class="mu-demo-form" :label-position="top" label-width="100">
          <mu-form-item prop="select" label="Клиент">
            <mu-select v-model="form.client">
              <mu-option v-for="client in clients" :key="client.name" :label="client.name"
                         :value="client.id"></mu-option>
            </mu-select>
          </mu-form-item>
          <mu-form-item prop="select" label="Направление">
            <mu-select v-model="form.direction">
              <mu-option v-for="direction in directions" :key="direction" :label="direction"
                         :value="direction"></mu-option>
            </mu-select>
          </mu-form-item>
          <mu-form-item prop="input" label="Второй пункт">
            <mu-text-field v-model="form.second_point"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="input" label="Километраж">
            <mu-text-field v-model="form.kilometrage"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="input" label="Вес груза">
            <mu-text-field v-model="form.weight"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="input" label="Стоимость">
            <mu-text-field v-model="form.price"></mu-text-field>
          </mu-form-item>
          <mu-form-item prop="select" label="Путевой лист">
            <mu-select v-model="form.manifest">
              <mu-option v-for="manifest in manifests" :key="manifest.date" :label="manifest.date"
                         :value="manifest.id"></mu-option>
            </mu-select>
          </mu-form-item>
        </mu-form>
        <mu-button slot="actions" color="green" @click="addOrder">Добавить</mu-button>
        <mu-button slot="actions" color="primary" @click="closeAddDialog">Закрыть</mu-button>
      </mu-dialog>
      <mu-button color="green" @click="openAddDialog">Добавить</mu-button>
    </mu-container>
    <mu-paper :z-depth="1" align="center">
      <mu-data-table :columns="columns" :sort.sync="sort"
                     @sort-change="handleSortChange" :data="orders">
        <template slot="expand" slot-scope="prop">
          <div style="padding: 15px;">
            <!--            <mu-button small slot="actions" color="primary" @click="loadInformation(prop.row.id)">-->
            <!--              Состав перевозки-->
            <!--            </mu-button>-->
            <mu-button small slot="actions" color="primary"
                       @click="openEditDialog(prop.row.client, prop.row.direction, prop.row.second_point, prop.row.kilometrage, prop.row.weight, prop.row.price, prop.row.manifest)">
              Редактировать
            </mu-button>
            <mu-button small slot="actions" color="red" @click="deleteOrder(prop.row.id)">Удалить</mu-button>
            <mu-dialog title="Редактирование клиента" width="500" scrollable :open.sync="openEdit">
              <mu-form :model="editForm" class="mu-demo-form" :label-position="top" label-width="100">
                <mu-form-item prop="select" label="Клиент">
                  <mu-select v-model="editForm.client">
                    <mu-option v-for="client in clients" :key="client.name" :label="client.name"
                               :value="client.id"></mu-option>
                  </mu-select>
                </mu-form-item>
                <mu-form-item prop="select" label="Направление">
                  <mu-select v-model="editForm.direction">
                    <mu-option v-for="direction in directions" :key="direction" :label="direction"
                               :value="direction"></mu-option>
                  </mu-select>
                </mu-form-item>
                <mu-form-item prop="input" label="Второй пункт">
                  <mu-text-field v-model="editForm.second_point"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="input" label="Километраж">
                  <mu-text-field v-model="editForm.kilometrage"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="input" label="Вес груза">
                  <mu-text-field v-model="editForm.weight"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="input" label="Стоимость">
                  <mu-text-field v-model="editForm.price"></mu-text-field>
                </mu-form-item>
                <mu-form-item prop="select" label="Путевой лист">
                  <mu-select v-model="editForm.manifest">
                    <mu-option v-for="manifest in manifests" :key="manifest.date" :label="manifest.date"
                               :value="manifest.id"></mu-option>
                  </mu-select>
                </mu-form-item>
              </mu-form>
              <mu-button slot="actions" color="green" @click="updateOrder(prop.row.id)">Сохранить</mu-button>
              <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
          </div>
        </template>
        <template slot-scope="scope">
          <td class="is-center">{{scope.row.direction}}</td>
          <td>{{scope.row.second_point}}</td>
          <td class="is-center">{{scope.row.kilometrage}}</td>
          <td class="is-center">{{scope.row.weight}}</td>
          <td class="is-center">{{scope.row.price}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Menu from "./Menu";

    export default {
        name: "Orders",
        components: {
            Menu
        },
        data() {
            return {
                orders: '',
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Направление', name: 'direction', width: 150, sortable: true},
                    {title: 'Второй пункт', name: 'second_point', width: 300, align: 'center'},
                    {title: 'Километраж', name: 'kilometrage', width: 100, align: 'center', sortable: true},
                    {title: 'Вес', name: 'weight', width: 100, align: 'center', sortable: true},
                    {title: 'Стоимость', name: 'price', width: 100, align: 'center', sortable: true},
                ],
                openAdd: false,
                openEdit: false,
                form: {
                    client: '',
                    direction: '',
                    second_point: '',
                    kilometrage: '',
                    weight: '',
                    price: '',
                    manifest: ''
                },
                editForm: {
                    client: '',
                    direction: '',
                    second_point: '',
                    kilometrage: '',
                    weight: '',
                    price: '',
                    manifest: ''
                },
                directions: [
                    'To client',
                    'From client'
                ],
                clients: '',
                manifests: '',
                composition: '',
                client: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadOrders()
            this.loadClients()
            this.loadManifests()
        },
        methods: {
            loadOrders() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/orders/",
                    type: "GET",
                    success: (response) => {
                        this.orders = response.data.orders
                    }
                })
            },
            addOrder() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/orders/",
                    type: "POST",
                    data: {
                        client: this.form.client,
                        direction: this.form.direction,
                        second_point: this.form.second_point,
                        kilometrage: parseFloat(this.form.kilometrage),
                        weight: parseFloat(this.form.weight),
                        price: parseFloat(this.form.price),
                        manifest: this.form.manifest
                    },
                    success: (response) => {
                        alert("Заказ добавлен")
                        this.loadOrders()
                        this.closeAddDialog()
                        this.form = {
                            client: '',
                            direstion: '',
                            second_point: '',
                            kilometrage: '',
                            weight: '',
                            price: '',
                            manifest: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            updateOrder(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/orders/" + id,
                    type: "PUT",
                    data: {
                        client: this.editForm.client,
                        direction: this.editForm.direction,
                        second_point: this.editForm.second_point,
                        kilometrage: parseFloat(this.editForm.kilometrage),
                        weight: parseFloat(this.editForm.weight),
                        price: parseFloat(this.editForm.price),
                        manifest: this.editForm.manifest
                    },
                    success: (response) => {
                        alert("Заказ обновлен")
                        this.loadOrders()
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            deleteOrder(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/orders/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Заказ удален")
                        this.loadOrders()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            loadClients() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/clients/",
                    type: "GET",
                    success: (response) => {
                        this.clients = response.data.data
                    }
                })
            },
            loadManifests() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/manifests/",
                    type: "GET",
                    success: (response) => {
                        this.manifests = response.data.manifest
                    }
                })
            },
            loadInformation(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/orders/" + id,
                    type: "GET",
                    success: (response) => {
                        this.composition = response.data.items
                        this.client = response.data.client
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Autopark"})
            },
            handleSortChange({name, order}) {
                if (name === 'direction') {
                    this.orders = this.orders.sort(function (a, b) {
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
                    this.orders = this.orders.sort((a, b) => order === 'asc' ? b[name] - a[name] : a[name] - b[name]);
                }
            },
            openAddDialog() {
                this.openAdd = true
            },
            closeAddDialog() {
                this.openAdd = false;
            },
            openEditDialog(client, direction, second_point, kilometrage, weight, price, manifest) {
                this.editForm.client = client
                this.editForm.direction = direction
                this.editForm.second_point = second_point
                this.editForm.kilometrage = kilometrage
                this.editForm.weight = weight
                this.editForm.price = price
                this.editForm.manifest = manifest
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
        }
    }
</script>

<style scoped>

</style>
