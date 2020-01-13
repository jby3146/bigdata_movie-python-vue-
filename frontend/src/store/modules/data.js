import api from '../../api'

const state = {
  movieSearchList: [],
  userSearchList:[],
  rankSearchList:[],
  adminSearchList:[],
  questionSearchList:[],
  recommendsList:[],
  vuexPeriod:''
}
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
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
    commit('setMovieSearchList', movies)
  },
  async searchRecommends({ commit }, params) {
    const resp = await api.recommendMovies(params)
    const movies = resp.data.map(d => ({
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
    commit('setRecommendsList', movies)
  },
  async searchRanks({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.viewCnt,
      rating: d.ratings/d.viewCnt,
      counting: d.counting
    }))
    commit('setRankSearchList', movies)
  },
  async searchUsers({ commit }, params) {
    const resp = await api.searchUsers(params)
    const users = resp.data.map(d => ({
      id: d.id,
      age: d.age,
      occupation: d.occupation,
      gender: d.gender,
    }))
    commit('setUserSearchList', users)
  },
  async searchAdmin({ commit }, params) {
    const resp = await api.searchAdmin(params)
    const admins = resp.data.map(d => ({
      cluster: d.group,
      userid: d.id,
      job: d.occupation,
      gender: d.gender,
      year: d.age,
    }))
    commit('setAdminSearchList', admins)
  },
  async searchQuestion({ commit }, params) {
    const resp = await api.searchQuestion(params)
    const questions = resp.data.map(d => ({
      name : d.name,
      title : d.title,
      content : d.content,
      replys : d.replys,
      times : d.times
    }))
    commit('setQuestionSearchList', questions)
  },
  async login(params) {
    await api.login(params)
  },
  async signUp(params) {
    await api.signUp(params)
  }
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setUserSearchList(state, users) {
    state.userSearchList = users.map(m => m)
  },
  setRankSearchList(state, movies) {
    state.rankSearchList = movies.map(m => m)
  },
  setAdminSearchList(state, admins) {
    state.adminSearchList = admins.map(m => m)
  },
  setQuestionSearchList(state, questions) {
    state.questionSearchList = questions.map(m => m)
  },
  seRecommendsList(state, questions) {
    state.recommendsList = questions.map(m => m)
  },
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}
