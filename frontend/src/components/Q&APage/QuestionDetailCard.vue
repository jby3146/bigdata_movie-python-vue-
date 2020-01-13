<template>
  <v-card
    :loading="loading"
    class="mx-auto card"
  >
    <v-card-text>
      <div class="article-details">
        <h4 class="post-category">Question Title</h4>
        <h3 class="post-title font"> {{ title }} </h3>

        <h4 class="post-category" style="padding-top:40px;">Question Name </h4>
        <h3 class="post-title font"> {{ name }} </h3>

        <h4 class="post-category" style="padding-top:40px;">Contents </h4>
        <v-chip-group
          text-center
          column
        >
          <v-chip style="height:200px; width:610px;"> {{ content }} </v-chip>
        </v-chip-group>

        <h4 class="post-category" style="padding-top:40px;">Replys </h4>
        <v-chip-group
          text-center
          column
        >
          <v-chip style="height:200px; width:610px;"> {{ replys }} </v-chip>
        </v-chip-group>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        default: ""
      },
      name: {
        type: String,
        default: ""
      },
      content: {
        type: String,
        default: ""
      },
      replys : {
        type: String,
        default: ""
      },
      times : {
        type: String,
        default: ""
      }
    },
    data: () => ({
      loading: false,
      movies: {

      },
    }),
    computed: {
    },
    mounted() {
    },
    methods: {
    },
  }
</script>
<style>
  .rating {
    margin-left: 130px;
  }
</style>
