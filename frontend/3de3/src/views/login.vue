<template>
  <div class="home">
    <b-container>
      <b-row>
        <div class="col-5"></div>
        <div class="col-2">
          <img class="img-fluid" src="../assets/3de3.png" alt="3de3 Guatemala" />
        </div>
        <div class="col-5"></div>
      </b-row>
      <b-row id="login-row" class="justify-content-center align-items-center">
        <div id="login-column" class="col-md-6">
          <div id="login-box" class="col-md-12">
            <b-form id="login-form" class="form" action="" method="post">
              <h3 class="text-center text-info">Ingreso administrativo</h3>
              <div class="form-group">
                <label for="username" class="text-info">Usuario:</label><br>
                <b-form-input type="text" name="username" id="username" class="form-control" />
              </div>
              <div class="form-group">
                <label for="password" class="text-info">Contraseña:</label><br>
                <b-form-input type="text" name="password" id="password" class="form-control" />
              </div>
              <div class="form-group">
                <b-button type="submit" class="btn-submit btn-lg">Enviar</b-button>
              </div>
            </b-form>
          </div>
      </div>
      </b-row>
    </b-container>
  </div>
</template>

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
