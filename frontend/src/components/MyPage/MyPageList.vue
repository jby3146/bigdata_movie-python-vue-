<template>
  <v-card>
    <v-card-title>
      내가 본 영화 목록  
    </v-card-title>
    <v-list-item
      v-for="(movie, id) in movies"
      :key="id"
    >
      <v-list-item-icon>
        <v-icon v-text="'mdi-movie'" />
      </v-list-item-icon>
      <v-list-item-content>
        <v-list-item-title v-text="movie.title" />
        <v-list-item-subtitle>
          <v-rating
            :value="movie.rating"
            color="amber"
            half-increments
            dense
            size="14"
            readonly
          />
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>

<script>
import api from '../../api'

  export default {
    data: () => ({
      loading: false,
      movies: {

      },
      users: [],
      dialog: false,
      id: sessionStorage.getItem("uid")
    }),
    mounted() {
      this.searchMovie(this.id);
    },
    methods: {
      async searchMovie(userid) {
        const params = {
          userid : userid
        }
        const resp = await api.searchUsersMovie(params)
        this.movies = resp.data.map(d => ({
          movieid: d.movieid,
          rating: d.rating,
          title: d.movietitle
        }))
      },
    },
  }
</script>
