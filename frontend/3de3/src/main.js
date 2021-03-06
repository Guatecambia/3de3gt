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

new Vue({
  router,
  store,
	beforeCreate() {
		this.$store.commit('initStore');
	},
  render: h => h(App)
}).$mount('#app')
