<template>

  <b-form @submit.prevent="register">
<h2 style="text-align:center">Регистрация</h2>
    <!-- <p v-if="err">{{ err }}</p> -->
  <div class="form-group">
       <label class="control-label" for="firstname">Имя:</label>
       <b-input v-model="form.firstname" type="text" id="firstname" placeholder="Имя..."></b-input>
     </div>
  <div class="form-group">
       <label class="control-label" for="lastname">Фамилия:</label>
       <b-input v-model="form.lastname" type="text" id="lastname" placeholder="Фамилия..."></b-input>
     </div>

    <div class="form-group required">
      <label class="control-label" for="username">Логин:</label>
      <b-input v-model="form.username" type="text" id="username" placeholder="Логин..."/>

      <p><small class="text-muted">Минимальная длина логина 5 символов</small></p>
    </div>

    <div class="form-group required">
       <label class="control-label" for="email">E-mail:</label>
       <b-input v-model="form.email" type="text" id="email" placeholder="e-mail..."></b-input>
     </div>

    <div class="form-group required">
      <label class="control-label" for="phone">Номер телефона:</label>
      <b-input
        v-model="form.phone"
        type="text"
        id="phone"
        v-imask="phoneNumberMask"
        placeholder="+7(900)000-00-00"
        @keypress="isNumber"
        @accept="onAccept"
        @complete="onComplete"
        maxlength="20"
      />

      <p><small class="text-muted">Введите номер в формате: +7(921)123-45-67</small></p>
    </div>
    
    <div class="form-group required">
      <label class="control-label" for="password">Пароль:</label>
      <b-input v-model="form.password" type="password" id="password" placeholder="Пароль..."></b-input>
      <p><small class="text-muted">Минимальная длина пароля 8 символов</small></p>
    </div>

    <div class="form-group required">
      <label class="control-label" for="repeatPassword">Повторите пароль:</label>
      <b-input v-model="form.repeatPassword" type="password" id="repeatPassword" placeholder="Повторите пароль..."/>
      </div>

    <p class="text-danger" v-if="!$v.form.password.minLength">Длина пароля меньше 8 символов</p>
    <p class="text-danger" v-if="isPasswordTheSame">Введённые пароли не совпадают</p>
    <b-button variant="primary" type="submit" :disabled="formValid">Регистрация</b-button>

    <p class="mt-2"><small class="text-muted">Все поля отмеченные <span class="text-danger">*</span> 
    обязательны для заполнения.</small></p>
    <p class="mt-3">Уже есть аккаунт? <router-link to="/auth/signin/">Вход</router-link></p>
  </b-form>
</template>
<script>

import { required, minLength, sameAs } from 'vuelidate/lib/validators'
import { IMaskDirective } from 'vue-imask'
import authRequest from '@/mixins/authRequest'
import editRequest from '@/mixins/editRequest'

export default {
  name: "SignUpForm",
  data () {
    return {
      form: {
        username: "",
        password: "",
        email: "",
        firstname: "",
        lastname: "",
        repeatPassword: "",
        phone: "",
        managerOrProducer: "",
      },
      userPhone: "",
      managerOrProducerOptions: [
       { text: 'Выберите...', value: '', disabled: true, selected: true },
       { text: 'Продюсер', value: 'producer' },
       { text: 'Менеджер', value: 'manager' }
     ],
      phoneNumberMask: {
        mask: '+0(000)000-00-00',
        lazy: true
      },
      err: ''
    }
  },
  validations: {
    form: {
      username: {
        required,
        minLength: minLength(5)
      },
      email:{
          required
      },
      password: {
        required,
        minLength: minLength(8)
      },
      repeatPassword: {
        required,
        sameAs: sameAs('password')
      },
      phone: {
        required
      },
      // managerOrProducer: {
      //   required
      // }
    }
  },
  computed: {
    formValid () {
      return this.$v.$invalid
    },
    isPasswordTheSame () {
      const form = this.$v.form
      return form.password.required 
        && form.repeatPassword.required 
        && !form.repeatPassword.sameAs
    }
  },
  mixins: [ authRequest, editRequest ],
  methods: {
    async register () {
      // логика регистрации
      try {
        const response = await this.authRequest('api/auth/users/', this.form);
        // const token = await this.authRequest('api/auth/token/', 
        //   {"username":this.form.username, "password":this.form.password});
        // console.log(token.token);
        // console.log(response.id);
        // // wait until the promise returns us a value
        // let resultToken = await token; 
        // this.axios.post('http://localhost:8000/api/managers/new', 
        //   { headers: {Authorization:`Token ${resultToken.token}`}}, {user:response.id, phone:this.form.phone})
        // .then(response => {console.log(response.data.phone)})
        // .catch(err => { console.error(err) });
        this.$store.dispatch('user', response);
        this.$router.push('/auth/signin');
      } catch (e) {
        console.error('AN API ERROR', e)
        this.err = e
      }
    },
    onAccept (e) {
      const maskRef = e.detail
      this.form.phone = maskRef.value
    },
    onComplete (e) {
      const maskRef = e.detail
      this.userPhone = maskRef.unmaskedValue
    },
    isNumber (e) {
      const regex = /[0-9]/
      if (!regex.test(e.key)) {
        e.returnValue = false;
        if (e.preventDefault) e.preventDefault();
      }
    }
  },
  directives: {
    imask: IMaskDirective
  }
};
</script>
<style>
.form-group.required .control-label:after {
  content:" *";
  color:red;
}
</style>