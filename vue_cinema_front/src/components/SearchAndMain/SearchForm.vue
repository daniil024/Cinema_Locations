<template>
  <div class="w-75 mx-auto">
    <b-form @submit.prevent="find">
      <div class="input-group mb-3">
        <input
          v-model="inputform.inputsearch"
          type="text"
          class="form-control"
          placeholder="Поиск..."
        />
        <div class="input-group-append">
          <button @click.prevent="find" type="submit" class="btn btn-primary">
            Поиск
          </button>
        </div>
      </div>
      <div>
        <div style="display: inline-block">
          <p>Введите цену:</p>
          <input
            v-model="inputform.priceMin"
            type="text"
            style="width: 80px; display: inline-block"
            class="form-control"
            placeholder="От"
          />
          &#8212;
          <input
            v-model="inputform.priceMax"
            type="text"
            style="width: 80px; display: inline-block"
            class="form-control"
            placeholder="До"
          />
        </div>
        <div style="margin-left: 30px; display: inline-block">
          <p>Введите адрес:</p>
          <input
            v-model="inputform.address"
            type="text"
            class="form-control"
            placeholder="Адрес"
          />
        </div>
      </div>
      <hr color="black" />
    </b-form>
    <h4 class="text-center" style="margin-bottom: 40px">
      Всего найдено {{ inputform.numberOfServices }} объявлений
    </h4>

    <div v-for="item in collection" :key="item.id">
      <!-- <div v-for="item in servicesfill.items" :key="item.id"> -->
      <div style="display: inline-block">
        <h5>
          <a :href="'/service/' + item.id">{{ item.name }}</a>
          <!-- <a :href="item.link">{{ item.name }}</a> -->
        </h5>
        <p
          style="
            width: 450px;
            white-space: nowrap;
            overflow: hidden;
            padding: 0px;
            text-overflow: ellipsis;
          "
        >
          {{ item.description }}
        </p>
      </div>
      <div style="font-size: 20px; display: inline-block; float: right">
        {{ item.price }}₽
      </div>
      <hr style="margin-top: -5px" />
    </div>

    <div class="text-center center-block">
      <div class="btn-toolbar">
        <div class="btn-group">
          <button
            class="btn btn-primary center-block"
            v-for="p in servicesfill.pagination.pages"
            :key="p"
            @click.prevent="setPage(p)"
          >
            {{ p }}
          </button>
        </div>
      </div>
    </div>
    <!-- <div style="margin-top:40px; text-align: center">
      <b-button variant="primary" type="submit">Следующие результаты</b-button>
    </div> -->
  </div>
</template>
<script>
import searchRequest from "@/mixins/searchRequest";
export default {
  name: "Search",
  data() {
    return {
      inputform: {
        inputsearch: "",
        priceMin: "",
        priceMax: "",
        address: "",
        numberOfServices: 0,
      },
      servicesfill: {
        items: [],
        perPage: 9,
        pagination: {},
      },
    };
  },
  computed: {
    collection() {
      return this.paginate(this.servicesfill.items);
    },
  },
  mixins: [searchRequest],
  methods: {
    setPage(p) {
      this.servicesfill.pagination = this.paginator(
        this.inputform.numberOfServices,
        p
      );
    },
    paginate(data) {
      return _.slice(
        data,
        this.servicesfill.pagination.startIndex,
        this.servicesfill.pagination.endIndex + 1
      );
    },
    paginator(totalItems, currentPage) {
      var startIndex = (currentPage - 1) * this.servicesfill.perPage,
        endIndex = Math.min(
          startIndex + this.servicesfill.perPage - 1,
          totalItems - 1
        );

      return {
        currentPage: currentPage,
        startIndex: startIndex,
        endIndex: endIndex,
        pages: _.range(
          1,
          Math.ceil(totalItems / this.servicesfill.perPage) + 1
        ),
      };
    },
    async find() {
      try {
        var path = "api/service/all";
        if (
          this.inputform.priceMin !== "" ||
          this.inputform.priceMax !== "" ||
          this.inputform.address !== "" ||
          this.inputform.inputsearch
        ) {
          path += "?";
          if (this.inputform.priceMin !== "") {
            path += "price_min=" + this.inputform.priceMin + "&";
          }
          if (this.inputform.priceMax !== "") {
            path += "price_max=" + this.inputform.priceMax + "&";
          }
          if (this.inputform.address !== "") {
            path += "address=" + this.inputform.address + "&";
          }
          if (this.inputform.inputsearch !== "") {
            path += "name=" + this.inputform.inputsearch + "&";
          }
        }
        const response = await this.searchRequest(path);
        this.inputform.numberOfServices = response.length;
        this.servicesfill.items = response;
        this.setPage(1);
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
  },
  mounted() {
    this.find();
  },
};
</script>