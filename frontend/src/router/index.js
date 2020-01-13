import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/SearchPage/MovieSearchPage'
import UserSearchPage from '../components/SearchPage/UserSearchPage'
import QuestionSearchPage from '../components/SearchPage/QuestionSearchPage'
import RankSearchPage from '../components/SearchPage/RankSearchPage'
import UserLoginForm from '../components/UserPage/UserLoginForm'
import UserSignUpForm from '../components/UserPage/UserSignUpForm'
import ClusterSearchPage from '../components/SearchPage/ClusterSearchPage'
import MovieRecommend from '../components/Recommend/MovieRecommend'
import MyPage from '../components/pages/MyPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/ranks/search', component: RankSearchPage, name: 'rank-search' },
    { path: '/users/search', component: UserSearchPage, name: 'user-search' },
    { path: '/question/search', component: QuestionSearchPage, name: 'question-search' },
    { path: '/user/login', component: UserLoginForm, name: 'user-login'},
    { path: '/user/singup', component: UserSignUpForm, name: 'user-singup'},
    { path: '/admin/manager', component: ClusterSearchPage, name: 'admin-management'},
    { path: '/movies/recommend', component: MovieRecommend, name: 'movie-recommend'},
    { path: '/mypages/mypage', component: MyPage, name: 'my-page'}
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router
