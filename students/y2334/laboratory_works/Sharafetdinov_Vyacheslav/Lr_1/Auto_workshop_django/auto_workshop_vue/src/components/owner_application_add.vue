<template>
    <mu-container>
    <vue-headful title="Создание заявки"/>
        <div class="form-pannel" style="width: 50%">
            <mu-row gutter>
                <mu-col span=3 class="form-pannel-cell">
                    <label class="form-label"><strong>Автомобиль:</strong></label>
                </mu-col>
                <mu-col span=9 class="form-pannel-cell">
                    <select form style="float: left" v-model="auto_id">
                        <option disabled value="">Выберите автомобиль</option>
                        <option v-for="auto in autos" v-bind:value="auto.id">
                            <span class="main-font" style="font-size: 12pt; text-align: left">
                                {{auto.brand}} {{auto.model}} {{auto.number}}
                            </span>
                        </option>
                    </select>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=3 class="form-pannel-cell">
                    <label class="form-label"><strong>Мастерская:</strong></label>
                </mu-col>
                <mu-col span=9 class="form-pannel-cell">
                    <select form style="float: left" v-model="workshop_id">
                        <option disabled value="">Выберите мастерскую</option>
                        <option v-for="workshop in workshops" v-bind:value="workshop.id">
                            <span class="main-font" style="font-size: 12pt; text-align: left">
                                №{{workshop.number}} {{workshop.address}}
                            </span>
                        </option>
                    </select>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=3 class="form-pannel-cell">
                    <label class="form-label"><strong>Дата записи:</strong></label>
                </mu-col>
                <mu-col span=9 class="form-pannel-cell">
                    <input class="form-input" v-model="date" type="date"/>
                </mu-col>
            </mu-row>
            <mu-row>
                <label style="float: left"><strong>Описание:</strong></label>
            </mu-row>
            <mu-row>
                <textarea rows="10" class="form-textarea" style="float: left" v-model="description"></textarea>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="goto_owner_applications">Отмена</mu-button>
                <mu-button class="blue-button" @click="conf_application_add">Отправить</mu-button>
            </div>
        </div>

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
        name: "Owner_auto_add",
        data() {
            return {
                autos: "",
                workshops: "",
                auto_id: "",
                workshop_id: "",
                date: "",
                description: "",
                alert_dialog: false,
                alert_text: "",
            }
        },
        mounted () {
            this.get_workshops()
            this.get_autos()
        },
        methods: {
            goto_owner_applications() {
                this.$router.push({name: "owner_applications_rout"})
            },
            get_workshops() {
                $.ajax({
                    url: "http://127.0.0.1:8000/workshops_for_application_list/",
                    type: "GET",
                    success: (response) => {
                        this.workshops = response.data.data
                    },
                    error: (response) => {
                        this.alert_text = "Ошибка на стороне сервера";
                        this.open_alert_dialog()
                    }
                })
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
            conf_application_add() {
            	if (this.auto_id && this.workshop_id && this.date && this.description) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/owner_application_add/",
                        type: "POST",
                        data: {
                            auto: this.auto_id,
                            workshop: this.workshop_id,
                            date: this.date,
                            status: "cons",
                            date_init: "01-01-2000",
                            description: this.description,
                        },
                        success: (response) => {
                            this.$router.push({name: "owner_applications_rout", query: {"outer_alert": "Заявка успешно отправлена"}})
                        },
                        error: (response) => {
                            if(response.status == 400) {
                    			this.alert_text = "Имеется неверно введённое поле";
                    			this.open_alert_dialog()
                            }
                            else {
                    			this.alert_text = "Ошибка на стороне сервера";
                    			this.open_alert_dialog()
                            }
                        }
                    })
                }
                else {
                    this.alert_text = "Введите все необходимые поля формы";
                    this.open_alert_dialog()
                }
            },
            open_alert_dialog() {
                this.alert_dialog = true;
            },
            close_alert_dialog() {
                this.alert_dialog = false;
            },
        }
    }
</script>


<style lang="scss" scoped>
    @import '@/assets/styles.scss';
</style>