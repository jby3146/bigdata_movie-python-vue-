<template>
  <v-form ref="form">
    <v-menu
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          id="outer_btn_right"
          class="user_search_css"
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
    <v-btn id="inter_btn_right" class="user_btn_css" @click="onSubmit">Search</v-btn>
    <v-text-field v-model="search" label="검색" @keyup.enter="onSubmit" />
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
        { title: '아이디' },
        { title: '성별' },
        { title: '나이순' },
      ],
      title: "select",
      search:"",
      params: {

      },
    }),
  methods: {
    onSubmit: function() {
      switch (this.title) {
        case "아이디":
          this.params = {
            id: this.search,
          };
          break;
        case "성별":
          this.params = {
            gender: this.search,
          };
          break;
        case "나이순":
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
.user_search_css{
  margin-right:10px;
}
.user_btn_css{
  margin-top: 10px;
}
</style>
