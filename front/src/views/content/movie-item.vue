<template>
  <div class="main-wrapper" @click="detailClick">
    <el-card
      shadow="hover"
      class="card-wrapper"
      :body-style="{ padding: '0px' }"
    >
      <el-image
        :src="item.pictureurl"
        fit="fill"
        class="image-wrapper"
      ></el-image>
    </el-card>
    <div class="title-wrapper">
      <span>{{ item.title }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieItem",
  data() {
    return {};
  },
  props: {
    item: {
      type: Object,
      default() {
        return {};
      },
    },
    width: {},
  },
  computed: {
    mainTabs: {
      get() {
        return this.$store.state.common.mainTabs;
      },
      set(val) {
        this.$store.commit("common/updateMainTabs", val);
      },
    },
  },
  watch: {
    $route: "handleRoute",
  },
  methods: {
    // 因为视频也用了该组件 所以需要判断
    handleRoute(route) {
      //console.log(route)
      this.$store.dispatch("common/addMainTabs", route);
    },
    detailClick() {
      //console.log(this.item);
      this.$router.push({
        name: "detail",
        params: {
          title: this.item.title,
          m_id: this.item.m_id,
          pictureurl: this.item.pictureurl,
          filming_year: this.item.filming_time,
        },
      });
      var i = this.mainTabs.findIndex((data) => {
        return data.name === "detail";
      });
      //console.log(i);
      if (i > -1) {
        this.mainTabs[i].title = this.item.title;
      }
    },
  },
};
</script>

<style lang = "scss" scped>
.main-wrapper {
  height: 240px;
  width: 12%; /*方便每行6个 */
  margin: 10px 10px;
  /* position: relative; */
  /* overflow: hidden; */
  cursor: pointer;
  line-height: 1.5;

  .card-wrapper {
    height: 200px;
    width: 100%;
    .image-wrapper {
      height: 200px;
      width: 100%;
    }
  }
  .title-wrapper {
    padding-top: 10px;
    font-size: 17px;
    height: 40px;
    width: 100%;
    text-align: center;
    line-height: 17px;
    font-family: Georgia, serif;
    font-weight: bold;
    overflow-y: hidden;
    color: rgb(21, 110, 211);
  }
}
</style>
