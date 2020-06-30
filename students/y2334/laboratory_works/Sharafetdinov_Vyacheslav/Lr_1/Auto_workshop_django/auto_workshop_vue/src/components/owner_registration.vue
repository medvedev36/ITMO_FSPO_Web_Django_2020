<template>
    <mu-container>
    <vue-headful title="Регистрация"/>
        <div class="form-pannel" style="width: 46%">
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Логин:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="login" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Пароль:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="password" type="password"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label"><strong>Подтвердите пароль:</strong></label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="password_check" type="password"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label">
                        <em>Имя:</em>
                    </label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="first_name" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label">
                        <em>Фамилия:</em>
                    </label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="last_name" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label">
                        <em>Отчество:</em>
                    </label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="patronymic" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label">
                        <em>Электронная почта:</em>
                    </label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="email" type="email"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=4 class="form-pannel-cell">
                    <label class="form-label">
                        <em>Номер телефона:</em>
                    </label>
                </mu-col>
                <mu-col span=8 class="form-pannel-cell">
                    <input class="form-input" v-model="phone" type="tel"/>
                </mu-col>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="goto_main">Отмена</mu-button>
                <mu-button class="blue-button" @click="conf_registration">Зарегистрироваться</mu-button>
            </div>
        </div>

        <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="alert_dialog">
            <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: #212121">{{alert_text}}</span>
            <div align="center" style="margin-top: 5%">
                <mu-button class="blue-button" slot="actions" @click="close_alert_dialog">Ок</mu-button>
            </div>
        </mu-dialog>

        <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="confirm_dialog">
            <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: #212121">
            Регистрация успешно пройдена!<br>
            Войдите в созданную запись, чтобы воспользоваться услугами сервиса</span>
            <div align="center" style="margin-top: 5%">
                <mu-button class="blue-button" slot="actions" @click="goto_main">Отмена</mu-button>
                <mu-button class="red-button" slot="actions" @click="goto_login">Войти</mu-button>
            </div>
        </mu-dialog>

    </mu-container>
</template>


<script>
    import $ from 'jquery'

    export default {
        name: "Owner_registration",
        data() {
            return {
                login: "",
                phone: "",
                email: "",
                password: "",
                password_check: "",
                first_name: "",
                last_name: "",
                patronymic: "",
                confirm_dialog: false,
                alert_dialog: false,
                alert_text: "",
            }
        },
        methods: {
            goto_main() {
                this.$router.push({name: "main_rout"})
            },
            goto_login() {
                this.$router.push({name: "login_rout"})
            },
            conf_registration() {
                if (this.login && this.password && this.password_check) {
                    if(this.password == this.password_check) {
                        $.ajax({
                            url: "http://127.0.0.1:8000/owner_registration/",
                            type: "POST",
                            data: {
                                username: this.login,
                                phone: this.phone,
                                email: this.email,
                                password: this.password,
                                first_name: this.first_name,
                                last_name: this.last_name,
                                patronymic: this.patronymic,
                            },
                            success: (response) => {
                                this.open_confirm_dialog()
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
                        this.alert_text = "Пароль не подтверждён!\nПроверьте введённые данные";
                        this.open_alert_dialog()
                    }
                }
                else {
                    this.alert_text = "Введите все необходимые поля формы";
                    this.open_alert_dialog()
                }
            },
            open_confirm_dialog() {
                this.confirm_dialog = true;
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