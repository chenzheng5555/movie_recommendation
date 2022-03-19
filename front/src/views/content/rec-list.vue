<template>
  <div class="list-content">
    <movie-item
      v-for="item in filmList"
      :key="item.m_id"
      :item="item"
      :width="itemWidth"
    />
  </div>
</template>

<script>
import MovieItem from "./movie-item.vue";
export default {
  data() {
    return {
      total: 0,
      filmList: [],
      itemWidth: 0,
    };
  },
  mounted() {
    this.getRecList();
  },
  components: {
    MovieItem,
  },

  methods: {
    getRecList() {
      this.$http({
        url: "/get_rec_list",
        method: "get",
        params: {},
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.filmList = data.data.list;
          this.total = data.data.total;
          //console.log(this.filmList);
        }
      });
    },
  },
};
</script>

<style lang='scss' scoped>
.list-content {
  // width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  justify-items: start;
  text-align: justify;
}
</style>
