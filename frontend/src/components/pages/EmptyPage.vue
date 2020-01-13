<template>
  <v-container>
    <MovieRecommendList v-if="recommend_status" />
    <v-row>
      <v-col
        cols="12"
      >
        <v-container grid-list-md text-center>
          <span class="see">S</span><span class="see2">ee</span><br>
          <span class="see">S</span><span class="see2">earch</span><br>
          <span class="see">S</span><span class="see2">hare</span><br>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MovieRecommendList from '../Recommend/MovieRecommendList';

export default {
  components: {
    MovieRecommendList
  },
  data: () => ({
      recommend_status: false
  }),
  created(){
    let recommend_user = sessionStorage.getItem("period")
    if(recommend_user!="undefined"&&recommend_user!=null){
      this.recommend_status=true
    }
    else{
      this.recommend_status=false
    }
  }
};
</script>

<style>
.see {
  text-align: center;
  font-size: 200%;
  color: white;
}

.see2{
  font-size: 200%;
}
</style>
