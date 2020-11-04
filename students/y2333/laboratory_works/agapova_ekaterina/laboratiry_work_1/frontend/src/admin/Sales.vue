<template>
  <div>
    <!--Таблица с данными-->
    <b-table :items="sales" :fields="saleFields" small bordered responsive>
      <!--      Дополнительная ячейка для кнопки "Изменить"    -->
      <template v-slot:cell(id)="data">
        <b-button @click="edit(data.index)" size="sm">Изменить</b-button>
      </template>
      <!--      Подставка названия товара вместо его ID    -->
      <template v-slot:cell(delivery)="data">
        {{ products[data.value] }}
      </template>
      <!--      Подставка email пользователя вместо его ID    -->
      <template v-slot:cell(user)="data">
        {{ users[data.value] }}
      </template>
    </b-table>
    <!--    Окно для создания/редактирования   -->
    <b-modal id="modal-edit"
             title="Изменить"
             ok-title="Сохранить"
             cancel-title="Удалить"
             @ok="saveItem"
             @cancel="deleteItem"
    >
      <b-form-group
        label="Время:"
      >
        <b-form-input
          required
          v-model="editedItem.date"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Товар:"
      >
        <b-form-select v-model="editedItem.delivery" :options="products"></b-form-select>
      </b-form-group>
      <b-form-group
        label="Кол-во:"
      >
        <b-form-input
          required
          type="number"
          v-model="editedItem.quantity"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Пользователь:"
      >
        <b-form-select v-model="editedItem.user" :options="users"></b-form-select>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: "sales",
    data() {
      return {
        //Все продажи
        sales: [],
        //Поля для таблицы
        saleFields: [
          {key: 'date', label: 'Время'},
          {key: 'delivery', label: 'Товар'},
          {key: 'quantity', label: 'Кол-во'},
          {key: 'user', label: 'Пользователь'},
          {key: 'id', label: ''},
        ],
        //Все товары
        products: {},
        //Все поставки
        deliveries: {},
        //Все пользователи
        users: {},
        //Изменяемая строка из таблицы
        editedItem: {
          'date': '',
          'delivery': '',
          'quantity': '',
          'user': '',
        },
        //Новая строка
        defaultItem: {
          'date': '',
          'delivery': '',
          'quantity': '',
          'user': '',
        },
        editedIndex: -1,
      };
    },
    methods: {
      /**
       * Изменение строки
       * @param id строки
       */
      edit(id) {
        this.editedIndex = id;
        this.editedItem = this.sales[id];
        this.$bvModal.show('modal-edit')
      },
      /**
       * Создание строки
       */
      create() {
        this.editedIndex = -1;
        this.editedItem = {...this.defaultItem}
        this.$bvModal.show('modal-edit')
      },
      /**
       * Сохранение
       */
      saveItem() {
        const data = new FormData();
        for (let key in this.editedItem) {
          data.append(key, this.editedItem[key]);
        }
        //Отправка запроса
        axios({
          url: '/sales/' + this.sales[this.editedIndex].id + '/',
          method: 'PUT',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          alert('Продажа изменена!')
        }).catch(() => alert('Произошла ошибка!'))
      },
      /**
       * Удаление строки из таблицы
       */
      deleteItem() {
        //Отправка запроса на удаление
        axios.delete('/sales/' + this.sales[this.editedIndex].id + '/').then((response) => {
          alert('Продажа удалена!')
          this.sales.splice(this.editedIndex, 1)
        }).catch(() => alert('Произошла ошибка!'))
      }
    },
    /**
     * Получение данных о продажах, пользователях, товарах и поставках
     */
    created() {
      axios.get('/sales/').then(response => this.sales = response.data)
      axios.get('/users/').then(response => {
        const users = response.data
        users.forEach(value => {
          this.$set(this.users, value.id, value.email)
        })
      })
      axios.get('/products/').then(response => {
        const products = response.data
        products.forEach(value => {
          this.$set(this.products, value.id, value.name)
        })

        axios.get('/deliveries/').then(response => {
          const deliveries = response.data
          deliveries.forEach(value => {
            this.$set(this.deliveries, value.id, this.products[value.product])
          })
        })
      })
    }
  }
</script>

<style scoped>

</style>
