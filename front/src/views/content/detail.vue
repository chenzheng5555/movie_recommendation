<template>
  <div>
    <el-card class="info-wrapper">
      <div class="image-box">
        <el-image
          class="image-wrapper"
          :src="$route.params.pictureurl"
          fit="fill"
        >
        </el-image>
      </div>

      <div class="info-box">
        <h1 class="title-box">{{ $route.params.title }}</h1>

        <div class="category-box">
          <h3>Actors:</h3>
          <div class="actor-div">
            <span>{{ actors }}</span>
          </div>
            
        </div>
        <div class="category-box">
          <h3>Directors:</h3>
          <span>{{ directors }}</span>
        </div>

        <div class="film-country">
          <div class="category-box film">
            <h3>Filming year:</h3>
            <span>{{ $route.params.filming_year }}</span>
          </div>
          <div class="category-box">
            <h3>Country:</h3>
            <span>{{ country }}</span>
          </div>
        </div>

        <div class="category-box">
          <h3>Genres:</h3>
          <span>{{ genres }}</span>
        </div>
      </div>
    </el-card>

    <el-card class="tag-wrapper">
      <h2>自定义标签</h2>
      <div class="tag-box" v-for="(item, index) in user_tags" :key="item.title">
        <span
          :style="'background-color:' + `rgba(9, 226, 107,${item.count / 20})`"
          >x{{ item.count }}</span
        >
        <span>{{ item.title }}</span>
        <span class="handle-tag" @click="deleteTag(index)">x</span>
      </div>
      <el-input
        class="input-box"
        v-if="inputVisible"
        v-model="inputValue"
        ref="saveTagInput"
        @keyup.enter.native="handleInputConfirm"
        @blur="handleInputConfirm"
      >
      </el-input>
      <el-button v-else @click="showInput" class="but-box">+添加标签</el-button>
      <h2>社区标签</h2>
      <div>
        <div
          class="tag-box"
          v-for="(item, index) in other_tags"
          :key="item.title"
        >
          <span
            :style="
              'background-color:' + `rgba(9, 226, 107,${item.count / 20})`
            "
            >x{{ item.count }}</span
          >
          <span>{{ item.title }}</span>
          <span class="handle-tag" @click="addTag(index)">+</span>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      actors: "",
      directors: "",
      country: "",
      genres: "",
      inputVisible: false,
      inputValue: "",
      other_tags: [],
      user_tags: [],
    };
  },
  created() {
    this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        //console.log(toParams, previousParams);
        if (this.$route.name === "detail") {
          this.getinfo();
        }
      }
    );
    this.getinfo();
  },
  methods: {
    getinfo() {
      this.get_country();
      this.get_genres();
      this.get_actors();
      this.get_directors();
      this.get_tags();
    },
    get_country() {
      this.$http({
        url: "/get_country_by_id",
        method: "get",
        params: {
          m_id: this.$route.params.m_id,
        },
      }).then(({ data }) => {
        this.country = data.data.toString();
      });
    },
    get_genres() {
      this.$http({
        url: "/get_genres_by_id",
        method: "get",
        params: {
          m_id: this.$route.params.m_id,
        },
      }).then(({ data }) => {
        this.genres = data.data.toString();
      });
    },
    get_actors() {
      this.$http({
        url: "/get_actors_by_id",
        method: "get",
        params: {
          m_id: this.$route.params.m_id,
        },
      }).then(({ data }) => {
        this.actors = data.data.toString();
      });
    },
    get_directors() {
      this.$http({
        url: "/get_directors_by_id",
        method: "get",
        params: {
          m_id: this.$route.params.m_id,
        },
      }).then(({ data }) => {
        this.directors = data.data.toString();
      });
    },
    get_tags() {
      this.$http({
        url: "/get_tags_by_id",
        method: "get",
        params: {
          m_id: this.$route.params.m_id,
        },
      }).then(({ data }) => {
        this.user_tags = data.data.user_tags;
        this.other_tags = data.data.other_tags;
        //console.log(this.user_tags, this.other_tags);
      });
    },
    addMysqlTag(tag_name) {
      this.$http({
        url: "/add_user_movie_tag",
        method: "post",
        data: {
          m_id: this.$route.params.m_id,
          t_name: tag_name,
        },
      }).then(({ data }) => {
        if (data && data.code === 0) {
          //console.log("添加成功", data.data);
          const tmp = { title: tag_name, count: data.data.count };
          const j = this.user_tags.findIndex((item) => item.count <= tmp.count);
          if (j === -1) {
            this.user_tags.push(tmp);
          } else {
            this.user_tags.splice(j, 0, tmp);
          }
        }
      });
    },
    deleteMysqlTag(tag_name) {
      this.$http({
        url: "/delete_user_movie_tag",
        method: "post",
        data: {
          m_id: this.$route.params.m_id,
          t_name: tag_name,
        },
      }).then(({ data }) => {
        if (data && data.code === 0) {
          //console.log("删除成功");
          if (data.data.count > 0) {
            const tmp = { title: tag_name, count: data.data.count };
            const j = this.other_tags.findIndex(
              (item) => item.count <= tmp.count
            );
            this.other_tags.splice(j, 0, tmp);
          }
        }
      });
    },
    /***********************/
    addTag(i) {
      var tmp = this.other_tags[i];
      tmp.count += 1;
      this.other_tags.splice(i, 1);
      this.addMysqlTag(tmp.title);
    },
    deleteTag(i) {
      var tmp = this.user_tags[i];
      this.user_tags.splice(i, 1);
      this.deleteMysqlTag(tmp.title);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick((_) => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        let i = this.user_tags.findIndex((item) => item.title === inputValue);
        if (i === -1) {
          let j = this.other_tags.findIndex(
            (item) => item.title === inputValue
          );
          //console.log(j, inputValue);
          if (j !== -1) this.other_tags.splice(j, 1);
          this.addMysqlTag(inputValue);
        }
      }
      this.inputVisible = false;
      this.inputValue = "";
    },
  },
};
</script>


<style lang='scss' scoped>
.info-wrapper {
  height: 300px;
  .image-box {
    width: 15%;
    float: left;
    .image-wrapper {
      height: 250px;
      width: 100%;
    }
  }
  .info-box {
    float: right;
    width: 80%;
  }
}
.title-box {
  color: rgb(69, 90, 146);
}
.category-box {
  //display: flex;
  white-space: nowrap;
  min-height: 40px;
  h3 {
    display: inline-block;
    width: 150px;
    margin: 0;
    font-size: 20px;
    font-family: Georgia, serif;
    color: rgb(236, 215, 27);
    vertical-align: middle;
  }
  .actor-div{
    width: 800px;  //隐藏内容滑动
    display: inline-block;
    overflow: auto;
    &::-webkit-scrollbar {
      display: none;
    }
  }
  span {
    font-size: 20px;
    vertical-align: middle;
  }
}
.film-country {
  display: flex;
  div.film {
    margin-right: 100px;
  }
}

.tag-wrapper {
  margin-top: 20px;
  //height: 350px;
  h1 {
    color: rgb(180, 163, 10);
    margin: 0;
    font-family: "Times New Roman", Times, serif;
  }
}
.input-box {
  width: 200px;
}
.but-box {
  font-size: 15px;
  line-height: 1.5;
  padding: 2px 5px;
}
.tag-box {
  display: inline-block;
  width: 250px;
  margin-bottom: 10px;
  //background-color: rgb(9, 226, 107);
  span {
    display: inline-block;
    border: 0.5px solid rgb(85, 84, 84);
    font-size: 15px;
    line-height: 1.2;
    padding: 2px 5px;
    &:first-child {
      border-right-width: 0;
    }
    &:last-child {
      border-left-width: 0;
    }
  }
  .handle-tag {
    cursor: pointer;
  }
}
</style>
