<template>
  <v-app id="app">
    <v-app-bar app clipped-left class="FBFAF2">
      <v-app-bar-nav-icon class="black--text" @click="drawer = !drawer" />
      <router-link to="/">
        <span id="outer_btn_right" class="black--text">See Search Share</span>
        <span id="inter_btn_right" class="black--text">See Search Share</span>
      </router-link>
      <v-spacer />
      <span class="black--text name_css" :class="{'activetitle':status}">
        Welcome to {{ name }}
      </span>
      <span id="outer_btn_right" class="singup_css">
        <UserLoginForm />
      </span>
      <span v-if="status == true" id="outer_btn_right">
        <UserSignUpForm />
      </span>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped color="">
      <br>
      <div v-if="status == false" class="title_css">
        <h3> Mypage </h3>
      </div>
      <v-list v-if="status == false" dense class="icon_css">
        <v-menu
          v-model="value"
          :close-on-click="closeOnClick"
          :close-on-content-click="closeOnContentClick"
          :offset-x="offsetX"
        >
          <template v-slot:activator="{ on }">
            <v-list-item>
              <v-list-item-action>
                <v-icon> mdi-account-box-outline </v-icon>
              </v-list-item-action>
              <v-list-item-title class="black--text" v-on="on">
                My Info Window
              </v-list-item-title>
            </v-list-item>
          </template>
          <v-list dense class=" lighten-4">
            <template v-for="(mypage, i) in mypages">
              <v-list-item
                :key="i"
                @click="() => {
                  goTo(mypage.path)
                }"
              >
                <v-list-item-action>
                  <v-icon>{{ mypage.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title class="subtitle-2 black--text">
                    {{ mypage.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </v-menu>
      </v-list>

      <div v-if="recommend_btn" class="title_css">
        <h3> Recommend </h3>
      </div>
      <v-list v-if="recommend_btn" dense class="icon_css">
        <template v-for="(Recommends, i) in Recommend">
          <v-list-item
            :key="i"
            @click="() => {
              if (Recommends.path) {
                goTo(Recommends.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ Recommends.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="black--text">{{ Recommends.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>

      <div class="title_css">
        <h3> Search </h3>
      </div>
      <v-list dense class="icon_css">
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>

      <div v-if=" username == 'admin'" class="title_css">
        <h3> Cluster </h3>
      </div>
      <v-list v-if=" username == 'admin'" dense class="icon_css">
        <template v-for="(Clusters, i) in Cluster">
          <v-list-item
            :key="i"
            @click="() => {
              if (Clusters.path) {
                goTo(Clusters.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ Clusters.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ Clusters.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>

      <div class="title_css">
        <h3> Developer </h3>
      </div>
      <v-list dense class="icon_css">
        <v-menu
          v-model="value_D"
          :close-on-click="closeOnClick"
          :close-on-content-click="closeOnContentClick"
          :offset-x="offsetX"
        >
          <template v-slot:activator="{ on }">
            <v-list-item>
              <v-list-item-action>
                <v-icon> mdi-github-box </v-icon>
              </v-list-item-action>
              <v-list-item-title class="black--text" v-on="on">
                Git Lab
              </v-list-item-title>
            </v-list-item>
          </template>

          <v-list dense class="lighten-4">
            <template v-for="(admin,i) in admins">
              <v-list-item :key="i">
                <v-list-item-action>
                  <v-icon>{{ admin.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title class="subtitle-2 black--text"><a :href="admin.http" style="color: black">{{ admin.text }}</a></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </v-menu>
      </v-list>

      <div v-if="status == false" class="title_css">
        <h3> Questions & Information </h3>
      </div>
      <v-list v-if="status == false" dense class="icon_css">
        <template>
          <v-list-item>
            <v-list-item-action>
              <v-icon> mdi-help </v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="caption subtitle-2"> <QuestionPage /> </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>

      <v-list-item id="inter_btn_right" class="list_item_padding">
        <UserLoginForm v-if="status == false" class="mobile_css" />
        <UserLoginForm v-if="status == true" />
        <UserSignUpForm v-if="status == true" />
      </v-list-item>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid fill-height class="backcolor-portfolios">
        <v-layout justify-center align-center>
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import UserSignUpForm from '../UserPage/UserSignUpForm';
import UserLoginForm from '../UserPage/UserLoginForm';
import QuestionPage from '../pages/QuestionPage';
import api from '../../api'
import { eventBus } from "../../store/index.js";
export default {
  components: {
    UserSignUpForm,
    UserLoginForm,
    QuestionPage
  },
  data: () => ({
    drawer: null,
    status: false,
    name:"",
    username: sessionStorage.getItem("name"),
    users: {

    },
    period: sessionStorage.getItem("period"),
    mypages: [
      {
        icon : "mdi-account-box-outline",
        text : "My Information",
        path : "my-page"
      }
    ],
    Recommend : [
      {
        icon: "mdi-star-outline",
        text: "Movie Recommendation",
        path: "movie-recommend"
      },

    ],
    choices: [
      {
        icon: "mdi-movie",
        text: "Movie Search",
        path: "movie-search"
      },
      {
        icon: "mdi-account",
        text: "Member Search",
        path: "user-search"
      },
      {
        icon: "mdi-help",
        text: "Question Search",
        path: "question-search"
      },
      {
        icon: "mdi-crown",
        text: "Ranking Search",
        path: "rank-search"
      }
    ],
    Cluster: [
      {
        icon: "mdi-database",
        text: "Clustering",
        path: "admin-management"
      }
    ],
    admins: [
      {
        icon : "mdi-numeric-1-box-outline",
        text : "Ms.KimH",
        http : "https://lab.ssafy.com/hyunnnji"
      },
      {
        icon : "mdi-numeric-2-box-outline",
        text : "Mr.Wi",
        http : "https://lab.ssafy.com/wijunseok"
      },
      {
        icon : "mdi-numeric-3-box-outline",
        text : "Mr.Jo",
        http : "https://lab.ssafy.com/jby3146"
      },
      {
        icon : "mdi-numeric-4-box-outline",
        text : "Mr.KimH",
        http : "https://lab.ssafy.com/DogBird"
      },
      {
        icon : "mdi-numeric-5-box-outline",
        text : "Mr.Jung",
        http : "https://lab.ssafy.com/JeongSY"
      }
    ],
    items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ],
      value: false,
      value_D: false,
      closeOnClick: true,
      closeOnContentClick: true,
      offsetX: true,
      recommend_btn:false
  }),
  created: function(){
    if(sessionStorage.getItem("name")!=null){
      this.Loginstatus="logout";
        this.status=false;
        this.name = sessionStorage.getItem("name");
        this.searchSubscribe();
    }
    else{
        this.Loginstatus="login";
        this.status=true;
    }
    eventBus.$on("sendPeriod", title => {
      if(title!="none"){
        this.recommend_btn=true
      }
      else{
        this.recommend_btn=false
      }
    })
    if(this.period!=null&&this.period!="undefined"){
          this.recommend_btn=true
    }
    else{
      this.recommend_btn=false
    }
  },
  methods: {
    async searchSubscribe() {
        const params = {
          usernametime: this.name
        }
        const resp = await api.createPeriod(params)
        this.period = resp.data[0]

        if(resp.data.length != 0) {
          this.period = resp.data[0]['period']
          if(this.period!="undefined"&&this.period!=null){
            sessionStorage.setItem("period", this.period);
          }
        }
        if(this.period!=null&&this.period!="undefined"){
          this.recommend_btn=true
        }
        else
          this.recommend_btn
      },
    goTo: function(path) {
      router.push({ name: path });
    },
    ...mapActions("data", ["login"])
  },
};
</script>

<style>
.mobile_css {
  padding-left: 60px;
}

.icon_css {
  padding-left: 20px;
}

.title_css {
  padding-left: 20px;
}

.singup_css {
  padding-right: 30px;
}

.activetitle {
  display:none;
}

.name_css {
  color: white;
  padding-right: 30px;
}

a {
  text-decoration:none ;
  color:#000000;
}

@media screen and (max-width: 420px) {
#outer_btn_right {
    display: none;
  }
}

@media screen and (min-width: 420px) {
#inter_btn_right {
    display: none;
  }
}

.list_item_padding {
  padding-left: 35px;
}

.recommend_css {
  display:none;
}

.choice_css {
  background-color: #657B69;
}
</style>
