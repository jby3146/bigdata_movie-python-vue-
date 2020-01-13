
<template>
  <v-hover v-slot:default="{ hover }">
    <v-card class="pic" :elevation="hover ? 8 : 2" @click="onDetail">
      <v-img v-if="imgpath == ''" class="pic-image" src="../../img/NotPoster.jpg" max-width="500" max-height="300" />
      <v-img v-else class="pic-image" :src="imgpath" max-width="500" max-height="300" />
      <v-flex class="pic-caption rotate-in" text-center>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="pic-title font-weight-white movie_pasd">
              {{ title }}
            </v-list-item-title>
            <v-list-item-title class="pic-title font-weight-white movie_pas">
              {{ genresStr }}
            </v-list-item-title>
            <v-list-item-title class="pic-title font-weight-white movie_pa">
              {{ overview }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-card-text>
          <v-layout v-if="rating > 0" justify-center>
            <v-rating
              id="card_rating_btn_right"
              :value="rating"
              color="yellow"
              background-color="rgb(158,158,160)"
              half-increments
              dense
              readonly
            />
          </v-layout>
        </v-card-text>
      </v-flex>
      <v-dialog
        v-model="dialog"
        max-width="600"
      >
        <MovieDetailCard
          :id="id"
          :img="img"
          :title="title"
          :genres="genres"
          :rating="rating"
          :view-cnt="viewCnt"
          :imgpath="imgpath"
          :overview="overview"
          :companies_array="companies_array"
          :countries_array="countries_array"
          :runtime="runtime"
        />
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>
import MovieDetailCard from "./MovieDetailCard"
export default {
  components: {
    MovieDetailCard
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    },
    imgpath: {
      type: String,
      default: ""
    },
    overview: {
      type: String,
      default: ""
    },
    companies_array: {
      type: Array,
      default: () => new Array()
    },
    countries_array: {
      type: Array,
      default: () => new Array()
    },
    runtime: {
      type: Number,
      default: 0
    }
  },
  data () {
      return {
        dialog: false,
      }
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
  },
  methods: {
    onDetail: function() {
      this.dialog = !this.dialog
    },
  }
};
</script>

<style>

.movie_pa {
  padding-top: 10%;
}
.movie_pas {
  padding-top: 5px;
}
.movie_pasd {
  padding-top: 20%;
}

@media screen and (max-width: 370px) {
#card_rating_btn_right {
    display: none;
  }
}
</style>
