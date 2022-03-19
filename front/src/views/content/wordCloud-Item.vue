<template>
  <el-card :body-style="{ padding: '0px' }" class="card-wrapper">
    <div :id="itemid" class="card-box"></div>
    <span>属性{{ parseInt(itemid.substr(-1)) + 1 }}</span>
  </el-card>
</template>

<script>
let echarts = require("echarts/lib/echarts");
require("echarts-wordcloud");
export default {
  name: "wordCloadItem",
  data() {
    return {
      chart: null,
    };
  },
  props: {
    datalist: {
      type: Array,
    },
    itemid: {
      type: String,
    },
  },
  mounted() {
    this.chart = echarts.init(document.getElementById(this.itemid));
    this.initEcharts();
    //console.log(this.datalist);
  },
  methods: {
    initEcharts() {
      var option = {
        series: [
          {
            type: "wordCloud",
            shape: "diamond",
            gridSize: 1,
            sizeRange: [5, 20],
            rotationRange: [-45, 45],
            rotationStep: 5,
            left: "center",
            top: "center",
            right: null,
            bottom: null,
            width: "100%",
            height: "100%",
            drawOutOfBound: true,
            textStyle: {
              color: function () {
                return (
                  "rgb(" +
                  [
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                  ].join(",") +
                  ")"
                );
              },
            },
            data: this.datalist,
          },
        ],
      };
      this.chart.setOption(option);
    },
  },
};
</script>


<style lang='scss' scoped>
.card-wrapper {
  display: inline-block;
  margin: 10px 20px;
  .card-box {
    //background-color: aqua;
    height: 250px;
    width: 250px;
  }
  span {
    display: block;
    text-align: center;
  }
}
</style>