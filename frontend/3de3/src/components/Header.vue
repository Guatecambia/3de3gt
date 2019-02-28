<template>
  <!--header class="page-navbar sticky-top container"-->
  <header class="page-navbar container">
    <div class="row page-menu">
        <div class="col-2">
            <router-link id="navbar-brand" to="/"><img class="img-fluid" src="../assets/3de3.png" alt="3de3 Guatemala" /></router-link>
        </div>
        <div class="col-10 page-menu-block">
          <nav>
            <ul class="navbar-nav nav-fill menu bd-navbar-nav flex-row smooth-scroll justify-content-center">
              <li class="nav-item"><router-link to="/#aspirantes" class="nav-link">Aspirantes</router-link></li>
              <li class="nav-item"><router-link to="/#exige" class="nav-link">Exige 3de3</router-link></li>
              <li class="nav-item"><router-link to="#estadisticas" class="nav-link">Estadisitcas</router-link></li>
              <li class="nav-item"><router-link to="/presenta" class="nav-link">Publica tu 3de3</router-link></li>
            </ul>
          </nav>
        </div>
    </div>
  </header>
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
