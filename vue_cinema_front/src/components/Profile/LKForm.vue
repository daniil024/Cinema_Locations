<template>
  <div class="w-75 mx-auto">
    <h2 class="w-50 mx-left">Личный кабинет</h2>
    <b-breadcrumb class="w-100 mx-left" :items="refs"></b-breadcrumb>
    <h4 class="w-50 mx-left" style="margin-top: 10px">Редактировать профиль</h4>
    <b-form
      class="w-75 mx-auto"
      style="margin-top: 40px"
      @submit.prevent="edit"
    >
      <div class="form-group w-75 mx-auto">
        <label for="email">E-mail:</label>
        <b-input
          v-model="form.email"
          type="text"
          id="email"
          placeholder="E-mail..."
        ></b-input>
      </div>
      <div class="form-group w-75 mx-auto">
        <label for="newPassword">Новый пароль:</label>
        <b-input
          v-model="form.newPassword"
          type="password"
          id="newPassword"
          placeholder="Пароль..."
        ></b-input>
        <b-button variant="primary" style="margin-top: 25px" type="submit"
          >Изменить</b-button
        >
      </div>
    </b-form>

    <div style="margin-top: 100px;">
      <h4 style="display:inline-block" class="w-50 mx-left">Мои локации</h4>
      <router-link to="/mylocations" style="display:inline-block; float:right">Посмотреть все</router-link>
    </div>
    <div v-if="items[0]" style="margin-top: 20px; display: flex" class="w-100 mx-left">
      <div class="card" style="width: 18rem; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">{{ items[0].name }}</h5>
          <p class="card-text">
            {{ items[0].description }}
          </p>
          <a href="#" class="btn btn-primary">Редактировать</a>
        </div>
      </div>

      <div v-if="items[1]"
        class="card"
        style="width: 18rem; margin-left: 45px; display: inline-block"
      >
        <div class="card-body">
          <h5 class="card-title">{{items[1].name}}</h5>
          <p class="card-text">
            {{ items[1].description }}
          </p>
          <a href="#" class="btn btn-primary">Редактировать</a>
        </div>
      </div>

      <div v-if="items[2]"
        class="card"
        style="width: 18rem; margin-left: 45px; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">{{items[2].name}}</h5>
          <p class="card-text">
            {{ items[2].description }}
          </p>
          <a href="#" class="btn btn-primary">Редактировать</a>
        </div>
      </div>
    </div>

    <div style="text-align:center; margin-top:30px;">
    <b-button to="/newservice" variant="primary" style="margin-top: 25px; text-align: center " type="submit">Добавить локацию</b-button>
    </div>

  </div>
</template>
<script>
import { mapGetters } from "vuex";
import editRequest from "@/mixins/editRequest";
import searchRequest from "@/mixins/searchRequest";
export default {
  name: "LK",
  data() {
    return {
      form: {
        email: "",
        newPassword: "",
      },
      items:[],
      refs: [
        {
          text: "Home",
          href: "#",
        },
        {
          text: "Search",
          href: "#",
        },
        {
          text: "Profile",
          active: true,
        },
      ],
    };
  },
  mixins: [editRequest, searchRequest],
  methods: {
    async edit() {
      // логика авторизации
      try {
        await this.editRequest(
          "api/managers/update/"+localStorage.iduser,
          this.form
        );
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
    async fillform() {
      this.form.email = this.user.email;
    },
  },
  async beforeMount() {
    this.fillform();
    var path = "api/service/all?user=" + localStorage.iduser;
    const response = await this.searchRequest(path);
    this.items = response;
  },
  computed: {
    ...mapGetters(["user"]),
  },
};
</script>