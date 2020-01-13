<template>
  <v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="white" black :class="{'activebtn':instatus}" v-on="on"> {{ Loginstatus }} </v-btn>
      </template>

      <v-card>
        <v-form ref="form" v-model="valid" lazy-validation class="form">
          <v-text-field v-model="username" :counter="10" :rules="nameRules" label="ID" required />
          <v-text-field v-model="password" :rules="passwordRules" label="PASSWORD" type="password" required />
          <v-card-actions>
            <div class="flex-grow-1" />
            <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" text @click="onSubmit">Login</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
    <v-flex>
      <v-layout>
        <v-btn color="white" :class="{'activebtn':outstatus}" @click="logout"> {{ Loginstatus }} </v-btn>
      </v-layout>
    </v-flex>
  </v-row>
</template>

<script>
import api from '../../api'
import router from "../../router";
  export default {
    data: () => ({
      dialog: false,
      show3: false,
      ndata:"",
      valid: true,
      username: '',
      userid: 0,
      instatus:false,
      outstatus:true,
      Loginstatus: "login",
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'password is required',
      ],
      params:{

      },
    }),
    mounted:function(){
      if(sessionStorage.getItem("name")!=null){
        this.Loginstatus="logout";
        this.instatus=true;
        this.outstatus=false;
      }
    },
    methods: {
      onSubmit: function() {
        this.params = {
          username:this.username,
          password:this.password,
        };
        if(this.Loginstatus=="login")
          this.logintest()
        else if(this.Loginstatus=="logout")
          this.logouttest();
      },
      async logintest(){
        var dat =await api.login(this.params);
        if(dat.data.data==200){
          this.dialog = false;
          this.Loginstatus = "logout"
          this.instatus=!this.instatus
          this.outstatus=!this.outstatus
          this.$store.name =this.username
          this.$store.uid = dat.data.uid
          sessionStorage.setItem("name", this.username);
          sessionStorage.setItem("uid", dat.data.uid);
          if(this.period!=null&&this.period!="undefined")
            sessionStorage.setItem("period", this.period);
          alert("로그인 되셨습니다.")
          location.href='/'
        }
        else if(dat.data==201){
          alert("로그인 실패 !")
        }
      },
      logout(){
        this.Loginstatus ="login"
        this.instatus=!this.instatus
        this.outstatus=!this.outstatus
        this.$store.name =""
        sessionStorage.removeItem("name")
        sessionStorage.removeItem("period")
        alert("로그아웃 되셨습니다.")
        location.href='/'
      },
      goTo: function(path) {
        router.push({ name: path });
      },

  }

}
</script>
<style>
.form {
  margin: 5px;
}
.activebtn{
  display:none;
}
</style>
