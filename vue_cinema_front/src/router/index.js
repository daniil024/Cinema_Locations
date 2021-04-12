import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/views/auth/SignIn'
import SignUp from '@/views/auth/SignUp'
import LK from '@/views/MainPages/LK'
import Search from '@/views/MainPages/Search'
import Service from '@/views/MainPages/Service'
import lodash from 'lodash'
import VueLodash from 'vue-lodash'
 
// name is optional
Vue.use(VueLodash, { name: 'custom' , lodash: lodash })
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
      path: '/auth/signin',
      name: 'SignIn',
      component: SignIn,
    },
    {
      path: '/auth/signup',
      name: 'SignUp',
      component: SignUp,
    },
    {
      path: '/lk',
      name: 'LK',
      component: LK,
    },
    {
      path: '/search',
      name: 'Search',
      component: Search,
    },
    {
      path: '/service/:id',
      name: 'Service',
      component: Service,
    },
  ],
});
