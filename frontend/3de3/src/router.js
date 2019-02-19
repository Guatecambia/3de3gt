import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/acerca-de',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import(/* webpackChunkName: "Faq" */ './views/Faq.vue')
    },
    {
      path: '/privacidad',
      name: 'privacy',
      component: () => import(/* webpackChunkName: "privacy" */ './views/Privacy.vue')
    },
  ],
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
      return {
        selector: to.hash
      }
    }
    else {
      if (savedPosition) {
        return savedPosition
      } 
      else {      
        return { x: 0, y: 0 }
      }
    }
  }
})
