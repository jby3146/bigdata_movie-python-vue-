import axios from 'axios'

const apiUrl = '/api'

export default {
  createPeriod(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/subscribe/`, {
      params,
    })
  },
  recommendMovies(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/recommends/`, {
      params,
    })
  },
  searchMovies(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/movies/`, {
      params,
    })
  },
  searchMovieUsers(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/ratings/`, {
      params,
    })
  },
  searchUsers(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/users/`, {
      params,
    })
  },
  searchAdmin(params) {
    return axios.post(`${process.env.VUE_APP_API_URL}/recommends/`, {
      params,
    })
  },
  searchQuestion(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/question/`, {
      params,
    })
  },
  searchUsersMovie(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/ratings/`, {
      params,
    })
  },
  searchMyMovie(params) {
    return axios.get(`${process.env.VUE_APP_API_URL}/myviews/`, {
      params,
    })
  },
  user_update(params) {
    return axios.post(`${process.env.VUE_APP_API_URL}/userupdates/`, {
       params,
     })
  },
  login(params) {
    return axios.post(`${process.env.VUE_APP_API_URL}/login/`, {
       params,
     })
  },
  signUp(params){
    return axios.post(`${process.env.VUE_APP_API_URL}/signup/`, {
      params,
    })
  },
  question(params){
    return axios.post(`${process.env.VUE_APP_API_URL}/question/`, {
      params,
    })
  },
  userrating(params){
    return axios.post(`${process.env.VUE_APP_API_URL}/userrating/`, {
      params,
    })
  },
  searchuser(params){
    return axios.post(`${process.env.VUE_APP_API_URL}/usermovieid/`,{
      params,
    })
  },
  ratingupload(params){
    return axios.post(`${process.env.VUE_APP_API_URL}/insertrating/`,{
      params,
    })
  }
}
