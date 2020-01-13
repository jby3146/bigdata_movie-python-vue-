<template>
  <v-layout wrap>
    <v-flex v-for="card in userListCardsSliced" :key="card.id" pa-2
            xs12
            sm6
            md6
            lg4
            xl3
    >
      <UserListCard
        :id="card.id"
        :gender="card.gender"
        :age="card.age"
        :occupation="card.occupation"
      />
    </v-flex>
    <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" style="padding-top:50px;" />
  </v-layout>
</template>

<script>
import UserListCard from "./UserListCard"
export default {
  components: {
    UserListCard
  },
  props: {
    userListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 12,
    page: 1,
  }),
  computed: {
    userListEmpty: function() {
      return this.userListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.userListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    userListCardsSliced: function() {
      return this.userListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
};
</script>
