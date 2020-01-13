<!-- 클러스터 검색 페이지 -->
<template>
  <div>
    <!-- 검색 폼 -->
    <ClusterSearchForm :submit="searchAdmin" />
    <!-- 검색 결과 -->
    <ClusterList :cluster-list="clusterList" />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ClusterList from "../ClusterPage/ClusterList"
import ClusterSearchForm from "../ClusterPage/ClusterSearchForm"

  export default {
    components: {
      ClusterList,
      ClusterSearchForm
    },
    data: () => ({
      username :sessionStorage.getItem("name")
    }),
    computed: {
      ...mapState({
        clusterList: state => state.data.adminSearchList
      })
    },
    created() {
      this.checks(this.username)
    },
    methods: {
      checks: function() {
        if(this.username != 'admin') {
          this.$router.push('/')
        }
      },
      ...mapActions("data", ["searchAdmin"]),
    }
  }
</script>

<style>
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
