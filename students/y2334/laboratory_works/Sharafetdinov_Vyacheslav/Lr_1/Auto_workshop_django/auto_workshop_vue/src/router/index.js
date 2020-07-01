import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/main'
import Login from '@/components/login'
import Owner_registration from '@/components/owner_registration'
import Owner_autos from '@/components/owner_autos'
import Owner_auto_add from '@/components/owner_auto_add'
import Owner_auto_edit from '@/components/owner_auto_edit'
import Owner_applications from '@/components/owner_applications'
import Owner_application_add from '@/components/Owner_application_add'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'main_rout',
            component: Main
        },
        {
            path: '/login',
            name: 'login_rout',
            component: Login
        },
        {
            path: '/owner_registration',
            name: 'owner_registration_rout',
            component: Owner_registration
        },
        {
            path: '/my_autos',
            name: 'owner_autos_rout',
            component: Owner_autos
        },
        {
            path: '/my_autos/add',
            name: 'owner_auto_add_rout',
            component: Owner_auto_add
        },
        {
            path: '/my_autos/edit',
            name: 'owner_auto_edit_rout',
            component: Owner_auto_edit
        },
        {
            path: '/my_applications',
            name: 'owner_applications_rout',
            component: Owner_applications
        },
        {
            path: '/my_applications/add',
            name: 'owner_application_add_rout',
            component: Owner_application_add
        },
    ]
})
