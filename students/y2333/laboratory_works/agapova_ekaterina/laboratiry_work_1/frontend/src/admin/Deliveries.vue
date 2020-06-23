<template>
  <div>
    <b-table :items="deliveries" :fields="deliveryFields" small bordered responsive>
      <template v-slot:cell(id)="data">
        <b-button @click="edit(data.index)" size="sm">Изменить</b-button>
      </template>
      <template v-slot:cell(product)="data">
        {{ products[data.value] }}
      </template>
    </b-table>
    <b-button @click="create" size="sm">Создать</b-button>
    <b-modal id="modal-edit"
             :title="editedIndex === -1 ? 'Создать' : 'Изменить'"
             ok-title="Сохранить"
             :ok-only="editedIndex === -1"
             cancel-title="Удалить"
             @ok="saveItem"
             @cancel="deleteItem"
    >
      <b-form-group
        label="Дата поставки:"
      >
        <b-form-input
          required
          placeholder="YYYY-MM-DD"
          v-model="editedItem.delivery_date"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Стоимость для продажи, ₽:"
      >
        <b-form-input
          required
          v-model="editedItem.price_for_sale"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Товар:"
      >
        <b-form-select v-model="editedItem.product" :options="products"></b-form-select>
      </b-form-group>
      <b-form-group
        label="Количество:"
      >
        <b-form-input
          required
          type="number"
          v-model="editedItem.quantity"
        ></b-form-input>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: "deliveries",
    data() {
      return {
        deliveries: [],
        products: {},
        deliveryFields: [
          {key: 'delivery_date', label: 'Дата поставки'},
          {key: 'price_for_sale', label: 'Стоимость для продажи, ₽'},
          {key: 'product', label: 'Товар'},
          {key: 'quantity', label: 'Количество'},
        ],
        editedItem: {
          'delivery_date': '',
          'price_for_sale': 0,
          'product': 0,
          'quantity': 0,
        },
        defaultItem: {
          'delivery_date': '',
          'price_for_sale': 0,
          'product': 0,
          'quantity': 0,
        },
        editedIndex: -1,
      };
    },
    methods: {
      edit(id) {
        this.editedIndex = id;
        this.editedItem = this.deliveries[id];
        this.$bvModal.show('modal-edit')
      },
      create() {
        this.editedIndex = -1;
        this.editedItem = {...this.defaultItem}
        this.$bvModal.show('modal-edit')
      },
      saveItem() {
        const data = new FormData();
        for (let key in this.editedItem) {
          data.append(key, this.editedItem[key]);
        }
        axios({
          url: this.editedIndex === -1 ? '/deliveries/' : '/deliveries/' + this.deliveries[this.editedIndex].id + '/',
          method: this.editedIndex === -1 ? 'POST' : 'PUT',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          alert('Поставка сохранена!')
          if (this.editedIndex === -1) {
            this.deliveries.push(this.editedItem)
          }
        }).catch(() => alert('Произошла ошибка!'))
      },
      deleteItem() {
        axios.delete('/deliveries/' + this.deliveries[this.editedIndex].id + '/').then((response) => {
          alert('Поставка удалена!')
          this.deliveries.splice(this.editedIndex, 1)
        }).catch(() => alert('Произошла ошибка!'))
      }
    },
    created() {
      axios.get('/deliveries/').then(response => this.deliveries = response.data)
      axios.get('/products/').then(response => {
        const products = response.data
        products.forEach(value => {
          this.$set(this.products, value.id, value.name)
        })
      })
    }
  }
</script>

<style scoped>

</style>
