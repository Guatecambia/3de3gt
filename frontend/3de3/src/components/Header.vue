<template>
  <!--header class="page-navbar sticky-top container"-->
  <header class="page-navbar container">
    <div class="row page-menu">
        <div class="col-4 col-sm-2">
            <router-link id="navbar-brand" to="/"><img class="img-fluid" src="../assets/3de3.png" alt="3de3 Guatemala" /></router-link>
        </div>
        <div class="col-8 col-sm-10">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div class="float-right rs-holder">
                  <a href="https://www.instagram.com/3de3guate/" target="_blank"><img class="rs-ico" src="../assets/ig.jpg"/></a>
                  <a href="https://www.facebook.com/3de3guatemala/" target="_blank"><img class="rs-ico" src="../assets/tw.jpg"/></a>
                  <a href="https://twitter.com/3de3guate" target="_blank"><img class="rs-ico" src="../assets/fb.jpg"/></a>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-12 page-menu-block">
                <b-navbar type="light" toggleable="lg" class="navbar-nav">
                  <b-navbar-toggle target="nav_collapse" class="ml-auto"/>
                  <b-collapse is-nav  id="nav_collapse">
                    <b-navbar-nav class="navbar navbar-nav nav-fill menu bd-navbar-nav flex-row smooth-scroll justify-content-center">
                      <b-nav-item to="/#aspirantes">Candidatos</b-nav-item>
                      <b-nav-item to="/#exige">Exige 3de3</b-nav-item>
                      <b-nav-item v-bind:class="{ active: $route.name === 'estadisticas' }" to="/estadisticas">Estadísticas</b-nav-item>
                      <b-nav-item v-bind:class="{ active: $route.name === 'addyours' }"to="/presenta">Publica tu 3de3</b-nav-item>
                    </b-navbar-nav>
                  </b-collapse>
                </b-navbar>
              </div>
            </div>
          </div>
        </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
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
.navbar-nav {
  padding: 0;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
li.nav-item {
  padding: 5px 25px;
  background: #EF2466;
  color: #FFF;
  border-left: 1px solid #EF2466;
  border-top: 1px solid #EF2466;
  border-bottom: 1px solid #EF2466;
}

li.nav-item a {
  color: #FFF;
}

li.nav-item a:hover {
  color: #0096DB;
}
li.nav-item:hover, li.nav-item.active {
  background: white;
  border: 1px solid #EF2466;
  color: #EF2466;
}
li.nav-item:hover a, li.nav-item.active a.active, li.nav-item:hover a.active{
  color: #EF2466 !important;
}
li.nav-item a.active {
  color: white !important;
}
.page-navbar{
  padding-top:10px;
}
.nav-item {
  border-right:1px solid #fff;
}
a.nav-link {
  color: #fff !important;
}
.navbar-toggler {
  background-color:#EF2466;
}
.rs-ico {
  margin: 3px 5px;
  max-width: 35px;
}
.rs-holder {
  margin-bottom: 25px;
}
@media (min-width: 992px) {
  #nav_collapse {
    display: flow-root !important;
  }
}
@media (max-width: 991px) {
  ul.navbar {
    flex-direction: column !important;
    background-color: #EF2466;
  }
  ul.navbar li {
    border-right: none;
    border-bottom: 1px solid #fff;
  }
  #nav_collapse {
    margin-left:auto !important;
  }
}
</style>
