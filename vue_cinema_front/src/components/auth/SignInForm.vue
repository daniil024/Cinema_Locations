<template>
  <b-form @submit.prevent="login">
<h2 style="text-align:center">Вход</h2>
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
    <div>
      <p style="display:inline;" class="mt-3">
        Ещё не зарегистрированы?
        <router-link to="/auth/signup">Регистрация</router-link>
      </p>

      <p style="display:inline; float:right" class="forgot-password text-right">
        <a href="http://127.0.0.1:8000/api/reset_password/">Забыли пароль?</a>
      </p>

    </div>
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
        this.setLogined(response.token, response.user.id);
        this.$router.push("/LK");
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
    setLogined(token, iduser) {
      // сохраняем токен
      localStorage.setItem("token", token);
      localStorage.setItem("iduser", iduser);
    },
  },
};
</script>