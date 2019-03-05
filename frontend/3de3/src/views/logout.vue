<template>
</template>
<script>
export default {
  name: 'logout',
  methods:{
    logmeout: function() {
      console.log("ejecutando el logoutn");
      this.$store.dispatch('nullSession');
    }

  },
  beforeMount(){
    this.logmeout();
  }
}
</script>
<style scoped>
body {
  margin: 0;
  padding: 0;
  background-color: #17a2b8;
  height: 100vh;
  color: #0096DB;
}
.text-info {
  color: #0096DB !important;
}
#login .container #login-row #login-column #login-box {
  margin-top: 120px;
  max-width: 600px;
  height: 320px;
  border: 1px solid #9C9C9C;
  background-color: #EAEAEA;
}
#login .container #login-row #login-column #login-box #login-form {
  padding: 20px;
}
#login-row {
  margin-top:45px;
}
.btn-submit {
  background-color: #EF2466;
  border-color: #EF2466;
}
</style>
