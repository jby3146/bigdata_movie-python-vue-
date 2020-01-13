<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column align-center py-4 pl-4>
      <v-card>
        <v-flex v-for="(card, index) in movieListCardsSliced" :key="card.id" pa-2>
          <v-list-item class="ml-4">
            <v-list-item-action>
              <v-icon>{{ index+1 }}위</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ card.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-flex>
      </v-card>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 10,
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
