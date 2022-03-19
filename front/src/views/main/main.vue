<template>
  <div
    v-loading.fullscreen.lock="loading"
    element-loading-text="拼命加载中"
    class="site-wrapper"
    :class="{ 'site-sidebar--fold': sidebarFold }"
  >
    <template v-if="!loading">
      <main-navbar />
      <main-sidebar />
      <div
        :style="{ 'min-height': documentClientHeight + 'px' }"
        class="site-content__wrapper"
      >
        <main-content v-if="!$store.state.common.contentIsNeedRefresh" />
      </div>
    </template>
  </div>
</template>

<script>
import MainNavbar from "./main-navbar.vue";
import MainSidebar from "./main-sidebar.vue";
import MainContent from "./main-content.vue";

export default {
  data() {
    return {
      loading: false,
    };
  },
  components: {
    MainNavbar,
    MainSidebar,
    MainContent,
  },
  computed: {
    documentClientHeight: {
      get() {
        return this.$store.state.common.documentClientHeight;
      },
      set(val) {
        this.$store.commit("common/updateDocumentClientHeight", val);
      },
    },
    sidebarFold: {
      get() {
        return this.$store.state.common.sidebarFold;
      },
    },
    userId: {
      get() {
        return this.$store.state.user.id;
      },
      set(val) {
        this.$store.commit("user/updateId", val);
      },
    },
    userName: {
      get() {
        return this.$store.state.user.name;
      },
      set(val) {
        this.$store.commit("user/updateName", val);
      },
    },
  },
  created() {
    this.getUserInfo();
    //console.log('main')
  },
  mounted() {
    this.resetDocumentClientHeight();
  },
  methods: {
    // 重置窗口可视高度
    resetDocumentClientHeight() {
      this.documentClientHeight = document.documentElement["clientHeight"];
      window.onresize = () => {
        this.documentClientHeight = document.documentElement["clientHeight"];
      };
    },
    // 获取当前管理员信息
    getUserInfo() {
      this.$http({
        url: "/get_user_info",
        method: "get",
        params: {},
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.loading = false;
          this.userId = data.data.userId;
          this.userName = data.data.userName;
        }
      });
    },
  },
};
</script>
