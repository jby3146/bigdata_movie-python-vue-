<template>
  <v-card>
    <v-form ref="form">
      <v-card-title>
        <span class="headline">영화 추천 서비스 구독</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <p v-if="recomend_day" class="font-weight-bold">구독 종료 기간. {{ period }}</p>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn v-if="!recomend_day" color="blue darken-1" text @click="onSubscribe">구독 서비스 시작</v-btn>
        <v-btn v-else color="blue darken-1" text @click="delSubscribe">구독 서비스 취소</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import api from '../../api'
import { eventBus } from "../../store/index.js";

  export default {
    data: () => ({
        username: sessionStorage.getItem("name"),
        period: sessionStorage.getItem("period"),
        recomend_day:false
    }),
    created(){
      if(this.period!=null&&this.period!="undefined"){
        this.recomend_day=true
      }
      else{
        this.recomend_day=false
      }
    },
    methods:{
       async onSubscribe() {
        const params = {
          clkbtn: this.username
        }
        const resp = await api.createPeriod(params)
        this.period = resp.data[0]['period']
        this.$store.state.vuexPeriod = this.period
        eventBus.$emit("sendPeriod", this.period);
        if(this.period!=null&&this.period!="undefined"){
          sessionStorage.setItem("period", this.period);
          this.recomend_day=true
        }
        else{
          this.recomend_day=false
          sessionStorage.removeItem("period")
        }
      },
       async delSubscribe() {
        const params = {
          cancelsub: this.username
        }
        const resp = await api.createPeriod(params)
        this.period = null
        this.$store.state.vuexPeriod = null
        sessionStorage.removeItem("period")
        if(this.period!=null&&this.period!="undefined"){
          this.recomend_day=true
        }
        else{
          this.recomend_day=false
        }
        eventBus.$emit("sendPeriod", "none");
      },
    }
  }
</script>
