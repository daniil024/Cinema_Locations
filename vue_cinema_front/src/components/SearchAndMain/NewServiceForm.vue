<template>
  <div class="w-75 mx-auto">
    <h2 style="margin-bottom: 20px">Новая локация</h2>
    <table class="w-75 mx-left">
      <tbody>
        <h5>Название</h5>
        <b-form-input
          v-model="form.title"
          placeholder="Введите название локации..."
        ></b-form-input>
      </tbody>
      <tbody>
        <h5>Опишите локацию</h5>
        <b-form-textarea
          v-model="form.description"
          placeholder="Опишите локацию, обозначьте ее особенности..."
          rows="8"
        ></b-form-textarea>
      </tbody>
      <tbody>
        <h5>Адрес локации</h5>
        <b-form-input
          v-model="form.address"
          placeholder="Номер телефона, почта..."
        ></b-form-input>
      </tbody>
      <tbody>
        <h5>Как с вами связаться</h5>
        <b-form-input
          v-model="form.contacts"
          placeholder="Номер телефона, почта..."
        ></b-form-input>
      </tbody>
      <tbody>
        <h5>Бюджет</h5>
        <b-form-input
          v-model="form.price"
          placeholder="Сколько стоит аренда/покупка..."
        ></b-form-input>
      </tbody>
      <tbody>
        <h5>Фото</h5>
        <b-form-file
          v-on:change="handleFileUpload"
          style="display: block; color: transparent"
          class="mt-3"
          multiple
          plain
        ></b-form-file>
        <label style="display: block; font-size: 9pt"
          >*Вы можете загрузить до 10 файлов</label
        >
        <div v-if="form.imgNames.length !== 0">
          <div
            v-for="(image, i) in form.imgNames"
            :key="i"
            class="file-listing"
          >
            {{ image.name }}
            <span class="remove-file" v-on:click="removeFile(i)">Remove</span>
          </div>
        </div>
      </tbody>
    </table>

    <b-button
      variant="primary"
      style="margin-top: 50px"
      type="submit"
      @click="add()"
      >Создать</b-button
    >
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import createService from "@/mixins/createService";

export default {
  name: "NewService",
  data() {
    return {
      form: {
        title: "",
        price: "",
        address: "",
        contacts: "",
        description: "",
        images: [],
        imgNames: [],
        link: "Локация была создана с помощью данного сервиса!",
      },
    };
  },
  mixins: [createService],
  methods: {
    async add() {
      try {
        const response = await this.createService("api/service/new", {
          "user":this.user.id, "name":this.form.title, "description":this.form.description, 
          "price":this.form.price, "contacts": this.form.contacts, "address":this.form.address,
          "photo1": this.form.images[0], "photo2": this.form.images[1], "photo3": this.form.images[2],
          "photo4": this.form.images[3], "photo5": this.form.images[4], "photo6": this.form.images[5],
          "photo7": this.form.images[6], "photo8": this.form.images[7], "photo9": this.form.images[8],
          "photo10": this.form.images[9],
        });
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
      
      this.form.images = [];
      this.form.imgNames = [];
      this.$router.push("/lk");
    },
    handleFileUpload(event) {
      this.form.imgNames.push(
        event.target.files[event.target.files.length - 1]
      );

      const fileReader = new FileReader();
      fileReader.addEventListener("load", () => {
        this.form.images.push(fileReader.result);
      });
      fileReader.readAsDataURL(
        event.target.files[event.target.files.length - 1]
      );
    },
    removeFile(key) {
      this.form.imgNames.splice(key, 1);
      this.form.images.splice(key, 1);
    },
  },
  computed: {
    ...mapGetters(["user"]),
    ...mapGetters(["token"]),
  },
};
</script>

<style scoped>
table tbody {
  border-top: 15px solid white;
}

span.remove-file {
  color: red;
  cursor: pointer;
  float: right;
}
</style>