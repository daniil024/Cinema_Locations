<template>
  <b-form @submit.prevent="handleSubmit()">
    <div class="form-group">
      <label for="username">E-mail:</label>
      <b-input
        v-model="form.email"
        type="text"
        id="email"
        placeholder="E-mail..."
      ></b-input>
    </div>
    <b-button variant="primary" type="submit">Изменить пароль</b-button>
  </b-form>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "ForgotForm",
  data() {
    return {
      form: {
        email: "",
      },
    };
  },
  methods:{
    async handleSubmit(){
      
    }
  },
  
};
</script>