<!-- 유저 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-1">Member Search</div>
        <br>
        <UserSearchForm :submit="searchUsers" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs12>
        <UserList :user-list-cards="userList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserSearchForm from "../UserPage/UserSearchForm";
import UserList from "../UserPage/UserList";
export default {
  components: {
    UserList,
    UserSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      userList: state => state.data.userSearchList
    })
  },
  methods: mapActions("data", ["searchUsers"])
};
</script>
