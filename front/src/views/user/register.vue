<template>
  <div class="site-wrapper site-page--register">
    <div class="site-content__wrapper">
      <div class="content-main" v-loading="loading">
        <h3 class="content-title">用户注册</h3>
        <el-form
          :model="dataForm"
          :rules="dataRule"
          ref="dataForm"
          label-width="80px"
          @keyup.enter.native="dataFormRegister()"
          status-icon
        >
          <el-form-item prop="userName" label="用户账号">
            <el-input
              v-model="dataForm.userName"
              placeholder="用户名称"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item prop="email" label="用户邮箱">
            <el-input
              v-model="dataForm.email"
              placeholder="电子邮箱地址"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password1" label="输入密码">
            <el-input
              v-model="dataForm.password1"
              placeholder="请输入密码"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item prop="password2" label="确认密码">
            <el-input
              v-model="dataForm.password2"
              placeholder="请确认密码"
              show-password
            ></el-input>
          </el-form-item>
          <div class="footer-content label-width">
            <el-button type="primary" @click="dataFormRegister()"
              >注册</el-button
            >
            <el-button size="medium" @click="retrunBtn()">取消</el-button>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.dataForm.password2 !== "") {
          this.$refs.dataForm.validateField("password2");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.dataForm.password1) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      dataForm: {
        userName: "",
        email: "",
        password1: "",
        password2: "",
      },
      dataRule: {
        userName: [
          { required: true, message: "帐号不能为空", trigger: "blur" },
        ],
        email: [
          { required: true, message: "邮箱不能为空", trigger: "blur" },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["blur", "change"],
          },
        ],
        password1: [{ validator: validatePass, trigger: "blur" }],
        password2: [{ validator: validatePass2, trigger: "blur" }],
      },
      loading: false
    };
  },
  methods: {
    retrunBtn() {
      this.$router.push({ name: "login" });
    },
    dataFormRegister() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          this.loading = true
          this.$http({
            url: "/register",
            method: "post",
            data: {
              u_name: this.dataForm.userName,
              password: this.dataForm.password1,
              email: this.dataForm.email,
            },
          }).then(({ data }) => {
            if (data) {
              if (data.code == 0) {
                this.$message.success("恭喜注册成功！");
                this.$router.replace({ name: "login" });
              } else {
                this.$message.error(data.msg);
              }
            }
            this.loading = false
          });
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.label-width {
  padding-left: 80px;
}
.el-button {
  //el-button
  width: 130px;
}
</style>