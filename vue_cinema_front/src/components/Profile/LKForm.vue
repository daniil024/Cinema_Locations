<template>
  <div class="w-75 mx-auto">
    <h2 class="w-50 mx-left">Личный кабинет</h2>
    <b-breadcrumb class="w-100 mx-left" :items="items"></b-breadcrumb>
    <h4 class="w-50 mx-left" style="margin-top: 10px">Редактировать профиль</h4>
    <b-form
      class="w-75 mx-auto"
      style="margin-top: 40px"
      @submit.prevent="edit"
    >
      <div class="form-group w-75 mx-auto">
        <label for="phone">Телефон:</label>
        <b-input
          v-model="form.phone"
          type="text"
          id="phone"
          placeholder="Телефон..."
        ></b-input>
      </div>
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

    <h4 style="margin-top: 50px" class="w-50 mx-left">Мои заказы</h4>
    <div style="margin-top: 20px; display: flex" class="w-100 mx-left">

      <div class="card" style="width: 18rem; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">{{title}}</h5>
          <p class="card-text">
            {{desc}}
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>

      
      <div class="card" style="width: 18rem; margin-left:45px; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>

      
      <div class="card" style="width: 18rem; margin-left:45px; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
      
    </div>

    <h4 style="margin-top: 50px" class="w-50 mx-left">Мои услуги</h4>
    <div style="margin-top: 20px; display: flex" class="w-100 mx-left">

      <div class="card" style="width: 18rem; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>

      
      <div class="card" style="width: 18rem; margin-left:45px; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>

      
      <div class="card" style="width: 18rem; margin-left:45px; display: inline-block">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
      
    </div>

  </div>
</template>
<script>
import {mapGetters} from 'vuex'
import editRequest from "@/mixins/editRequest";
export default {
  name: "LK",
  data() {
    return {
      form: {
        phone: "",
        email: "",
        newPassword: "",
      },
      title:"",
      desc:"",
      items: [
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
  mixins: [editRequest],
  methods: {
    async edit() {
      // логика авторизации
      try {
        const response = await this.editRequest(
          "api/managers/update/3",
          this.form
        );
        // авторизуем юзера
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
    async fillform() {
      // const response = this.axios
      //   .get(`http://localhost:8000/api/managers/3`, {
      //     headers: {
      //       'Authorization': `Token ${this.token}`,
      //     }
      //   })
      //   .then((response)=>{
      //     //this.form.phone=response.data.phone;
      //     this.form.email=response.data.user.email;
      //   })
      //   .catch((err) => {
      //     console.error(err);
      //   });
      this.form.email=this.user.email;
    },
  },
  beforeMount() {
    this.fillform();

    this.axios
        .get(`http://localhost:8000/api/service/6`, {
          headers: {
            'Authorization': `Token ${localStorage.token}`,
          }
        })
        .then((response)=>{
          this.title=response.data.name;
          this.desc=response.data.description;
        })
        .catch((err) => {
          console.error(err);
        });
  },
  computed:{
    ...mapGetters(['user'])
  }
};
</script>