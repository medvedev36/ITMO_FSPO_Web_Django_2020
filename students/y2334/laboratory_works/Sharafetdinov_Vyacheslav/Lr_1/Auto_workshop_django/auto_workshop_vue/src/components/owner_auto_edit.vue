<template>
    <mu-container>
    <vue-headful title="Редактирование данных автомобиля"/>
        <div class="form-pannel" style="width: 41%">
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Гос. номер:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="auto.number" type="text" :placeholder="auto.number"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Марка:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="auto.brand" type="text" :placeholder="auto.brand"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Модель:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="auto.model" type="text" :placeholder="auto.model"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Год производства:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="auto.year" type="text" :placeholder="auto.year"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Тех. паспорт:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="auto.tech_passport" type="text" :placeholder="auto.tech_passport"/>
                </mu-col>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="goto_owner_autos">Отмена</mu-button>
                <mu-button class="blue-button" @click="conf_auto_edit(auto.id)">Подтвердить</mu-button>
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
        name: "Owner_auto_edit",
        data() {
            return {
                auto: "",
                alert_dialog: false,
                alert_text: "",
            }
        },
        created() {
            this.auto = this.$route.query.current_auto
        },
        methods: {
            goto_owner_autos() {
                this.$router.push({name: "owner_autos_rout"})
            },
            conf_auto_edit(id) {
                var href = "http://127.0.0.1:8000/owner_auto_edit/" + id + "/"
                $.ajax({
                    url: href,
                    type: "POST",
                    data: {
                        id: this.auto.id,
                        number: this.auto.number,
                        brand: this.auto.brand,
                        model: this.auto.model,
                        year: this.auto.year,
                        tech_passport: this.auto.tech_passport
                    },
                    success: (response) => {
                        this.$router.push({name: "owner_autos_rout", query: {"outer_alert": "Данные успешно отредактированы"}})
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