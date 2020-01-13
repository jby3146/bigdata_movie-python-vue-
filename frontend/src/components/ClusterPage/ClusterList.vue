<template>
  <v-card>
    <v-card-title>
      {{ title }}
      <v-spacer />
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
      />
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="clusterList"
      :search="search"
    >
      <template v-slot:items="clusterList">
        <td>{{ item.name }}</td>
        <td class="text-xs-right">{{ item.cluster }}</td>
        <td class="text-xs-right">{{ item.userid }}</td>
        <td class="text-xs-right">{{ item.job }}</td>
        <td class="text-xs-right">{{ item.gender }}</td>
        <td class="text-xs-right">{{ item.year }}</td>
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </template>
    </v-data-table>
  </v-card>
</template>


<script>
  export default {
    props: {
      clusterList: {
      type: Array,
      default: () => new Array(),
      },
    },
    data () {
      return {
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
        switch (this.select_value) {
          case 1:
            this.params = {
              cluster : this.select_value
            }
            break;
          case 2:
            this.params = {
              cluster : this.select_value
            }
            break;
          case 3:
            this.params = {
              cluster : this.select_value
            }
            break;
        }
        this.submit(this.params);
      }
    }
  }
</script>
