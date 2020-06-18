<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <Menu slot="left"></Menu>
      Клиенты
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
    </mu-appbar>
    <mu-list textline="two-line" v-for="client in clients">
      <mu-list-item button @click="openEditDialog(client.name, client.address)">
        <mu-list-item-content>
          <mu-list-item-title><strong>{{client.name}}</strong></mu-list-item-title>
          <mu-list-item-sub-title style="color: rgba(0, 0, 0, .87)">{{client.address}}</mu-list-item-sub-title>
          <mu-container aligh="left">
            <mu-dialog title="Редактирование" width="500" :open.sync="openEdit">
              <mu-text-field v-model="editForm.name" type="text" placeholder="Название"></mu-text-field>
              <br>
              <mu-text-field v-model="editForm.address" type="text" placeholder="Адрес"></mu-text-field>
              <br>
              <mu-button slot="actions" color="green" @click="updateClient(client.id)">Сохранить</mu-button>
              <mu-button slot="actions" color="red" @click="deleteClient(client.id)">Удалить</mu-button>
              <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
          </mu-container>
        </mu-list-item-content>
      </mu-list-item>
      <mu-divider></mu-divider>
    </mu-list>
    <mu-container align="left">
      <mu-form :model="form" class="mu-demo-form" :label-position="top" label-width="100">
        <mu-form-item prop="input" label="Название">
          <mu-text-field v-model="form.name"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="input" label="Адрес">
          <mu-text-field v-model="form.address"></mu-text-field>
        </mu-form-item>
      </mu-form>
      <mu-button color="green" @click="addClient">Добавить</mu-button>
    </mu-container>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Menu from "./Menu";

    export default {
        name: "Clients",
        components: {
            Menu
        },
        data() {
            return {
                clients: '',
                form: {
                    name: '',
                    address: '',
                },
                editForm: {
                    name: '',
                    address: '',
                },
                openEdit: false
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadClients()
        },
        methods: {
            goHome() {
                this.$router.push({name: "Autopark"})
            },
            openEditDialog(name, address) {
                this.editForm.name = name
                this.editForm.address = address
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
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
            addClient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/clients/",
                    type: "POST",
                    data: {
                        name: this.form.name,
                        address: this.form.address
                    },
                    success: (response) => {
                        alert("Клиент добавлен")
                        this.loadClients()
                        this.form = {
                            name: '',
                            address: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            updateClient(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/clients/" + id,
                    type: "PUT",
                    data: {
                        name: this.editForm.name,
                        address: this.editForm.address
                    },
                    success: (response) => {
                        alert("Клиент обновлен")
                        this.loadClients()
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            deleteClient(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/autopark/clients/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Клиент удален")
                        this.loadClients()
                        this.closeEditDialog()
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
