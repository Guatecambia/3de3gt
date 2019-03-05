import Vue from 'vue'
import Vuex from 'vuex'
import {HTTP} from '../http-constants'
import router from './router'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'api/token/',
      refreshJWT: 'api/token/refresh/'
    },
    auth: localStorage.getItem('as')
  },
  mutations: {
    updateToken(state, newToken){
      localStorage.setItem('t', newToken);
      state.jwt = newToken;
      localStorage.setItem('as', true);
    },
    removeToken(state){
      localStorage.removeItem('t');
      state.jwt = null;
      localStorage.removeItem('as');
      state.auth = false;
    }
  },
  actions: {
    obtainToken(context, userData){
      const payload = {
        username: userData.username,
        password: userData.password
      }
      HTTP.post(this.state.endpoints.obtainJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token);
          })
        .catch((error)=>{
            this.commit('removeToken');
            console.log(error);
            alert("usuario o contraseña incorrecta");
          })
    },
    nullSession() {
      this.commit('removeToken');
      router.push('3de3-login');
    }
  },
  getters: {
    isAuth(state) {
      return state.auth;
    }
  }
})
