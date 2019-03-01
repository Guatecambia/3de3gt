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
    },
    {
      path: '/3de3-login',
      name: 'login',
      component: () => import('./views/login.vue')
    },
    {
      path: '/3de3-admin',
      name: 'admin',
      component: () => import('./views/admin.vue')
    },
    {
      path: '/3de3-admin/partidos',
      name: 'partidos',
      component: () => import('./views/partidos.vue')
    },
    {
      path: '/3de3-admin/distritos',
      name: 'distritos',
      component: () => import('./views/distritos.vue')
    },
    {
      path: '/3de3-admin/distrito/:id',
      name: 'distrito-single',
      component: () => import('./views/distritoSingle.vue')
    },
    {
      path: '/3de3-admin/distrito',
      name: 'distrito-single-new',
      component: () => import('./views/distritoSingle.vue')
    },    
    {
      path: '/3de3-admin/municipios',
      name: 'municipios',
      component: () => import('./views/municipios.vue')
    },
    {
      path: '/3de3-admin/ingresos',
      name: 'ingresos',
      component: () => import('./views/ingresos.vue')
    },
    {
      path: '/3de3-admin/ingreso/:id',
      name: 'ingreso-single-edit',
      component: () => import('./views/ingresoSingle.vue')
    },
    {
      path: '/3de3-admin/candidatos',
      name: 'candidatos',
      component: () => import('./views/candidatos.vue')
    },
    {
      path: '/3de3-admin/candidato/:id',
      name: 'candidato-single-edit',
      component: () => import('./views/candidatoSingle.vue')
    },
    {
      path: '/3de3-admin/candidato',
      name: 'candidato-single-new',
      component: () => import('./views/candidatoSingle.vue')
    },
    {
      path: '/3de3-admin/estadisticas',
      name: 'estadisticas-backend',
      component: () => import('./views/estadisticasBackend.vue')
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
