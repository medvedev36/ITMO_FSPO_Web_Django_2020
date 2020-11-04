<template>
    <mu-container>
    <vue-headful title="Мои автомобили"/>
        <mu-row>
            <mu-appbar style="width: 100%" color="deepPurple700">
                <span class="main-font" style="font-size: 20pt; float: left">Автомастерские &laquoПод капотом&raquo</span>
                <mu-button flat slot="right" @click="goto_main">На главную</mu-button>
            </mu-appbar>
        </mu-row>
        <mu-row>
            <h1 class="main-font" style="margin: 3% auto 0">Мои автомобили</h1>
        </mu-row>
        <mu-row>
            <h1 class="main-font" v-if="empty_flag" style="margin: 3% auto 0">Список заявок пуст</h1>
        </mu-row>
        <div>
            <mu-button class="green-button" style="margin-left: 45%" @click="goto_auto_add">Добавить авто</mu-button>
        </div>

        <mu-row class="alert" v-if="alert">
            <mu-col span=10>
                <span class="main-font" style="font-size: 18pt; float: left">{{alert_text}}</span>
            </mu-col>
            <mu-col span=2>
                <mu-button class="blue-button" @click="close_alert">Ок</mu-button>
            </mu-col>
        </mu-row>

        <mu-row gutter v-for="auto in autos">
        <div class="info-pannel" style="width: 70%">
            <mu-row>
                <span class="main-font" style="font-size: 20pt; float: left">{{auto.brand}} {{auto.model}}</span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 20pt; float: left">Гос. номер: {{auto.number}}</span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 15pt; float: left">Год выпуска: <strong>{{auto.year}}</strong></span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 15pt; float: left">Тех. паспорт: <strong>{{auto.tech_passport}}</strong></span>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="open_confirm_dialog">Удалить</mu-button>

                <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="confirm_dialog">
                    <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: #212121">Вы точно уверены, что хотите удалить автомобиль?</span>
                    <div align="center" style="margin-top: 5%">
                        <mu-button class="blue-button" slot="actions" @click="close_confirm_dialog">Отмена</mu-button>
                        <mu-button class="red-button" slot="actions" @click="conf_delete(auto.id)">Удалить</mu-button>
                    </div>
                </mu-dialog>

                <mu-button class="blue-button" @click="goto_auto_edit(auto)">Редактировать</mu-button>
            </div>
        </div>
        </mu-row>

        <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="alert_dialog">
            <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: #212121">{{alert_text}}</span>
            <div align="center" style="margin-top: 5%">
                <mu-button class="blue-button" slot="actions" @click="close_alert_dialog">Ок</mu-button>
            </div>
        </mu-dialog>

    </mu-container>
</template>


<script>
    import $ from 'jquery'

    export default {
        name: "Owner_autos",
        data() {
            return {
                autos: "",
                confirm_dialog: false,
                alert_dialog: false,
                alert: false,
                alert_text: "",
            }
        },
        created() {
            $.ajaxSetup({
                headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")}
            });
            this.get_autos()
            if(this.$route.query.outer_alert) {
                this.alert_text = this.$route.query.outer_alert;
                this.show_alert()
            }
        },
        methods: {
        	goto_main() {
        		this.$router.push({name: "main_rout"})
        	},
            goto_auto_add() {
                this.$router.push({name: "owner_auto_add_rout"})
            },
            goto_auto_edit(current_auto) {
                this.$router.push({name: "owner_auto_edit_rout", query: {"current_auto": current_auto}})
            },
            get_autos() {
                $.ajax({
                    url: "http://127.0.0.1:8000/owner_autos_list/",
                    type: "GET",
                    success: (response) => {
                        this.autos = response.data.data
                    },
                    error: (response) => {
                        this.alert_text = "Ошибка на стороне сервера";
                        this.open_alert_dialog()
                    }
                })
            },
            remove_auto(id) {
                var href = "http://127.0.0.1:8000/owner_auto_remove/" + id + "/"
                $.ajax({
                    url: href,
                    type: "DELETE",
                    success: (response) => {
                        this.alert_text = "Автомобиль успешно удалён";
                        this.show_alert()
                        this.get_autos()
                        this.$forceUpdate();
                    },
                    error: (response) => {
                        this.alert_text = "Ошибка на стороне сервера";
                        this.open_alert_dialog()
                    }
                })
            },
            conf_delete(id) {
                this.close_confirm_dialog()
                this.remove_auto(id)
            },
            open_confirm_dialog() {
                this.confirm_dialog = true;
            },
            close_confirm_dialog() {
                this.confirm_dialog = false;
            },
            open_alert_dialog() {
                this.alert_dialog = true;
            },
            close_alert_dialog() {
                this.alert_dialog = false;
            },
            show_alert() {
                this.alert = true;
            },
            close_alert() {
                this.alert = false;
            }
        },
    }
</script>


<style lang="scss" scoped>
    @import '@/assets/styles.scss';
</style>