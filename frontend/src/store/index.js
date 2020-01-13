import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
export const eventBus = new Vue();
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    data,
  },
  name:""
})
