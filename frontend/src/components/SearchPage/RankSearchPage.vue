<!-- 랭킹 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-1">Ranking Search</div>
        <br>
        <RankSearchForm :submit="searchRanks" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs12>
        <RankList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import RankSearchForm from "../RankPage/RankSearchForm";
import RankList from "../RankPage/RankList";
export default {
  components: {
    RankList,
    RankSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      movieList: state => state.data.rankSearchList
    })
  },
  methods: mapActions("data", ["searchRanks"])
};
</script>
