<template>
  <v-hover v-slot:default="{ hover }">
    <v-card style="width:400px" :elevation="hover ? 8 : 2" @click="onDetail">
      <v-flex text-center>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="headline">
              {{ id }}
            </v-list-item-title>
            <v-list-item-subtitle>
              성별 : {{ gender }} 나이 :{{ age }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-flex>
      <v-dialog
        v-model="dialog"
        max-width="600"
      >
        <UserDetailCard
          :id="id"
          :gender="gender"
          :age="age"
          :occupation="occupation"
        />
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>
import UserDetailCard from "./UserDetailCard"
export default {
  components: {
      UserDetailCard
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    gender: {
      type: String,
      default: ""
    },
    occupation: {
      type: String,
      default: ""
    },
    age: {
      type: Number,
      default: 0
    },
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
