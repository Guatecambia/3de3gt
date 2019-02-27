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
      component: () => import('./views/About.vue')
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import('./views/Faq.vue')
    },
    {
      path: '/privacidad',
      name: 'privacy',
      component: () => import('./views/Privacy.vue')
    },
    {
      path: '/presenta',
      name: 'addyours',
      component: () => import('./views/AddYours.vue')
    }
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
