<template>
  <v-card>
    <v-form ref="form">
      <v-card-title>
        <span class="headline">User Profile</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="4">
              <v-autocomplete
                v-model="form.occupation"
                :items="[ 'other' , 'academic/educator' , 'artist' , 'clerical/admin' , 'college/grad student' ,
                          'customer service' , 'doctor/health care' , 'executive/managerial' , 'farmer' , 'homemaker'
                          , 'K-12 student' , 'lawyer' , 'programmer' ,'retired','sales/marketing' ,'scientist'
                          ,'self-employed' ,'technician/engineer' ,'tradesman/craftsman' ,'unemployed' ,'writer'
                ]"
                label="Job"
              />
            </v-col>
            <v-col cols="12" sm="4">
              <v-select
                v-model="form.gender"
                :items="['M', 'F']"
                label="Gender*"
                required
              />
            </v-col>
            <v-col cols="12" sm="4" style="display:none">
              <v-text-field v-model="form.password" label="Password*" type="password" required />
            </v-col>
            <v-col cols="12" sm="4">
              <v-select
                v-model="form.age"
                label="Age*"
                :hint="`${form.age.state}, ${form.age.abbr}`"
                :items="items"
                item-text="state"
                item-value="abbr"
                persistent-hint
                single-line
              />
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.username"
                style="display:none;"
                label="User Name*"
                hint="My Name."
                persistent-hint
                required
              />
            </v-col>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn color="blue darken-1" text @click="onSubmit">Update</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import api from '../../api'
  export default {
    data: () => ({
      dialog: false,
      form: {
        username :sessionStorage.getItem("name"),
        age: "",
        gender : "",
        occupation : "",
      },
      items: [
          { state: '18 세 미만', abbr: '1' },
          { state: '18 ~ 24', abbr: '18' },
          { state: '25 ~ 34', abbr: '25' },
          { state: '35 ~ 44', abbr: '35' },
          { state: '45 ~ 49', abbr: '45' },
          { state: '50 ~ 55', abbr: '50' },
          { state: '56 ~ ', abbr: '56+' },
        ],
    }),
    methods:{
      onSubmit: function() {
        api.user_update(this.form);
    },
    }
  }
</script>
