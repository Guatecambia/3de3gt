import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import store from './store.js'


Vue.use(Router)

let router = new Router({
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
      path: '/estadisticas',
      name: 'estadisticas',
      component: () => import('./views/Estadisticas.vue')
    },
    {
      path: '/3de3-login',
      name: 'login',
      component: () => import('./views/login.vue'),
      meta: {
        authScreen: true
      }
    },
    {
      path: '/3de3-logout',
      name: 'logout',
      component: () => import('./views/logout.vue'),
    },
    {
      path: '/3de3-admin',
      name: 'admin',
      component: () => import('./views/admin.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/partidos',
      name: 'partidos',
      component: () => import('./views/partidos.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/partido/:id',
      name: 'partido-single',
      component: () => import('./views/partidoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/partido',
      name: 'partido-single-new',
      component: () => import('./views/partidoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/distritos',
      name: 'distritos',
      component: () => import('./views/distritos.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/distrito/:id',
      name: 'distrito-single',
      component: () => import('./views/distritoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/distrito',
      name: 'distrito-single-new',
      component: () => import('./views/distritoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },    
    {
      path: '/3de3-admin/municipios',
      name: 'municipios',
      component: () => import('./views/municipios.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/muni/:id',
      name: 'muni-single-edit',
      component: () => import('./views/municipioSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/muni',
      name: 'muni-single-new',
      component: () => import('./views/municipioSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/ingresos',
      name: 'ingresos',
      component: () => import('./views/ingresos.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/ingreso/:id',
      name: 'ingreso-single-edit',
      component: () => import('./views/ingresoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/candidatos',
      name: 'candidatos',
      component: () => import('./views/candidatos.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/candidato/:id',
      name: 'candidato-single-edit',
      component: () => import('./views/candidatoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/candidato',
      name: 'candidato-single-new',
      component: () => import('./views/candidatoSingle.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/3de3-admin/estadisticas',
      name: 'estadisticas-backend',
      component: () => import('./views/estadisticasBackend.vue'),
      meta: {
        requiresAuth: true
      }
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
  },
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuth) {
      return next()
    }
    else {
      return next('/3de3-login')
    }
  } 
  else {
    if(to.matched.some(record => record.meta.authScreen)) {
      if (store.getters.isAuth) {
        return next('/3de3-admin')
      }
    }
    return next() 
  }
})

router.beforeResolve((to, from, next) => {
  if (to.name) {
    NProgress.start()
  }
  next()
})

router.afterEach((to, from) => {
  NProgress.done()
})

export default router
