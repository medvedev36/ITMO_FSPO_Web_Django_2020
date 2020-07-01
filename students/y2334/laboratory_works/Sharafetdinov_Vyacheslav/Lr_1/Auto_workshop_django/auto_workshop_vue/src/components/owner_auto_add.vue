<template>
    <mu-container>
    <vue-headful title="Добавление автомобиля"/>
        <div class="form-pannel" style="width: 41%">
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Гос. номер:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="number" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Марка:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" input v-model="brand" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Модель:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="model" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Год производства:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="year" type="number"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Тех. паспорт:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="tech_passport" type="text"/>
                </mu-col>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="goto_owner_autos">Отмена</mu-button>
                <mu-button class="blue-button" @click="conf_auto_add">Добавить</mu-button>
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
                number: "",
                brand: "",
                model: "",
                year: "",
                tech_passport: "",
                alert_dialog: false,
                alert_text: "",
            }
        },
        methods: {
            goto_owner_autos() {
                this.$router.push({name: "owner_autos_rout"})
            },
            conf_auto_add() {
                if (this.number && this.brand && this.model && this.year && this.tech_passport) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/owner_auto_add/",
                        type: "POST",
                        data: {
                            number: this.number,
                            brand: this.brand,
                            model: this.model,
                            year: this.year,
                            tech_passport: this.tech_passport
                        },
                        success: (response) => {
                            this.$router.push({name: "owner_autos_rout", query: {"outer_alert": "Автомобиль успешно добавлен"}})
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