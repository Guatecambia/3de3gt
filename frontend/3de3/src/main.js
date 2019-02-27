import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import Vuelidate from 'vuelidate'
import VueClipboard from 'vue-clipboard2'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.use(BootstrapVue);
VueClipboard.config.autoSetContainer = true 
Vue.use(VueClipboard);
Vue.use(Vuelidate);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
