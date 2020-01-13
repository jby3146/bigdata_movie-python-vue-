<template>
  <v-layout wrap>
    <v-flex v-for="card in movieListCardsSliced" :key="card.id" pa-2
            xs12
            sm6
            md6
            lg4
            xl3
    >
      <MovieListCard
        :id="card.id"
        :img="card.img"
        :title="card.title"
        :genres="card.genres"
        :rating="card.rating"
        :view-cnt="card.viewCnt"
        :imgpath="card.imgpath"
        :overview="card.overview"
        :companies_array="card.companies_array"
        :countries_array="card.countries_array"
        :runtime="card.runtime"
      />
    </v-flex>
    <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" style="padding-top:50px;" />
  </v-layout>
</template>

<script>
import MovieListCard from "./MovieListCard"
export default {
  components: {
    MovieListCard
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 9,
    page: 1,
  }),
  computed: {
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      return this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
};
</script>
