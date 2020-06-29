<template>
  <div>
    <!--Таблица с данными-->
    <b-table :items="users" :fields="userFields" small bordered responsive>
      <!--      Дополнительная ячейка для кнопки "Изменить"    -->
      <template v-slot:cell(id)="data">
        <b-button @click="edit(data.index)" size="sm">Изменить</b-button>
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
        label="Имя:"
      >
        <b-form-input
          required
          v-model="editedItem.first_name"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Фамилия:"
      >
        <b-form-input
          required
          v-model="editedItem.last_name"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Почта:"
      >
        <b-form-input
          required
          type="email"
          v-model="editedItem.email"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Дата рождения:"
      >
        <b-form-input
          required
          placeholder="YYYY-MM-DD"
          v-model="editedItem.date_of_birth"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Карта:"
      >
        <b-form-input
          required
          v-model="editedItem.card"
        ></b-form-input>
      </b-form-group>
      <b-form-checkbox
        v-model="editedItem.is_superuser"
      >
        Админ
      </b-form-checkbox>
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: "Users",
    data() {
      return {
        //Все пользователи
        users: [],
        //Поля для таблицы
        userFields: [
          {key: 'first_name', label: 'Имя'},
          {key: 'last_name', label: 'Фамилия'},
          {key: 'email', label: 'Почта'},
          {key: 'date_of_birth', label: 'Дата рождения'},
          {key: 'card', label: 'Карта'},
          {key: 'is_superuser', label: 'Админ'},
          {key: 'id', label: ''},
        ],
        //Изменяемая строка из таблицы
        editedItem: {
          'first_name': '',
          'last_name': '',
          'email': '',
          'date_of_birth': '',
          'card': '',
          'is_superuser': false
        },
        //Новая строка
        defaultItem: {
          'first_name': '',
          'last_name': '',
          'email': '',
          'date_of_birth': '',
          'card': '',
          'is_superuser': false
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
        this.editedItem = this.users[id];
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
          url: '/users/' + this.users[this.editedIndex].id + '/',
          method: 'PUT',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          alert('Пользователь изменен!')
        }).catch(() => alert('Произошла ошибка!'))
      },
      /**
       * Удаление строки из таблицы
       */
      deleteItem() {
        //Отправка запроса на удаление
        axios.delete('/users/' + this.users[this.editedIndex].id + '/').then((response) => {
          alert('Пользователь удален!')
          this.users.splice(this.editedIndex, 1)
        }).catch(() => alert('Произошла ошибка!'))
      }
    },
    /**
     * Получение данных о пользователях
     */
    created() {
      axios.get('/users/').then(response => this.users = response.data)
    }
  }
</script>

<style scoped>

</style>
