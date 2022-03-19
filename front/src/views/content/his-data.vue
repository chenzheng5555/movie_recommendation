<template>
  <div>
    <el-card class="box-wrapper" :body-style="{ padding: '0px' }">
      <div class="title-box">用户电影交互历史</div>
      <wordCloadItem
        v-for="(item, index) in movie_list"
        :key="'movie' + index"
        :itemid="'movie' + index"
        :datalist="item"
      />
    </el-card>

    <el-card class="box-wrapper" :body-style="{ padding: '0px' }">
      <div class="title-box">用户标签标注历史</div>
      <wordCloadItem
        v-for="(item, index) in tag_list"
        :key="'tag' + index"
        :itemid="'tag' + index"
        :datalist="item"
      />
    </el-card>
  </div>
</template>

<script>
import wordCloadItem from "./wordCloud-Item.vue";
export default {
  data() {
    return {
      movie_list: [],
      tag_list: [],
    };
  },
  components: { wordCloadItem },
  mounted() {
    this.getHistMovieList();
    this.getHistTagList();
  },
  methods: {
    getHistMovieList() {
      this.$http({
        url: "/get_user_movie_hist",
        method: "get",
        params: {},
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.movie_list = data.data;
          //console.log(this.movie_list);
        }
      });
    },
    getHistTagList() {
      this.$http({
        url: "/get_user_tag_hist",
        method: "get",
        params: {},
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.tag_list = data.data;
          //console.log(this.tag_list);
        }
      });
    },
  },
};
</script>

<style lang='scss' scoped>
.box-wrapper {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-around;
  margin: 10px 0;
  .title-box {
    display: inline-block;
    writing-mode: vertical-lr;
    text-align: center;
    height: 250px;
    font-size: 20px;
    color: rgb(33, 198, 248);
  }
}
</style>