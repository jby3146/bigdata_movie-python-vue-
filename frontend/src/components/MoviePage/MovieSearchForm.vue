<template>
  <v-form ref="form">
    <v-menu
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          id="outer_btn_right"
          class="movie_search_css"
          v-on="on"
        >
          {{ title }}
        </v-btn>
        <v-btn
          id="inter_btn_right"
          v-on="on"
        >
          {{ title }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="Dropdown(item.title)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-btn id="outer_btn_right" @click="onSubmit">Search</v-btn>
    <v-btn id="inter_btn_right" class="movie_btn_css" @click="onSubmit">Search</v-btn>
    <v-text-field class="white_s" v-model="search" label="검색" @keyup.enter="onSubmit" />
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
      items: [
        { title: '타이틀' },
        { title: '장르' },
        { title: '조회순' },
        { title: '평점순' },
      ],
      title: "Select",
      search:"",
      params: {

      },
    }),
  methods: {
    onSubmit: function() {
      switch (this.title) {
        case "타이틀":
          this.params = {
            title: this.search,
          };
          break;
        case "장르":
          this.params = {
            genres: this.search,
          };
          break;
        case "조회순":
          this.params = {
            sort: '2',
          };
          break;
        case "평점순":
          this.params = {
            sort: '1',
          };
          break;
      }
      this.submit(this.params);
    },
    Dropdown: function(title) {
      this.title = title;
    }
  }
};
</script>

<style>
.movie_search_css{
  margin-right:10px;
}
.movie_btn_css {
  margin-top: 10px;
}
</style>
