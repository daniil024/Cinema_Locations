import Vue from 'vue'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router/index'
import Vuelidate from 'vuelidate'
import store from './vuex'


// Vue.use section ...
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(router)
Vue.use(Vuelidate)

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  axios,
});
