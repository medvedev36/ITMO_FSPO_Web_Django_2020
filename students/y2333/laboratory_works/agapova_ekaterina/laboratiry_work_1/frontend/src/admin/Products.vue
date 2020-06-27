<template>
  <div>
    <!--Таблица с данными-->
    <b-table :items="products" :fields="productFields" small bordered responsive>
      <!--      Дополнительная ячейка для кнопки "Изменить"    -->
      <template v-slot:cell(id)="data">
        <b-button @click="edit(data.index)" size="sm">Изменить</b-button>
      </template>
      <!--      Подставка названия производителя вместо его ID    -->
      <template v-slot:cell(fabric)="data">
        {{ fabrics[data.value] }}
      </template>
    </b-table>
    <b-button @click="create" size="sm">Создать</b-button>
    <!--    Окно для создания/редактирования   -->
    <b-modal id="modal-edit"
             :title="editedIndex === -1 ? 'Создать' : 'Изменить'"
             ok-title="Сохранить"
             :ok-only="editedIndex === -1"
             cancel-title="Удалить"
             @ok="saveItem"
             @cancel="deleteItem"
    >
      <b-form-group
        label="Фабрика:"
      >
        <b-form-select v-model="editedItem.fabric" :options="fabrics"></b-form-select>
      </b-form-group>
      <b-form-group
        label="Фото:"
      >
        <b-form-input
          required
          v-model="editedItem.image"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Название:"
      >
        <b-form-input
          required
          v-model="editedItem.name"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Цена, ₽:"
      >
        <b-form-input
          required
          v-model="editedItem.price"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Код:"
      >
        <b-form-input
          required
          v-model="editedItem.vendor_code"
        ></b-form-input>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: "Products",
    data() {
      return {
        //Все товары
        products: [],
        //Все производители
        fabrics: {},
        //Поля для таблицы
        productFields: [
          {key: 'fabric', label: 'Фабрика'},
          {key: 'image', label: 'Фото'},
          {key: 'name', label: 'Название'},
          {key: 'price', label: 'Цена, ₽'},
          {key: 'vendor_code', label: 'Код'},
          {key: 'id', label: ''},
        ],
        //Изменяемая строка из таблицы
        editedItem: {
          'fabric': '',
          'image': '',
          'name': '',
          'price': 0,
          'vendor_code': '',
        },
        //Новая строка
        defaultItem: {
          'fabric': '',
          'image': '',
          'name': '',
          'price': 0,
          'vendor_code': '',
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
        this.editedItem = this.products[id];
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
          url: this.editedIndex === -1 ? '/products/' : '/products/' + this.products[this.editedIndex].id + '/',
          method: this.editedIndex === -1 ? 'POST' : 'PUT',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          alert('Товар сохранен!')
          if (this.editedIndex === -1) {
            this.products.push(this.editedItem)
          }
        }).catch(() => alert('Произошла ошибка!'))
      },
      /**
       * Удаление строки из таблицы
       */
      deleteItem() {
        axios.delete('/products/' + this.products[this.editedIndex].id + '/').then((response) => {
          alert('Товар удален!')
          this.products.splice(this.editedIndex, 1)
        }).catch(() => alert('Произошла ошибка!'))
      }
    },
    /**
     * Получение данных о товарах и производителях
     */
    created() {
      axios.get('/products/').then(response => this.products = response.data)
      axios.get('/fabrics/').then(response => {
        const fabrics = response.data
        fabrics.forEach(value => {
          this.$set(this.fabrics, value.id, value.name)
        })
      })
    }
  }
</script>

<style scoped>

</style>
