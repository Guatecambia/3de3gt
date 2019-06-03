<template>
  <div class="section footer">
    <b-container>
      <b-row class="footer-links">
        <div col="col-12">
          <ul class="nav nav-fill">
            <li class="nav-item">
              <router-link to="/privacidad">Privacidad</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/faq">Preguntas Frecuentes</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/acerca-de">Acerca de</router-link>
            </li>
          </ul>
        </div>
      </b-row>
      <b-row class="footer-logos">
        <div class="d-none d-sm-block col-sm-2 col-lg-3"></div>
        <div class="col-sm-8 col-lg-6">
          <!--b-row>
            <div class="col-6">
              <a href="http://accionciudadana.org.gt/" target="_blank"><img class="img-fluid" alt="Acción Ciudadana" src="../assets/ac.png" /></a>
            </div>
            <div class="col-6">
              <a href="http://www.guatecambia.org.gt" target="_blank"><img class="img-fluid" alt="Guatecambia" src="../assets/guatecambia.png" /></a>
            </div>
          </b-row-->
        </div>
        <div class="d-none d-sm-block col-sm-2 col-lg-3"></div>
      </b-row>
    </b-container>
    <div class="promotedContent">
      <p class="promotedP"><img src="../assets/mochila.png"/>¡Conoce más herramientas de tecnología cívica para estas elecciones en <a target="_blank" href="http://mochilaelectoral.gt">mochilaelectoral.gt</a>!</p>
    </div>
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
@font-face {
  font-family: Apercu;
  src: url('../assets/apercu/apercu_regular.otf');
}
@font-face {
  font-family: Apercu;
  font-weight: bold;
  src: url('../assets/apercu/apercu_bold.otf');
}
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
.separator {
  display: inline-block !important;
}
.promotedContent {
  position:fixed;
  bottom:0;
  z-index:1200;
  width:100%;
  background: #444471;
}

.promotedP{
  text-align:center;
  color: #FFF;
  margin: 10px;
  font-family: 'Apercu', 'Heebo';
}

.promotedP a, .promotedP a:hover, .promotedP a:visited{
  color: #27B1AA;
  font-weight:bold;
}

.promotedP img {
  height: 50px;
}
</style>
