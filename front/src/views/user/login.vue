<template>
  <div class="site-wrapper site-page--login">
    <div class="site-content__wrapper">
      <div class="content-main">
        <h3 class="content-title">用户登录</h3>
        <el-form
          :model="dataForm"
          :rules="dataRule"
          ref="dataForm"
          @keyup.enter.native="dataFormSubmit()"
          status-icon
        >
          <el-form-item prop="userName">
            <el-input
              v-model="dataForm.userName"
              placeholder="用户名"
              clearable
              prefix-icon="el-icon-s-custom"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model="dataForm.password"
              placeholder="密码"
              show-password
              prefix-icon="el-icon-info"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              class="content-btn-submit"
              type="primary"
              @click="dataFormSubmit()"
              >登录</el-button
            >
          </el-form-item>
          <div class="footer-content">
            <span style="font-size: 14px">
              没有账号？
              <router-link :to="{ path: '/register' }">立即注册</router-link>
            </span>
            <span class="span-a"
              ><a @click="forgetPasswordHandle()">忘记密码</a></span
            >
          </div>
        </el-form>
      </div>
    </div>
    <!-- 弹窗, 忘记密码 -->
    <forget-pwd v-if="forgetPassowrdVisible" ref="forgetPassowrd"></forget-pwd>
  </div>
</template>

<script>
import forgetPwd from "./forgetPwd.vue";
export default {
  data() {
    return {
      dataForm: {
        userName: '',
        password: "",
      },
      dataRule: {
        userName: [
          { required: true, message: "帐号不能为空", trigger: "blur" },
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
      },
      forgetPassowrdVisible: false,
    };
  },
  components: {
    forgetPwd,
  },
  methods: {
    dataFormSubmit() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          this.$http({
            url: "/login",
            method: "post",
            data: {
              u_name: this.dataForm.userName,
              password: this.dataForm.password,
            },
          }).then(({ data }) => {
            if (data) {
              if (data.code === 0) {
                this.$message.success("登录成功");
                //this.$cookie.set('u_id', data.data.u_id)
                this.$router.push({ name: "home" });
                //console.log('login push home ')
              } else {
                this.$message.error(data.msg);
              }
            } else {
              this.$message.error("未知错误");
            }
          });
        }
      });
    },
    forgetPasswordHandle() {
      this.forgetPassowrdVisible = true;
      this.$nextTick(() => {
        this.$refs.forgetPassowrd.init();
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.span-a {
  cursor: pointer;
}
</style>
