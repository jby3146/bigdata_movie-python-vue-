<template>
  <v-form ref="form">
    <v-menu
      bottom
      origin="center center"
      transition="scale-transition"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
        >
          {{ title }}
        </v-btn>
      </template>

      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          @click="select_check(item)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-btn
      class="ma-2"
      @click="onSubmit"
    >
      Clustering algorithm
      <template v-slot:loader>
        <span>Loading...</span>
      </template>
    </v-btn>
    <v-slider
      v-model="number"
      color="black darken-4"
      min="1"
      max="20"
      label="Cluster"
      thumb-label
    />
  </v-form>
</template>


<script>
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
        length: 5,
        select_value: 0,
        number: 0,
        title: "Kmeans",
        loader: null,
        loading: false,
        search: '',
        params: {

        },
        headers: [
         {
           text: 'Cluster',
           align: 'left',
           sortable: false,
           value: 'cluster'
         },
         { text: 'Userid', value: 'userid' },
         { text: 'Job', value: 'job' },
         { text: 'Gender', value: 'gender' },
         { text: 'Year', value: 'year' }
       ],
       items: [
         {
           value: 1,
           title: "Kmeans"
         },
         {
           value: 2,
           title: "Hierarchical"
         },
         {
           value: 3,
           title: "EM"
         }
       ],
      }
    },
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]
        setTimeout(() => (this[l] = false), 3000)
        this.loader = null
      }
    },
    methods: {
      select_check : function(select) {
        this.select_value = select.value;
        this.title = select.title;
      },
      onSubmit : function() {
        if(this.select_value == 0){
          this.select_value = 1;
        }
        this.params = {
          cluster : this.select_value,
          number : this.number
        }
        this.submit(this.params);
      }
    }
  }
</script>
