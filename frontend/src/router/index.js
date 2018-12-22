import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/components/About'
import Home from '@/components/Home'
import NotFound from '@/components/NotFound'

// const routerOptions = [
//   { path: '/', component: 'Home' },
//   { path: '/about', component: 'About' },
//   { path: '*', component: 'NotFound' }
// ]
// const routes = routerOptions.map(route => {
//   return {
//     ...route,
//     component: () => import(`@/components/${route.component}.vue`)
//   }
// })
// Vue.use(Router)

// export default new Router({
//   routes,
//   mode: 'history'
// })

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
