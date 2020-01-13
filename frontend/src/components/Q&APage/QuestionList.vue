<template>
  <v-layout wrap>
    <v-flex v-for="card in questionListCardsSliced" :key="card.id" pa-2
            xs12
            sm6
            md6
            lg4
            xl3
    >
      <QuestionListCard
        :title="card.title"
        :name="card.name"
        :content="card.content"
        :replys="card.replys"
        :times="card.times"
      />
    </v-flex>
    <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
  </v-layout>
</template>

<script>
import QuestionListCard from "./QuestionListCard"
export default {
  components: {
    QuestionListCard
  },
  props: {
    questionListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 9,
    page: 1,
  }),
  computed: {
    questionListEmpty: function() {
      return this.questionListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.questionListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    questionListCardsSliced: function() {
      return this.questionListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
};
</script>
