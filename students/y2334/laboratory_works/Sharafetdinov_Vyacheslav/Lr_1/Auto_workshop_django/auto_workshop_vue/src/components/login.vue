<template>
    <mu-container>
    <vue-headful title="Авторизация"/>
        <div class="form-pannel" style="width: 40%">
            <mu-row gutter>
                <mu-col span=2 class="form-pannel-cell">
                    <label class="form-label"><strong>Логин:</strong></label>
                </mu-col>
                <mu-col span=10 class="form-pannel-cell">
                    <input class="form-input" v-model="login" type="text"/>
                </mu-col>
            </mu-row>
            <mu-row gutter>
                <mu-col span=2 class="form-pannel-cell">
                    <label class="form-label"><strong>Пароль:</strong></label>
                </mu-col>
                <mu-col span=10 class="form-pannel-cell">
                    <input class="form-input" v-model="password" type="password"/>
                </mu-col>
            </mu-row>
            <div style="margin: 5% auto 0">
                <mu-button class="red-button" @click="goto_main">Отмена</mu-button>
                <mu-button class="blue-button" @click="conf_login">Войти</mu-button>
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
        name: "Login",
        data() {
	    	return {
		    	login: "",
		    	password: "",
                alert_dialog: false,
                alert_text: "",
	    	}
	    },
        methods: {
            goto_main() {
                this.$router.push({name: "main_rout"})
            },
            conf_login() {
                if (this.login && this.password) {
                    $.ajax({
                        url: "http://127.0.0.1:8000/auth/token/login/",
                        type: "POST",
                        data: {
                            username: this.login,
                            password: this.password
                        },
                        success: (response) => {
                            sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                            this.$router.push({name: "main_rout"})
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