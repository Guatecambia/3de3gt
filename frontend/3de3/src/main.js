import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import Vuelidate from 'vuelidate'
import VueClipboard from 'vue-clipboard2'
import App from './App.vue'
import router from './router'
import store from './store'
import VueAnalytics from 'vue-analytics'
import VuePaginate from 'vue-paginate'

Vue.config.productionTip = false
Vue.use(BootstrapVue);
VueClipboard.config.autoSetContainer = true 
Vue.use(VueClipboard);
Vue.use(Vuelidate);
Vue.use(VueAnalytics, {
    id: 'UA-134357063-1',
    debug: {
      sendHitTask: process.env.NODE_ENV === 'production'
    },
    router
})
Vue.use(VuePaginate)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
