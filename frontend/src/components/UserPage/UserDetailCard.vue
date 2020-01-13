<template>
  <v-card
    :loading="loading"
    class="mx-auto card"
    max-width="584"
  >
    <v-img
      height="250"
      src="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2018%2F11%2Favengers-4-done-filming-0001.jpg?q=75&w=800&cbr=1&fit=max"
    />
    <div class="article-details">
      <h4 class="post-category">More information</h4>

      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip> 아이디 : {{ id }} </v-chip>
        <v-chip> 성별 : {{ gender }} </v-chip>
        <v-chip> 나이 : {{ age }} </v-chip>
      </v-chip-group>

      <h4 class="post-category">Job</h4>
      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip> {{ occupation }} </v-chip>
      </v-chip-group>
    </div>

    <v-card-text>
      <template>
        <v-card
          class="mx-auto"
          max-width="800"
          tile
        >
          <v-list disabled>
            <v-subheader>이 유저가 본 영화와 평점</v-subheader>
            <v-list-item-group color="primary">
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
            </v-list-item-group>
          </v-list>
        </v-card>
      </template>
    </v-card-text>

    <v-container class="mx-auto">
      <v-card>
        <v-subheader>취향이 비슷한 사람</v-subheader>
        <v-flex v-for="(card, index) in users" :key="card.id" pa-2>
          <v-dialog v-model="dialog" width="500">
            <template v-slot:activator="{ on }">
              <v-list-item class="grey--text ml-4" v-on="on" @click="searchSameMovie(card.uid)">
                <v-list-item-action>
                  <v-icon>{{ index+1 }}위</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title><v-icon v-text="'mdi-account'" />{{ card.uid }} <v-icon v-text="'mdi-face'" /> {{ card.gender }} <v-icon v-text="'mdi-label'" />{{ card.occupation }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
            <v-card>
              <v-card-title class="headline grey lighten-2" primary-title>
                두 유저 모두 시청한 영화
              </v-card-title>
              <v-card-text v-for="title in sameMovieList" :key="title">
                {{ title }}
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-flex>
      </v-card>
    </v-container>
  </v-card>
</template>

<script>
import api from '../../api'

  export default {
    props: {
      id: {
        type: Number,
        default: 0
      },
      gender: {
        type: String,
        default: ""
      },
      occupation: {
        type: String,
        default: ""
      },
      age: {
        type: Number,
        default: 0
      }
    },
    data: () => ({
      loading: false,
      movies: {

      },
      users: [],
      uidlist: '',
      sameMovieList: [],
      dialog: false,
      resp: ''
    }),
    computed: {
      genresStr: function() {
        return this.genres.join(" / ");
      },
    },
    mounted() {
      this.searchMovie(this.id);
      this.searchUsers(this.id);
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
      async searchSameMovie(userid) {
        const params = {
          userid : userid
        }
        const resp = await api.searchUsersMovie(params)
        var mlist = resp.data.map(d => ({
          title: d.movietitle
        }))

        this.sameMovieList = []
        for(var i = 0; i < mlist.length; i++) {
          for(var j = 0; j < this.movies.length; j++) {
              if( mlist[i]['title'] == this.movies[j]['title'] ) {
                this.sameMovieList.push( mlist[i]['title'] )
              }
          }
        }
      },
      async searchUsers(userid) {
        const params = {
          id : userid
        }
        const resp = await api.searchUsers(params)
        this.resp = resp.data
        this.uidlist = resp.data[0]['uidlist_array']
        this.searchUserList(this.uidlist)
      },
      async searchUserList(uidlist) {
          for(var i = 0; i < 5; i++) {
              const param = {
                id : uidlist[i]
              }
              const res = await api.searchUsers(param)
              this.users.push({
                uid : res.data[0].id,
                gender : res.data[0].gender,
                occupation : res.data[0].occupation
              })
          }
      }
    },
  }
</script>
<style>
  .rating {
    margin-left: 130px;
  }
</style>
