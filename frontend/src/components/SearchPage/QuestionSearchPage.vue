<!-- 질문 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-1">Question Search</div>
        <br>
        <QuestionSearchForm :submit="searchQuestion" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs12>
        <QuestionList :question-list-cards="questionList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import QuestionSearchForm from "../Q&APage/QuestionSearchForm";
import QuestionList from "../Q&APage/QuestionList";
export default {
  components: {
    QuestionList,
    QuestionSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      questionList: state => state.data.questionSearchList
    })
  },
  methods: mapActions("data", ["searchQuestion"])
};
</script>
