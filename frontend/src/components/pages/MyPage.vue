<template>
  <v-container class="backcolor-portfolios">
    <MyPageUpdate />
    <br>
    <MyPageSubscribe />
    <br>
    <MyPageList />
    <br>
  </v-container>
</template>

<script>
import MyPageUpdate from "../MyPage/MyPageUpdate"
import MyPageList from "../MyPage/MyPageList"
import MyPageSubscribe from "../MyPage/MyPageSubscribe"

export default {
  components : {
    MyPageUpdate,
    MyPageList,
    MyPageSubscribe
  },
  data: () => ({
      username :sessionStorage.getItem("name"),
  }),
  created() {
    this.checks(this.username)
  },
  methods: {
    checks: function() {
      if(this.username == null) {
        this.$router.push('/')
      }
    }
  }
}

</script>
