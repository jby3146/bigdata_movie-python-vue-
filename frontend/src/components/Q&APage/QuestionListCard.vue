<template>
  <v-hover v-slot:default="{ hover }">
    <v-card class="question_css backcolor-port" :elevation="hover ? 8 : 2" @click="onDetail">
      <v-flex>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="headline" style="padding-top:100px;">
              {{ title }}
            </v-list-item-title>
            <v-list-item-subtitle style="padding-top:100px;">
              {{ times }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-flex>
      <v-dialog
        v-model="dialog"
        max-width="600"
      >
        <QuestionDetailCard
          :name="name"
          :title="title"
          :content="content"
          :replys="replys"
          :times="times"
        />
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>
import QuestionDetailCard from "./QuestionDetailCard"
export default {
  components: {
      QuestionDetailCard
  },
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
  data () {
      return {
        dialog: false,
      }
    },
  methods: {
    onDetail: function() {
      this.dialog = !this.dialog
    },
  }
};
</script>

<style>
.question_css {
  width: 400px;
  height: 300px;
}
</style>
