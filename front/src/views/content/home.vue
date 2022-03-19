<template>
  <div>
    <div>
      <div class="category-content">
        <div class="category-title">类别：</div>
        <div class="list-wrapper">
          <span
            v-for="genre in genresList"
            :key="genre.g_id"
            :class="curGenresId === genre.g_id ? 'actived' : ''"
            class="category-box"
            @click="changeEvent(genre.g_id, 'curGenresId')"
          >
            {{ genre.g_name }}
          </span>
        </div>
      </div>

      <div class="category-content">
        <span class="category-title">国家：</span>
        <div class="list-wrapper">
          <span
            v-for="country in countryList"
            :key="country.c_id"
            :class="curCountryId === country.c_id ? 'actived' : ''"
            class="category-box"
            @click="changeEvent(country.c_id, 'curCountryId')"
          >
            {{ country.c_name }}
          </span>
        </div>
      </div>
    </div>

    <div class="list-content">
      <movie-item
        v-for="item in filmList"
        :key="item.m_id"
        :item="item"
        :width="itemWidth"
      />
    </div>

    <div class="page-content">
      <el-pagination
        background
        layout="total, prev, pager, next"
        :page-size="curSize"
        :page-count="pageCount"
        :current-page.sync="curPage"
        :total="total"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import MovieItem from "./movie-item.vue";
export default {
  data() {
    return {
      curGenresId: -1,
      curCountryId: -1,
      curPage: 1,
      curSize: 14,
      itemWidth: 0,
      total: 0,
      genresList: [],
      countryList: [],
      filmTimeList: [],
      filmList: [],
    };
  },
  computed: {
    pageCount() {
      return Math.ceil(this.total / this.curSize + (this.total % this.curSize));
    },
  },
  components: {
    MovieItem,
  },
  mounted() {
    this.getGneresList();
    this.getCountryList();
    this.getFilmList();
    //this.getFilmTimeList()
    this.itemWidth = Math.ceil(100 / (this.curSize / 8));
    //console.log(this.itemWidth);
  },
  created() {
    //console.log('home')
  },
  methods: {
    getGneresList() {
      this.$http.get("/get_genres_list").then(({ data }) => {
        if (data.data) {
          this.genresList = [{ g_id: -1, g_name: "all" }].concat(data.data);
        }
      });
    },
    getCountryList() {
      this.$http.get("/get_country_list").then(({ data }) => {
        if (data.data) {
          this.countryList = [{ c_id: -1, c_name: "all" }].concat(data.data);
        }
      });
    },
    getFilmTimeList() {
      this.$http.get("/get_filmtime_list").then(({ data }) => {
        this.fileTimeList = data.data;
      });
    },
    getFilmList() {
      this.$http({
        url: "/get_film_list",
        method: "post",
        data: {
          g_id: this.curGenresId,
          c_id: this.curCountryId,
          limit: this.curSize,
          offset: (this.curPage - 1) * this.curSize,
        },
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.filmList = data.data.list;
          this.total = data.data.total;
          //console.log(this.filmList);
        }
      });
    },

    changeEvent(new_id, key_id) {
      if (this[key_id] !== new_id) {
        this[key_id] = new_id;
        //console.log(this[key_id]);
        this.getFilmList();
      }
    },

    handleCurrentChange(val) {
      this.getFilmList();
      console.log(this.filmList);
    },
  },
};
</script>

<style lang='scss' scoped>
.category-content {
  font-size: 20px;
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  vertical-align: middle;
  text-align: center;

  .category-title {
    float: left;
    width: 8%;
    vertical-align: middle;
    text-align: center;
    //padding-top: 10px;
  }
  .list-wrapper {
    height: 40px;
    white-space: nowrap;
    display: inline-block;
    width: 92%;
    overflow-x: auto;
    overflow-y: hidden;
    .category-box {
      display: inline-block;
      width: 100px;
      //margin: 10px;
      overflow-x: hidden;
    }
    &::-webkit-scrollbar {
      display: none;
    }
  }

  .actived {
    color: #fff;
    background-color: #2286d8;
    border-radius: 2px;
  }
}

.list-content {
  // width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  justify-items: start;
  text-align: justify;
  //margin-top: 20px;
}
.page-content {
  text-align: center;
}
</style>
