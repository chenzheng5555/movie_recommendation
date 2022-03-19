<template>
  <nav class="site-navbar" :class="'site-navbar--' + navbarLayoutType">
    <div class="site-navbar__header">
      <h1
        class="site-navbar__brand"
        @click="$router.push({ name: 'home' }).catch((err) => {})"
      >
        <a class="site-navbar__brand-lg" href="javascript:;"
          >基于标签的电影推荐</a
        >
        <a class="site-navbar__brand-mini" href="javascript:;">推荐</a>
      </h1>
    </div>
    <div class="site-navbar__body clearfix">
      <!-- 折叠图标 -->
      <el-menu class="site-navbar__menu" mode="horizontal">
        <el-menu-item
          class="site-navbar__switch"
          index="0"
          @click="sidebarFold = !sidebarFold"
        >
          <i :class="sidebarFold ? 'el-icon-s-unfold' : 'el-icon-s-fold'"></i>
        </el-menu-item>
      </el-menu>

      <el-menu
        class="site-navbar__menu site-navbar__menu--right"
        mode="horizontal"
      >
        <el-menu-item class="site-navbar__avatar" index="1">
          <el-dropdown :show-timeout="0" placement="bottom">
            <span class="el-dropdown-link">
              <img src="@/assets/img/avatar.png" :alt="userName" />{{
                userName
              }}
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="updatePasswordHandle()"
                >修改密码</el-dropdown-item
              >
              <el-dropdown-item @click.native="logoutHandle()"
                >退出</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
        </el-menu-item>
      </el-menu>
    </div>
    <!-- 弹窗, 修改密码 -->
    <change-pwd v-if="updatePassowrdVisible" ref="updatePassowrd"></change-pwd>
  </nav>
</template>

<script>
import changePwd from "../user/changePwd.vue";
export default {
  data() {
    return {
      updatePassowrdVisible: false,
    };
  },
  components: {
    changePwd,
  },
  computed: {
    navbarLayoutType: {
      get() {
        return this.$store.state.common.navbarLayoutType;
      },
    },
    sidebarFold: {
      get() {
        return this.$store.state.common.sidebarFold;
      },
      set(val) {
        this.$store.commit("common/updateSidebarFold", val);
      },
    },
    userName: {
      get() {
        return this.$store.state.user.name;
      },
    },
  },
  methods: {
    // 修改密码
    updatePasswordHandle() {
      this.updatePassowrdVisible = true;
      this.$nextTick(() => {
        this.$refs.updatePassowrd.init();
      });
    },
    // 退出
    logoutHandle() {
      this.$messageBox
        .confirm(`确定进行[退出]操作?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
        .then(() => {
          // this.$http({
          //   url: this.$http.adornUrl("/sys/logout"),
          //   method: "post",
          //   data: this.$http.adornData(),
          // }).then(({ data }) => {
          //   if (data && data.code === 0) {
          //     clearLoginInfo();
          //     this.$router.push({ name: "login" });
          //   }
          // });
          //clearLoginInfo();
          this.$router.push({ name: "login" });
        })
        .catch(() => {});
    },
  },
};
</script>
