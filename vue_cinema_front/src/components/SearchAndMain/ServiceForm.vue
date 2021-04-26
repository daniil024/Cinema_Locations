<template>
  <div class="w-75 mx-auto">
    <div style="border-bottom: 2px solid black">
      <div style="display: inline-block; border-bottom: 1px black">
        <h2>{{ form.title }}</h2>
      </div>
      <div style="font-size: 20px; display: inline-block; float: right">
        {{ form.price }}₽
      </div>
    </div>
    <p style="white-space: pre-line; margin-top: 50px">
      <span style="font-weight: bold">От пользователя: </span
      >{{ form.user.username }}
    </p>
    <p style="font-weight: bold">Контакты:</p>
    <p>{{ form.contacts }}</p>
    <p style="font-weight: bold">Описание:</p>
    <p>{{ form.description }}</p>
    <p style="font-weight: bold">Адрес:</p>
    <p>{{ form.address }}</p>
    <p style="font-weight: bold">Оригинальная ссылка:</p>
    <p>
      <span
        v-if='form.link==="Локация была создана с помощью данного сервиса!"'
        >{{ form.link }}</span
      >
      <a v-else :href="form.link">{{ form.link }}</a>
    </p>

    <b-carousel
      controls
      indicators
      img-width="300"
      img-height="300"
      style="margin-top: 100px"
    >
      <b-carousel-slide
        img-width="300"
        img-height="300"
        v-for="(photo, i) in form.photos"
        :key="i"
        :img-src="photo"
      >
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>
<script>
import searchRequest from "@/mixins/searchRequest";
export default {
  name: "Service",
  data() {
    return {
      form: {
        title: "",
        price: "",
        address: "",
        photos: [],
        description: "",
        contacts:"",
        link: "Локация была создана с помощью данного сервиса!",
        // manager: {
        //   id: 0,
        //   user: {
        //     username: "",
        //     email: "",
        //     first_name: "",
        //     last_name: "",
        //   },
        //   phone: "",
        // },
        user: {
             username: "",
             email: "",
             first_name: "",
             last_name: "",
           },
      },
    };
  },
  computed: {},
  mixins: [searchRequest],
  methods: {
    async find() {
      try {
        var id = window.location.href.split("/");
        const response = await this.searchRequest(
          "api/service/" + id[id.length - 1]
        );
        this.form.title = response.name;
        this.form.price = response.price;
        this.form.address = response.address;
        this.form.description = response.description;
        this.form.user = response.user;
        this.form.contacts = response.contacts;

        if(response.photo1!=="" && response.photo1!=null){
        this.form.photos.push(response.photo1)
        }
        if(response.photo2!=="" && response.photo2!=null){
        this.form.photos.push(response.photo2)
        }
        if(response.photo3!=="" && response.photo3!=null){
        this.form.photos.push(response.photo3)
        }
        if(response.photo4!=="" && response.photo4!=null){
        this.form.photos.push(response.photo4)
        }
        if(response.photo5!=="" && response.photo5!=null){
        this.form.photos.push(response.photo5)
        }
        if(response.photo6!=="" && response.photo6!=null){
        this.form.photos.push(response.photo6)
        }
        if(response.photo7!=="" && response.photo7!=null){
        this.form.photos.push(response.photo7)
        }
        if(response.photo8!=="" && response.photo8!=null){
        this.form.photos.push(response.photo8)
        }
        if(response.photo9!=="" && response.photo9!=null){
        this.form.photos.push(response.photo9)
        }
        if(response.photo10!=="" && response.photo10!=null){
        this.form.photos.push(response.photo10)
        }
        if (response.link !== undefined && response.link!=="" && response.link!==null)  {
          this.form.link = response.link;
        }
        if (response.photo_link !== undefined && response.photo_link !=="" && response.photo_link!==null) {
          this.form.photos = response.photo_link.split(" ");
        }
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
  },
  beforeMount() {
    this.find();
  },
};
</script>

<style scoped>
</style>