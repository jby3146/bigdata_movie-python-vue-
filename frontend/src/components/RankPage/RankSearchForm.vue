<template>
  <v-form ref="form">
    <v-menu
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          class="rank_search_css"
          v-on="on"
        >
          {{ title }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="Dropdown(item.title)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-menu
      v-if="title == '나이순'"
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
        >
          나이
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(year, i) in years"
                     :key="i"
                     @click="test(year)"
        >
          {{ year.title }}
        </v-list-item>
      </v-list>
    </v-menu>

    <v-container v-if="title == '나이순'">
      <v-text-field
        v-model="counting"
        label="View"
        outlined
      />
    </v-container>

    <v-menu
      v-if="title == '직업순'"
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
        >
          직업
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(job, i) in jobs"
                     :key="i"
                     @click="test(job)"
        >
          {{ job.title }}
        </v-list-item>
      </v-list>
    </v-menu>

    <v-container v-if="title == '직업순'">
      <v-text-field
        v-model="counting"
        label="View"
        outlined
      />
    </v-container>

    <v-menu
      v-if="title == '성별'"
      :open-on-hover="true"
      :offset-y="true"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
        >
          {{ gender }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(gender, i) in genders"
                     :key="i"
                     @click="test(gender)"
        >
          {{ gender.title }}
        </v-list-item>
      </v-list>
    </v-menu>

    <v-container v-if="title == '성별'">
      <v-text-field
        v-model="counting"
        label="View"
        outlined
      />
    </v-container>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
      items: [
        { title: '나이순' },
        { title: '직업순' },
        { title: '성별' },
      ],
      title: "select",
      search:"",
      gender: "성별 선택",
      params: {

      },
      years: [
        { title: "18-" , value: "1"},
        { title: "18-24" , value: "18"},
        { title: "25-34" , value: "25"},
        { title: "35-44" , value: "35"},
        { title: "45-49" , value: "45"},
        { title: "50-55 " , value: "50"},
        { title: "56+" , value: "56"}
      ],
      jobs: [
        { title: "학업/교육자", value: "academic/educator" },
        { title: "아티스트", value: "artist" },
        { title: "임원/관리자", value: "clerical/admin" },
        { title: "대학/학년생", value: "college/grad student" },
        { title: "의사/건강 관리", value: "doctor/health care" },
        { title: "고객 서비스", value: "customer service" },
        { title: "임원/관리", value: "executive/managerial" },
        { title: "주부", value: "homemaker" },
        { title: "농부", value: "farmer" },
        { title: "학생", value: "K-12 student" },
        { title: "변호사", value: "lawyer" },
        { title: "프로그래머", value: "programmer"  },
        { title: "퇴직", value: "retired" },
        { title: "판매/마케팅", value: "sales/marketing"  },
        { title: "과학자", value: "scientist"  },
        { title: "자영업자", value: "self-employed" },
        { title: "기술자/엔지니어", value: "technician/engineer" },
        { title: "상인/장인", value: "tradesman/craftsman" },
        { title: "실직", value: "unemployed" },
        { title: "작가", value: "writer" },
        { title: "기타", value: "other" }
      ],
      genders: [
        { title: "남성", value: "M" },
        { title: "여성", value: "F" }
      ],
      val: "",
      counting: 1
    }),
  methods: {
    test : function(select) {
      this. val = select.value
      this.onSubmit()
    },
    onSubmit: function() {

      switch (this.title) {
        case "성별":
          this.params = {
            sel: '1',
            selGender: this.val,
            counting: this.counting
          };
          break;
        case "나이순":
          this.params = {
            sel: '2',
            selAge: this.val,
            counting: this.counting
          };
          break;
        case "직업순":
          this.params = {
            sel: '3',
            selOccupation: this.val,
            counting: this.counting
          };
          break;
      }

      this.submit(this.params);
    },

    Dropdown: function(title) {
      this.title = title;
    }
  }
};
</script>

<style>
.rank_search_css {
  margin-right: 10px;
}
</style>
