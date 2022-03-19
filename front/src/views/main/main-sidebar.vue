<template>
  <aside class="site-sidebar" :class="'site-sidebar--' + sidebarLayoutSkin">
    <div class="site-sidebar__inner">
      <el-menu
        :default-active="menuActiveName || 'home'"
        :collapse="sidebarFold"
        :collapseTransition="false"
        class="site-sidebar__menu"
      >
        <el-menu-item index="home" @click="checkpush('home')">
          <i class="el-icon-s-home"></i>
          <span slot="title">首页</span>
        </el-menu-item>
        <el-submenu index="recommend">
          <template slot="title">
            <i class="el-icon-star-on"></i>
            <span>个性化推荐</span>
          </template>
          <el-menu-item index="rec-list" @click="checkpush('rec-list')">
            <i class="el-icon-menu"></i>
            <span slot="title">推荐列表</span>
          </el-menu-item>
          <el-menu-item index="his-data" @click="checkpush('his-data')">
            <i class="el-icon-s-data"></i>
            <span slot="title">历史数据分析</span>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </aside>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    sidebarLayoutSkin: {
      get() {
        return this.$store.state.common.sidebarLayoutSkin;
      },
    },
    sidebarFold: {
      get() {
        return this.$store.state.common.sidebarFold;
      },
    },
    menuActiveName: {
      get() {
        return this.$store.state.common.menuActiveName;
      },
      set(val) {
        this.$store.commit("common/updateMenuActiveName", val);
      },
    },
    mainTabs: {
      get() {
        return this.$store.state.common.mainTabs;
      },
      set(val) {
        this.$store.commit("common/updateMainTabs", val);
      },
    },
    mainTabsActiveName: {
      get() {
        return this.$store.state.common.mainTabsActiveName;
      },
      set(val) {
        this.$store.commit("common/updateMainTabsActiveName", val);
      },
    },
  },
  watch: {
    $route: "routeHandle",
  },
  methods: {
    // 路由操作
    routeHandle(route) {
      // console.log(route)
      // if (route.meta.isTab) {
      //   // tab选中, 不存在先添加
      //   var tab = this.mainTabs.filter(item => item.name === route.name)[0]
      //   if (!tab) {
      //     tab = {
      //       menuId: route.meta.menuId || route.name,
      //       name: route.name,
      //       title: route.meta.title,
      //       type: isURL(route.meta.iframeUrl) ? 'iframe' : 'module',
      //       iframeUrl: route.meta.iframeUrl || '',
      //       params: route.params,
      //       query: route.query
      //     }
      //     this.mainTabs = this.mainTabs.concat(tab)
      //   }
      //   this.menuActiveName = tab.menuId + ''
      //   this.mainTabsActiveName = tab.name
      // }
      this.$store.dispatch("common/addMainTabs", route);
    },
    checkpush(routeName) {
      //console.log(routeName,document.cookie)
      //console.log(this.$cookie,this.$cookie.get('u_id'))
      if (!this.$cookie.get('u_id')) {
        this.$message.error("前先登录");
        this.$router.replace({ name: "home" });
      }
      this.$router.push({ name: routeName }).catch((err) => {});
    },
  },
};
</script>
