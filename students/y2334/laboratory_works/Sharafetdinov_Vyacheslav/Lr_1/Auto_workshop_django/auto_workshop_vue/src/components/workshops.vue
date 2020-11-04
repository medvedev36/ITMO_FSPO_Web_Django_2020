<template>
    <mu-container>
        <mu-row>
            <h1 class="main-font" style="margin: 3% auto 0">Наши автомастерские</h1>
        </mu-row>
        <mu-row gutter v-for="workshop in workshops">
        <div class="info-pannel" style="width: 70%">
            <mu-col>
                <mu-row>
                    <span class="main-font" style="font-size: 20pt; text-align: left">
                        <u>Мастерская №{{workshop.number}}</u>
                    </span>
                </mu-row>
                <mu-row>
                    <span class="main-font" style="font-size: 15pt; text-align: left">{{workshop.address}}</span>
                </mu-row>
            </mu-col>
            <mu-col span=5 style="margin-top: 5%">
                <mu-expansion-panel>
                    <div slot="header">Обслуживаемые марки:</div>
                    <mu-row v-for="brands in workshop.brands">
                        <span class="main-font" style="font-size: 12pt; text-align: left">{{brands.brand}}</span>
                    </mu-row>
                </mu-expansion-panel>
            </mu-col>
        </div>
        </mu-row>
    </mu-container>
</template>


<script>
    import $ from 'jquery'

    export default {
        name: "Workshops",
        data() {
            return {
                workshops: "",
            }
        },
        mounted() {
            this.get_workshops()
        },
        methods: {
             get_workshops() {
                $.ajax({
                    url: "http://127.0.0.1:8000/workshops_brands/",
                    type: "GET",
                    success: (response) => {
                        this.workshops = response.data.data
                    },
                    error: (response) => {
                        this.$emit("send_alert", "Ошибка на стороне сервера")
                    }
                })
            },
        },
    }
</script>


<style lang="scss" scoped>
    @import '@/assets/styles.scss';
</style>