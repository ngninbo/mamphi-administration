import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

// Import Components
import StudieDescription from './components/StudieDescription.vue'
import InformedConsent from './components/InformedConsent.vue'
import CenterList from './components/CenterList.vue'
import RandomWeek from './components/RandomWeek.vue'
import RandomWeek2 from './components/RandomWeek2.vue'
import MonitoringPlan from './components/MonitoringPlan.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        { path: '/description', component: StudieDescription },
        { path: '/center', component: CenterList },
        { path: '/consent', component: InformedConsent },
        { path: '/firstrandomization', component: RandomWeek },
        { path: '/secondrandomization', component: RandomWeek2 },
        { path: '/monitorplan', component: MonitoringPlan },
        { path: '*', redirect: '/description' },
    ]
});

new Vue({
    render: h => h(App),
    router,
}).$mount('#app')