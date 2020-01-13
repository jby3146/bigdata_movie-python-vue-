<template>
  <v-app id="app" class="backcolor-portfolios">
    <HeaderPage />
  </v-app>
</template>

<script>
import HeaderPage from "./components/HeaderPage/HeaderPage";

export default {
  components: {
    HeaderPage
  },
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
.backcolor-port {
  background-image: -webkit-gradient(
    linear,
    left top, left bottom,
    from(#EAE4DF),
    color-stop(50%, #FFFFFF),
    color-stop(75%, #EAE4DF)
  );
}
.backcolor-portfolios {
  background-image: -webkit-gradient(
    linear,
    left top, left bottom,
    from(#F0F0EE),
    color-stop(50%, #EAE4DF),
    color-stop(75%, #DACDC8)
  );
}
</style>
