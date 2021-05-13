<template>
  <div id="app" class="app-wrapper">
    <header class="bg-dark">
      <b-navbar class="w-75 mx-auto" type="dark" variant="dark">
        <b-navbar-brand>Cinema Locations</b-navbar-brand>
        <b-navbar-nav>
          <router-link class="nav-link" to="/">Главная</router-link>
          <router-link class="nav-link" to="/search">Поиск</router-link>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto" v-if="!token">
          <b-nav-form>
            <router-link class="nav-link" to="/auth/signup">Регистрация</router-link>
            <router-link class="nav-link" to="/auth/signin">Вход</router-link>
          </b-nav-form>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto" v-if="token">
          <b-nav-form>
            <a @click="logout()" class="nav-link">Выйти</a>
            <!-- <router-link @click="logout()" class="nav-link" to="/auth/signin">Выйти</router-link> -->
            <router-link title="Личный кабинет" style="margin-left:15px" to="/LK"><svg width="1.5em" height="2em" viewBox="0 0 16 16" class="bi bi-house-door-fill" fill="white" xmlns="http://www.w3.org/2000/svg">
              <path d="M6.5 10.995V14.5a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5h-4a.5.5 0 0 1-.5-.5V11c0-.25-.25-.5-.5-.5H7c-.25 0-.5.25-.5.495z"/>
              <path fill-rule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
            </svg> </router-link>
          </b-nav-form>
        </b-navbar-nav>

      </b-navbar>
    </header>
    <main class="container-fluid my-5">
      <router-view />
    </main>
    <footer>
      <b-jumbotron
        bg-variant="dark"
        text-variant="white"
        class="rounded-0 mb-0"
      >
        <div class="w-75 mx-auto">
          <div class="row">
            <div class="col-4 text-left">© Cinema Locations</div>
            <div class="col-4 text-center">Контакты</div>
            <div class="col-4 text-right">О нас</div>
          </div>
        </div>
      </b-jumbotron>
    </footer>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "App",
  data () {
    return {
      
    }
  },
  methods: {
      logout(){
        this.axios.get('http://127.0.0.1:8000/api/auth/logout',{headers: {'Authorization':`Token ${localStorage.token}`}}, this.user)
        .catch(err=>console.log(err));

        localStorage.removeItem("token");
        localStorage.removeItem("iduser");
        // localStorage.clear();
        this.$store.dispatch('token', null);
        this.$store.dispatch('user', null);
        this.$router.push("/auth/signin");
      },
  },
  computed:{
    ...mapGetters(['token']),
    ...mapGetters(['user'])
  }
};
</script>

<style>
.navbar,
.navbar-brand {
  font-size: 16pt;
}
header {
  height: 70px;
}
main {
  height: calc(100vh - 160px - 70px * 2);
  min-height: 600px;
}
footer {
  margin-top: 550px;
  font-size: 20pt;
}
footer .jumbotron {
  height: 160px;
}
</style>
