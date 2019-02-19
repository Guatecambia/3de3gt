<template>
  <div class="section footer">
    <b-container>
      <b-row class="footer-links">
        <div col="col-12">
          <router-link to="/privacidad">Privacidad</router-link>
          |
          <router-link to="/faq">Preguntas Frecuentes</router-link>
          |
          <router-link to="/acerca-de">Acerca de</router-link>
        </div>
      </b-row>
      <b-row class="footer-logos">
        <div class="col-4"></div>
        <div class="col-4">
          <b-row>
            <div class="col-6">
              <a href="http://accionciudadana.org.gt/"><img class="img-fluid" alt="Acción Ciudadana" src="../assets/ac.png" /></a>
            </div>
            <div class="col-6">
              <a href="http://www.guatecambia.org.gt"><img class="img-fluid" alt="Guatecambia" src="../assets/guatecambia.png" /></a>
            </div>
          </b-row>
        </div>
        <div class="col-4"></div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  background-color:#333;
}
.footer-links {
  padding:35px 0 35px 0;
  color: #fff;
}
.footer-links a {
  color: #fff;
  margin: 0 25px 0 25px;
}
.footer-links a:hover {
  color:#EF2466;
  text-decoration:none;
}
.footer-logos {
  padding: 50px 0 50px 0;
}
</style>
