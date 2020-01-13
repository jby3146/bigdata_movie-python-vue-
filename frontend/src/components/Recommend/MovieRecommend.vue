<template>
  <v-container grid-list-md text-center>
    <MovieRecommendList />
  </v-container>
</template>

<script>
import MovieRecommendList from './MovieRecommendList'
export default {
  components: {
    MovieRecommendList
  },
  data: () => ({
    username :sessionStorage.getItem("name"),
  }),
  mounted() {
    this.checks(this.username);
    },
    methods: {
      checks: function() {
        if(this.username == null) {
          this.$router.push('/')
        }
      }
    }
};
</script>
