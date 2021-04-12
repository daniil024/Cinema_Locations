<template>
  <b-form @submit.prevent="login">
    <div class="form-group">
      <label for="username">Логин:</label>
      <b-input
        v-model="form.username"
        type="text"
        id="username"
        placeholder="Логин..."
      ></b-input>
    </div>
    <div class="form-group">
      <label for="password">Пароль:</label>
      <b-input
        v-model="form.password"
        type="password"
        id="password"
        placeholder="Пароль..."
      ></b-input>
    </div>
    <b-button variant="primary" type="submit">Войти</b-button>
    <p class="mt-3">
      Ещё не зарегистрированы?
      <router-link to="/auth/signup">Регистрация</router-link>
    </p>
  </b-form>
</template>
<script>
import { mapGetters } from "vuex";
import authRequest from "@/mixins/authRequest";
export default {
  name: "SignInForm",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  mixins: [authRequest],
  methods: {
    async login() {
      // логика авторизации
      try {
        const response = await this.authRequest("api/auth/token/", this.form);
        // авторизуем юзера
        this.$store.dispatch("token", response.token);
        this.$store.dispatch("user", response.user);

        this.setLogined(response.token);
        this.$router.push("/LK");
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
    setLogined(token) {
      // сохраняем токен
      localStorage.setItem("token", token);
    },
  },
};
</script>