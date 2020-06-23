<template>
  <div>
    <b-table :items="fabrics" :fields="fabricFields" small bordered responsive>
      <template v-slot:cell(id)="data">
        <b-button @click="edit(data.index)" size="sm">Изменить</b-button>
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
        label="Адрес:"
      >
        <b-form-input
          required
          v-model="editedItem.address"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        label="Страна:"
      >
        <b-form-input
          required
          v-model="editedItem.country"
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
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: "Fabrics",
    data() {
      return {
        fabrics: [],
        fabricFields: [
          {key: 'address', label: 'Адрес'},
          {key: 'country', label: 'Страна'},
          {key: 'name', label: 'Название'},
          {key: 'id', label: ''},
        ],
        editedItem: {
          'address': '',
          'country': '',
          'name': ''
        },
        defaultItem: {
          'address': '',
          'country': '',
          'name': ''
        },
        editedIndex: -1,
      };
    },
    methods: {
      edit(id) {
        this.editedIndex = id;
        this.editedItem = this.fabrics[id];
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
          url: this.editedIndex === -1 ? '/fabrics/' : '/fabrics/' + this.fabrics[this.editedIndex].id + '/',
          method: this.editedIndex === -1 ? 'POST' : 'PUT',
          data: data,
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          alert('Фабрика сохранена!')
          if (this.editedIndex === -1) {
            this.fabrics.push(this.editedItem)
          }
        }).catch(() => alert('Произошла ошибка!'))
      },
      deleteItem() {
        axios.delete('/fabrics/' + this.fabrics[this.editedIndex].id + '/').then((response) => {
          alert('Фабрика удалена!')
          this.fabrics.splice(this.editedIndex, 1)
        }).catch(() => alert('Произошла ошибка!'))
      }
    },
    created() {
      axios.get('/fabrics/').then(response => this.fabrics = response.data)
    }
  }
</script>

<style scoped>

</style>
