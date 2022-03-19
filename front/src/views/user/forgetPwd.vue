<template>
  <el-dialog
    width="30%"
    title="修改密码"
    :visible.sync="visible"
    :append-to-body="true"
  >
    <el-form
      :model="dataForm"
      :rules="dataRule"
      ref="dataForm"
      @keyup.enter.native="dataFormSubmit()"
      label-width="80px"
    >
      <el-form-item label="账号" prop="userName">
        <el-input type="input" v-model="dataForm.userName"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input type="email" v-model="dataForm.email"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="code">
        <el-input type="input" v-model="dataForm.code">
          <el-button
            slot="append"
            type="primary"
            @click="codeSubmit()"
            :disabled="disabled"
            >{{ btnTxt }}</el-button
          >
        </el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="newPassword">
        <el-input
          type="password"
          show-password
          v-model="dataForm.newPassword"
        ></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="confirmPassword">
        <el-input
          type="password"
          show-password
          v-model="dataForm.confirmPassword"
        ></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="visible = false">取消</el-button>
      <el-button type="primary" @click="dataFormSubmit()">确定</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  data() {
    var validateConfirmPassword = (rule, value, callback) => {
      if (this.dataForm.newPassword !== value) {
        callback(new Error("确认密码与新密码不一致"));
      } else {
        callback();
      }
    };
    return {
      visible: false,
      btnTxt: "获取验证码",
      disabled: false,
      dataForm: {
        userName: "",
        email: "",
        code: "",
        newPassword: "",
        confirmPassword: "",
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
        code: [{ required: true, message: "新密码不能为空", trigger: "blur" }],
        newPassword: [
          { required: true, message: "新密码不能为空", trigger: "blur" },
        ],
        confirmPassword: [
          { required: true, message: "确认密码不能为空", trigger: "blur" },
          { validator: validateConfirmPassword, trigger: "blur" },
        ],
      },
    };
  },
  computed: {},
  methods: {
    // 初始化
    init() {
      this.visible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].resetFields();
      });
    },
    // 表单提交
    dataFormSubmit() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          this.$http({
            url: "forget_password",
            method: "post",
            data: {
              u_name: this.dataForm.userName,
              code: this.dataForm.code,
              newPassword: this.dataForm.newPassword,
            },
          }).then(({ data }) => {
            if (data && data.code === 0) {
              this.$message({
                message: "操作成功",
                type: "success",
                duration: 1000,
                onClose: () => {
                  this.visible = false;
                  // this.$nextTick(() => {
                  //   this.mainTabs = [];
                  //   clearLoginInfo();
                  //   this.$router.replace({ name: "login" });
                  // });
                },
              });
            } else {
              this.$message.error(data.msg);
            }
          });
        }
      });
    },
    codeSubmit() {
      const p1 = new Promise((resolve) => {
        this.$refs["dataForm"].validateField("userName", (err) => {
          resolve(err);
        });
        resolve();
      });
      const p2 = new Promise((resolve) => {
        this.$refs["dataForm"].validateField("email", (err) => {
          resolve(err);
        });
        resolve();
      });
      Promise.all([p1, p2]).then((result) => {
        if (!result.join("")) {
          let time = 30;
          this.btnTxt = time + "秒后重试";
          this.disabled = true;
          let s = setInterval(() => {
            time--;
            this.btnTxt = time + "秒后重试";
          }, 1000);
          let s1 = setTimeout(() => {
            clearInterval(s);
            this.disabled = false;
            this.btnTxt = "获取验证码";
          }, 1000 * 30);
          this.$http({
            url: "send_email",
            method: "post",
            data: {
              u_name: this.dataForm.userName,
              email: this.dataForm.email,
            },
          }).then(({ data }) => {
            if (data && data.code === 0) {
              this.$message.success("验证码已发送到您邮箱，请查收！");
            } else {
              this.$message.error(data.msg);
            }
          });
        }
      });
    },
  },
};
</script>

<style lang='scss' scoped>
.email-button {
  display: flex;
  flex-wrap: nowrap;
}
</style>