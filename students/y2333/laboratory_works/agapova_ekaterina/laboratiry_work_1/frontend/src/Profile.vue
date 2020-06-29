<template>
  <b-container>
    <b-row class="mt-3 justify-content-md-center">
      <b-col sm="12" md="6">
        <b-card title="Профиль">
<!--          Форма с данными о пользователе и возможностью редактирования   -->
          <b-form @submit.prevent="update">
            <b-form-group
              label="Почта:"
            >
              <b-form-input
                required
                placeholder="email"
                v-model="email"
                type="email"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Номер карты:"
            >
              <b-form-input
                required
                placeholder="card"
                v-model="card"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Имя:"
            >
              <b-form-input
                required
                placeholder="Имя"
                v-model="first_name"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Фамилия:"
            >
              <b-form-input
                required
                placeholder="Фамилия"
                v-model="last_name"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              label="Дата рождения:"
            >
              <b-form-input
                v-model="date_of_birth"
                type="text"
                placeholder="YYYY-MM-DD"
                autocomplete="off"
              ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Сохранить</b-button>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
    <b-row class="mt-3 mb-3 justify-content-md-center">
      <b-col sm="12" md="6">
<!--        Данные о покупках пользователя       -->
        <b-card title="Покупки">
          <b-table :items="sales" :fields="saleFields"></b-table>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "Profile",
    data() {
      return {
        //Данные пользователя
        email: this.$root.user.email,
        date_of_birth: this.$root.user.date_of_birth,
        card: this.$root.user.card,
        first_name: this.$root.user.first_name,
        last_name: this.$root.user.last_name,
        sales: [],
        //Поля таблицы с покупками
        saleFields: [
          {key: 'name', label: 'Изделие'},
          {key: 'quantity', label: 'Кол-во'},
          {key: 'total', label: 'Всего, ₽'},
        ]
      };
    },
    watch: {
      /**
       * Обновление значений в форме при изменении
       */
      '$root.user'() {
        this.email = this.$root.user.email;
        this.date_of_birth = this.$root.user.date_of_birth;
        this.card = this.$root.user.card;
        this.first_name = this.$root.user.first_name;
        this.last_name = this.$root.user.last_name;
      }
    },
    /**
     * Получение данных о покупках
     */
    created() {
      axios.get('/user/sale/').then(response => {
        this.sales = response.data
      })
    },
    methods: {
      /**
       * Обновление данных о пользователе
       */
      update() {
        let bodyFormData = new FormData();
        bodyFormData.set('email', this.email);
        bodyFormData.set('date_of_birth', this.date_of_birth);
        bodyFormData.set('card', this.card);
        bodyFormData.set('first_name', this.first_name);
        bodyFormData.set('last_name', this.last_name);
        //Отправка запроса на обновление
        axios({
          method: 'put',
          url: '/user/',
          data: bodyFormData,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then(response => {
          alert('Данные профиля обновлены!')
        }).catch(() => {
          alert('Что-то заполнено неверно, попробуйте еще раз!')
        });
      },
    }
  }
</script>

<style scoped>

</style>
