<template>
  <v-card
    :loading="loading"
    class="mx-auto card"
    xs12 sm6 md4 lg3 xl2
  >
    <v-img v-if="imgpath == ''" class="post-image" src="../../img/NotPoster.jpg" />
    <v-img v-else id="inter_btn_right" :src="imgpath" max-width="320" max-height="400" />
    <div class="article-details">
      <h4 class="post-category">MOVIE Title</h4>
      <h3 class="post-title font"> {{ title }} </h3>

      <br>
      <h4 class="post-category">Production Companies</h4>
      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip v-for="i in companies_array" :key="i">{{ i }}</v-chip>
      </v-chip-group>

      <br>
      <h4 class="post-category">Production Countries</h4>
      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip v-for="i in countries_array" :key="i">{{ i }}</v-chip>
      </v-chip-group>

      <br>
      <h4 class="post-category">Overview</h4>
      <p> {{ overview }} </p>

      <br>
      <h4 class="post-category">Runtime</h4>
      <p> {{ runtime }} Minute </p>

      <br>
      <h4 class="post-category">MOVIE Genre</h4>
      <v-chip-group
        active-class="teal  accent-4 white--text"
        column
      >
        <v-chip v-for="i in genres" :key="i">{{ i }}</v-chip>
      </v-chip-group>

      <br>
      <h4 class="post-category">My Rating( {{ myrating }} )</h4>
      <v-rating
        v-model="myrating"
        color="amber"
        background-color="gray"
        dense
        size="20"
      />

      <h4 class="post-category">MOVIE Grade( {{ rating.toFixed(1) }} )</h4>
      <v-rating
        :value="rating"
        color="amber"
        background-color="gray"
        half-increments
        dense
        size="20"
        readonly
      />
    </div>
    <v-card-text>
      <template>
        <v-card
          class="mx-auto"
          tile
        >
          <v-list disabled>
            <v-subheader>이 영화를 본 유저들</v-subheader>
            <v-list-item-group color="primary">
              <v-list-item
                v-for="(user, id) in users"
                :key="id"
              >
                <v-list-item-icon>
                  <v-icon v-text="'mdi-account'" />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="user.id" />
                  <v-list-item-subtitle>
                    <v-rating
                      :value="user.rating"
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
        <v-subheader>유사 영화 랭킹</v-subheader>
        <v-flex v-for="(card, index) in mlist" :key="card.id" pa-2>
          <v-list-item class="grey--text ml-4">
            <v-list-item-action>
              <v-icon>{{ index+1 }}위</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ card }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
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

        title: {
        type: String,
        default: ""
        },

        genres: {
        type: Array,
        default: () => new Array()
        },

        img: {
        type: String,
        default: ""
        },

        rating: {
        type: Number,
        default: 0.0
        },

        viewCnt: {
        type: Number,
        default: 0
        },
        imgpath: {
          type: String,
          default: ""
        },
        overview: {
          type: String,
          default: ""
        },
        companies_array: {
          type: Array,
          default: () => new Array()
        },
        countries_array: {
          type: Array,
          default: () => new Array()
        },
        runtime: {
          type: Number,
          default: 0
        }
    },
    data: () => ({
      loading: false,
      dialog: false,
      users: {

      },
      myrating:3,
      mlist:'',
      username:0,
      movieid:0,
      rating_status:null,
      rating_value:false,
      cnt:0
      }),
    computed: {
      genresStr: function() {
        return this.genres.join(" / ");
      },

    },
    watch:{
      myrating: async function(){
        if(this.cnt>0){

          const param ={
            username:sessionStorage.getItem('name'),
            movieid:this.id,
            rating:this.myrating,
            status:this.rating_value
          }
          const resp = await api.ratingupload(param)
          this.rating_status = resp.data.insert
          this.rating_value = true
        }
        else
          this.cnt=1
      }
    },
    mounted() {
      this.searchMovieUsers(this.id);
      this.searchMovies(this.id);
      this.searchuser(this.id);
    },
    methods: {
      async searchMovieUsers(userid) {
        const params = {
          id : userid,
        }
        const resp = await api.searchMovieUsers(params)
        this.users = resp.data.map(d => ({
          id: d.userid,
          rating: d.rating,
        }))
      },
      async searchMovies(movieid) {
        const param = {
          id : movieid
        }
        const resp = await api.searchMovies(param)
        this.mlist = resp.data[0]['mlist_array']
      },
      async searchuser(){
        const params = {
          username:sessionStorage.getItem('name'),
          movieid:this.id
        }
        const resp = await api.searchuser(params)

        if(resp.data.movieid!="None"){
          this.myrating = resp.data.rating
          this.rating_value = true
        }
        else{
          this.myrating =0
          this.rating_value=false
        }
      },
    }
  }
</script>

<style>
.card {
    width: 1000px;
  }
.font {
  font-family: "Karla Tamil Upright", sans-serif;
}
.blog-card {

  display: flex;
  flex-direction: row;
  background: #fff;
  box-shadow: 0 0.1875rem 1.5rem rgba(0, 0, 0, 0.02);
  border-radius: 0.375rem;
  overflow: hidden;
}

.card-link {
  position: relative;
  display: block;
  color: inherit;
  text-decoration: none;
}

.card-link:hover .post-image {
  @include transition(opacity 0.3s ease);
  opacity: 0.9;
}

.post-image {
  @include transition(opacity 0.3s ease);
  display: block;
  /* width: 100%; */
	/* object-fit: cover; */
}

.article-details {
  padding: 3rem;
}

.post-category {
  display: inline-block;
  text-transform: uppercase;
  font-size: 0.89rem;
  font-weight: 700;
  line-height: 1;
  letter-spacing: 0.0625rem;
  margin: 0 0 0.75rem 0;
  padding: 0 0 0.25rem 0;
  border-bottom: 0.125rem solid #ebebeb;
}

.post-title {
  @include transition(color 0.3s ease);
  font-size: 1.525rem;
  line-height: 1.4;
  color: #121212;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
}

.post-author {
  font-size: 1.275rem;
  line-height: 1;
  margin: 1.125rem 0 0 0;
  padding: 1.125rem 0 0 0;
  border-top: 0.0625rem solid #ebebeb;
}

@media (max-width: 40rem) {
  #container {
    width: 18rem;
    height: 27.25rem;
  }

  .blog-card {
    flex-wrap: wrap;
  }
}

@supports (display: grid) {

  #container {
    grid-area: main;
    align-self: center;
    justify-self: center;
  }

  .post-image {
    height: 125%;
  }

  .blog-card {
    display: grid;
    grid-template-columns: 1fr 2fr;
    grid-template-rows: 1fr;
  }

  @media (max-width: 40rem) {
    .blog-card {
      grid-template-columns: auto;
      grid-template-rows: 12rem 1fr;
    }
  }
}
</style>
