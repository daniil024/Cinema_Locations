import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/views/auth/SignIn'
import SignUp from '@/views/auth/SignUp'
import ForgotDone from '@/views/auth/ForgotDone'
import ForgotConfirm from '@/views/auth/ForgotConfirm'
import ForgotComplete from '@/views/auth/ForgotComplete'
import LK from '@/views/MainPages/LK'
import Search from '@/views/MainPages/Search'
import Service from '@/views/MainPages/Service'
import NewService from '@/views/MainPages/NewService'
import MyServices from '@/views/MainPages/MyServices'
import EditServices from '@/views/MainPages/EditService'
import Forgot from '@/views/auth/Forgot'
import lodash from 'lodash'
import VueLodash from 'vue-lodash'
 
Vue.use(VueLodash, { name: 'custom' , lodash: lodash })
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Search',
      component: Search,
    },
    {
      path: '/auth/signin/',
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
    {
      path: '/newService',
      name: 'NewService',
      component: NewService,
    },
    {
      path: '/forgot',
      name: 'Forgot',
      component: Forgot,
    },
    {
      path: '/mylocations',
      name: 'MyServices',
      component: MyServices,
    },
    {
      path: '/editservice/:id',
      name: 'EditServices',
      component: EditServices,
    },
    {
      path: '/resetdone',
      name: 'ResetPasswordDone',
      component: ForgotDone,
    },
    {
      path: '/resetcomplete',
      name: 'ResetPasswordComplete',
      component: ForgotComplete,
    },
    {
      path: '/resetconfirm',
      name: 'ResetPasswordConfirm',
      component: ForgotConfirm,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
});
