
<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on }">
      <span v-on="on">Question</span>
    </template>
    <v-card>
      <v-form ref="form">
        <v-card-title>
          <span class="headline">Question</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="form.name" label="아이디" required />
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="form.title" label="제목을 입력하세요.*" required />
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="form.content" label="내용을 입력하세요.*" required />
              </v-col>
              <v-col cols="12" class="reply_css">
                <v-text-field v-model="form.replys" label="내용을 입력하세요.*" required />
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1" />
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="onSubmit">Save</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import api from '../../api'
  export default {
    data () {
      return {
        dialog: false,
        form: {
          name : sessionStorage.getItem("name"),
          title : "",
          content : "",
          replys : ""
        }
      }
    },
    methods: {
      onSubmit: function() {
        api.question(this.form);
        this.dialog = false
    },
    }
  }
</script>

<style>
.reply_css {
  display: none;
}
</style>
