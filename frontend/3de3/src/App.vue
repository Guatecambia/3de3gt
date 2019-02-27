<template>
  <div id="app">
    <!--header class="page-navbar sticky-top container"-->
    <header class="page-navbar container">
      <div class="row page-menu">
          <div class="col-2">
              <router-link id="navbar-brand" to="/"><img class="img-fluid" src="./assets/3de3.png" alt="3de3 Guatemala" /></router-link>
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
    <router-view/>
    <Footer />    
  </div>
</template>
<script>
import Footer from '@/components/Footer.vue'
export default {
  components: {
    Footer
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Heebo:400,900');

html, body {
  font-family: 'Heebo', sans-serif;
}

body {
  font-family: 'Heebo', sans-serif;
}

#app {
  font-family: 'Heebo', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
}

li.nav-item a {
  color: #FFF;
}

li.nav-item a:hover {
  color: #0096DB;
}

.page-navbar{
  padding-top:10px;
}

.section {
  margin-top: 35px;
}

hr.line {
  border-top: 1px solid;
  border-color: #000;
}

h2,h1 {
  text-align:center;
  text-transform:uppercase;
  font-weight: bolder;
}
.pink-font {
  color: #EF2466;
}
.blue-font{
  color: #0096DB;
}
.green-font {
  color: #60bd55;
}
.nav-item {
  border-right:1px solid #fff;
}
</style>
