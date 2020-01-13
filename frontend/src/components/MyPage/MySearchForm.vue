<template>
  <v-form ref="form">
    <v-btn
      class="ma-2"
      @click="onSubmit"
    >
      Search
    </v-btn>
  </v-form>
</template>


<script>
import api from '../../api'
  export default {
    props: {
      submit: {
        type: Function,
        default: () => {}
      },
      cluster : {
        type: Number,
        default: 0
      },
      userid : {
        type: Number,
        default: 0
      },
      job : {
        type: String,
        default: ""
      },
      gender : {
        type: String,
        default: ""
      },
      year : {
        type: Number,
        default: 0
      },
    },
    data () {
      return {
        form: {
          username : sessionStorage.getItem("name")
        },
        length: 5,
        select_value: 0,
        number: 0,
        title: "Kmeans",
        loader: null,
        loading: false,
        search: '',
      }
    },
    methods: {
      onSubmit: function() {
        api.searchMyMovie(this.form);
      },
    }
  }
</script>
