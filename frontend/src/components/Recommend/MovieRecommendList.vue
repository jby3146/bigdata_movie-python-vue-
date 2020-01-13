<template>
  <v-container grid-list-md text-center>
    <v-row>
      <v-col
        cols="12"
        md="8"
      >
        <v-card
          id="outer_btn_right"
          class="pic"
        >
          <v-img v-if="imgpaths[0] == ''" class="pic-image" src="../../img/NotPoster.jpg" />
          <v-img v-else :src="imgpaths[0]" class="pic-image" aspect-ratio="1" />

          <span class="pic-caption rotate-in margin_t">
            <div style="height:150px" />
            <span class="pic-title font-weight-black"> {{ titles[0] }} </span>
            <span> {{ runtimes[0] }} minute</span>
            <br>
            <br>
            <span class="font-weight-bold"> companie : </span><span v-for="co in companies[0]"> {{ co }} |</span>
            <br>
            <span class="font-weight-bold"> Genre : </span> <span v-for="ar in genre[0]"> {{ ar }} |</span>
            <br>
            <br>
            <span class="font-weight-bold"> Stroy </span>
            <br>
            <br>
            <p> {{ overviews[0] }}</p>
            <br>
            <br>
            <span class="font-weight-bold"> countrie : </span> <span v-for="coun in countries[0]"> {{ coun }} </span>
          </span>
        </v-card>
        <v-card
          id="inter_btn_right"
          class="pic"
        >
          <v-img v-if="imgpaths[0] == ''" class="pic-image" src="../../img/NotPoster.jpg" />
          <v-img v-else :src="imgpaths[0]" class="pic-image" aspect-ratio="1" />

          <span class="pic-caption rotate-in margin_t">
            <span class="pic-title font-weight-black"> {{ titles[0] }} </span>
            <span> {{ runtimes[0] }} minute</span>
            <br>
            <br>
            <span class="font-weight-bold"> companie : </span><span v-for="co in companies[0]"> {{ co }} |</span>
            <br>
            <span class="font-weight-bold"> Genre : </span> <span v-for="ar in genre[0]"> {{ ar }} |</span>
            <br>
            <br>
            <span class="font-weight-bold"> Stroy </span>
            <br>
            <br>
            <p> {{ overviews[0] }}</p>
            <br>
            <br>
            <span class="font-weight-bold"> countrie : </span> <span v-for="coun in countries[0]"> {{ coun }} </span>
          </span>
        </v-card>
      </v-col>
      <v-col
        cols="12"
        md="4"
      >
        <v-card
          class="pic"
        >
          <v-img v-if="imgpaths[1] == ''" class="pic-image" src="../../img/NotPoster.jpg" aspect-ratio="1.5" />
          <v-img v-else :src="imgpaths[1]" class="pic-image" aspect-ratio="1.05" />

          <span class="pic-caption rotate-in margin_t">
            <span class="pic-title font-weight-black"> {{ titles[1] }} </span>
            <span> {{ runtimes[1] }} minute</span>
            <br>
            <br>
            <span class="font-weight-bold"> companie : </span><span v-for="co in companies[1]"> {{ co }} |</span>
            <br>
            <span class="font-weight-bold"> Genre : </span> <span v-for="ar in genre[1]"> {{ ar }} |</span>
            <br>
            <br>
            <span class="font-weight-bold"> Stroy </span>
            <br>
            <p> {{ overviews[1] }}</p>
            <br>
          </span>
        </v-card>
        <br>
        <v-card
          class="pic"
        >
          <v-img v-if="imgpaths[2] == ''" class="pic-image" src="../../img/NotPoster.jpg" aspect-ratio="1.5" />
          <v-img v-else :src="imgpaths[2]" class="pic-image" aspect-ratio="0.99" />

          <span class="pic-caption rotate-in margin_t">
            <span class="pic-title font-weight-black"> {{ titles[2] }} </span>
            <span> {{ runtimes[2] }} minute</span>
            <br>
            <br>
            <span class="font-weight-bold"> companie : </span><span v-for="co in companies[2]"> {{ co }} |</span>
            <br>
            <span class="font-weight-bold"> Genre : </span> <span v-for="ar in genre[2]"> {{ ar }} |</span>
            <br>
            <br>
            <span class="font-weight-bold"> Stroy </span>
            <br>
            <br>
            <p class="patop"> {{ overviews[2] }}</p>
          </span>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="n in 3"
        :key="n"
        cols="12"
        md="4"
      >
        <v-card
          class="pic"
        >
          <v-img v-if="imgpaths[n+2] == ''" class="pic-image" src="../../img/NotPoster.jpg" aspect-ratio="1.5" />
          <v-img v-else :src="imgpaths[n+2]" class="pic-image" aspect-ratio="0.8" />

          <span class="pic-caption rotate-in margin_t">
            <span class="pic-title font-weight-black"> {{ titles[n+2] }} </span>
            <span> {{ runtimes[n+2] }} minute</span>
            <br>
            <br>
            <span class="font-weight-bold"> companie : </span><span v-for="co in companies[n+2]"> {{ co }} |</span>
            <br>
            <span class="font-weight-bold"> Genre : </span> <span v-for="ar in genre[n+2]"> {{ ar }} |</span>
            <br>
            <br>
            <span class="font-weight-bold"> Stroy </span>
            <br>
            <br>
            <p class="patop"> {{ overviews[n+2] }}</p>
          </span>
        </v-card>
      </v-col>
    </v-row>
    <span class="dis"> {{ movies[0] }} </span>
  </v-container>
</template>

<script>
import api from '../../api'
export default {
  components: {
  },
  data: () => ({
    movies: {

    },
    genre:[[""],[""],[""],[""],[""],[""]],
    companies:[[""],[""],[""],[""],[""],[""]],
    countries:[[""],[""],[""],[""],[""],[""]],
    imgpaths:[[""],[""],[""],[""],[""],[""]],
    titles:[[""],[""],[""],[""],[""],[""]],
    runtimes:[[""],[""],[""],[""],[""],[""]],
    overviews:[[""],[""],[""],[""],[""],[""]],
  }),
  mounted() {
    this.recommendMovies(sessionStorage.getItem("uid"));
    },
    methods: {
      async recommendMovies(userid) {
        const params = {
          id : userid
        }
        const resp = await api.recommendMovies(params)
        this.movies = resp.data.map(d => ({
          id: d.id,
          title: d.title,
          genres: d.genres_array,
          viewCnt: d.viewCnt,
          rating: d.ratings/d.viewCnt,
          counting: d.counting,
          imgpath: d.imgpath,
          overview: d.overview,
          companies_array: d.production_companies_array,
          countries_array: d.production_countries_array,
          runtime: d.runtime
          }))
          for(var i=0; i<this.movies.length; i++) {
            var arrays = [];
            for(var j=0; j<this.movies[i].genres.length; j++){
              arrays.push(this.movies[i].genres[j])
            }
            this.genre[i] = arrays
          }
          for(var k=0; k<this.movies.length; k++) {
            var arrays_se = [];
            for(var l=0; l<this.movies[k].companies_array.length; l++){
              arrays_se.push(this.movies[k].companies_array[l])
            }
            this.companies[k] = arrays_se
          }
          for(var a=0; a<this.movies.length; a++) {
            var arrays_ae = [];
            for(var b=0; b<this.movies[a].countries_array.length; b++){
              arrays_ae.push(this.movies[a].countries_array[b])
            }
            this.countries[a] = arrays_ae
          }
          for(var w=0; w<this.movies.length; w++) {
            this.imgpaths[w] = this.movies[w].imgpath
          }
          for(var s=0; s<this.movies.length; s++) {
            this.titles[s] = this.movies[s].title
          }
          for(var r=0; r<this.movies.length; r++) {
            this.runtimes[r] = this.movies[r].runtime
          }
          for(var o=0; o<this.movies.length; o++) {
            this.overviews[o] = this.movies[o].overview
          }
      }
    },
};
</script>

<style>

.dis {
  display: none;
}
.margin_t {
  padding-top: 200px;
}

.content {
  position: realative;
}
.img {
  max-width: 100%;
  height: auto;
}

.rank_img {
  position: absolute;
  top:0px;
  left:0px;
   z-index: 1;
}

.first_css {
  height: 600px;
}

.second_css {
  height: 290px;
}

.third_css {
  height: 300px;
}

.pic {
    position: relative;
    overflow: hidden;
    margin: 10px;
    display: inline-block;
    -webkit-animation: anima 2s;
    -moz-animation: anima 2s;
    -o-animation: anima 2s;
    -ms-animation: anima 2s;
    animation: anima 2s;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    -o-backface-visibility: hidden;
    -ms-backface-visibility: hidden;
    backface-visibility: hidden;


}

.pic-caption {
    font-family: 'Raleway', Arial, sans-serif;
    cursor: default;
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,1);
    color: #ffffff;
    padding: 40px;
    text-align: center;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=($opacity * 100))";
    filter: alpha(opacity=0);
    -moz-opacity: 0;
    -khtml-opacity: 0;
    opacity: 0
}

.pic-image {
    -webkit-transform: scale(1.1);
    -moz-transform: scale(1.1);
    -o-transform: scale(1.1);
    -ms-transform: scale(1.1);
    transform: scale(1.1)
}

.pic:hover .pic-image {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -o-transform: scale(1);
    -ms-transform: scale(1);
    transform: scale(1)
}

.pic-title {
    font-size: 1.8em;
    color: #ffffff;
}

a,
a:hover,
.pic .pic-image,
.pic-caption,
.pic:hover .pic-caption,
.pic:hover img {
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    -ms-transition: all 0.5s ease;
    transition: all 0.5s ease
}

.pic:hover .rotate-in {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=($opacity * 100))";
    filter: alpha(opacity=100);
    -moz-opacity: 1;
    -khtml-opacity: 1;
    opacity: 1;
    -webkit-user-select: none;
    -moz-user-select: none;
    -o-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-touch-callout: none;
    -moz-touch-callout: none;
    -o-touch-callout: none;
    -ms-touch-callout: none;
    touch-callout: none;
    -webkit-tap-highlight-color: transparent;
    -moz-tap-highlight-color: transparent;
    -o-tap-highlight-color: transparent;
    -ms-tap-highlight-color: transparent;
    tap-highlight-color: transparent
}

.rotate-in {
    -webkit-transform: rotate(90deg) scale(0.1);
    -moz-transform: rotate(90deg) scale(0.1);
    -o-transform: rotate(90deg) scale(0.1);
    -ms-transform: rotate(90deg) scale(0.1);
    transform: rotate(90deg) scale(0.1);
    top: 0;
    left: 0
}

.pic:hover .rotate-in {
    -webkit-transform: rotate(360deg) scale(1);
    -moz-transform: rotate(360deg) scale(1);
    -o-transform: rotate(360deg) scale(1);
    -ms-transform: rotate(360deg) scale(1);
    transform: rotate(360deg) scale(1)
}

@media screen and (min-width: 100px) {
    .pic {
        display: block;
        -webkit-animation: none;
        -moz-animation: none;
        -o-animation: none;
        -ms-animation: none;
        animation: none;
        margin: 10px auto
    }
}
</style>
