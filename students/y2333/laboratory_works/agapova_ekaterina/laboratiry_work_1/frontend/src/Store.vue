<template>
  <div>
<!--    Заголовок главной страницы магазина   -->
    <b-jumbotron header="Ювелирная фантазия" lead="Украшения, которые придутся по душе" />
<!--    Меню для покупки   -->
    <b-modal id="modal-buy"
             title="Покупка"
             ok-title="Купить"
             cancel-title="Отмена"
             @ok="buy(toBuy.id, toBuy.toBuyQuantity)"
    >
      <p class="my-4">
        <strong>{{ toBuy.name }}</strong><br>
        {{ toBuy.quantity }} доступно<br>
        {{ toBuy.price_for_sale }}₽
      </p>
      <b-form-group
        label="Кол-во к покупке:"
      >
        <b-form-input
          required
          v-model="toBuy.toBuyQuantity"
          type="number"
        ></b-form-input>
      </b-form-group>
    </b-modal>
    <b-container>
      <b-row v-for="(chunkedProducts, i) in products" :key="i" class="mb-3">
        <b-col md="4" sm="12" v-for="(product, j) in chunkedProducts" :key="product.id">
<!--          Данные о товарах    -->
          <b-card
            :title="product.name"
            :img-src="product.image"
          >
            <p>
              {{ product.price_for_sale }}₽<br>
              {{ product.quantity }} доступно<br>
              {{ product.fabric_country }}, {{ product.fabric_name }}
            </p>
            <b-button variant="primary" @click="openBuyMenu(i, j)">Купить</b-button>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  export default {
    name: "Store",
    data() {
      return {
        //Все товары
        products: [],
        //Данные о процессе покупки
        toBuy: {
          name: '',
          quantity: 0,
          id: 0,
          toBuyQuantity: 1,
          price_for_sale: 0,
        }
      };
    },
    /**
     * Получение продаваемых товаров
     */
    created() {
      axios.get('/store/').then(response => {
        let products = response.data;
        for (let i = 0; i < Math.ceil(products.length/3); i++) {
          this.products.push(products.slice(i*3, i*3+3))
        }
      })
    },
    methods: {
      /**
       * Открытие меню покупки
       * @param i
       * @param j
       */
      openBuyMenu(i, j) {
        if (!this.$root.loggedIn) {
          alert('Сначала треубется зарегистрироваться и войти!')
          return;
        }
        this.toBuy.name = this.products[i][j].name;
        this.toBuy.quantity = this.products[i][j].quantity;
        this.toBuy.id = this.products[i][j].id;
        this.toBuy.price_for_sale = this.products[i][j].price_for_sale;
        this.$bvModal.show('modal-buy')
      },
      /**
       * Покупка товара
       * @param id
       * @param quantity
       */
      buy(id, quantity) {
        let data = new FormData()
        data.set('id', id)
        data.set('quantity', quantity)
        //Отправка запроса на покупку
        axios({
          url: '/user/sale/',
          method: 'POST',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then(() => {
          alert('Поздравляем с покупкой!')
        })
      }
    }
  }
</script>

<style scoped>

</style>
