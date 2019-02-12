<template>
  <div id="app">
    <!--header class="page-navbar sticky-top container"-->
    <header class="page-navbar container">
      <div class="row page-menu">
          <div class="col-2">
              <a id="navbar-brand" href="#inicio"><img class="img-fluid" src="./assets/3de3.jpg" alt="3de3 Guatemala" /></a>
          </div>
          <div class="col-10 page-menu-block">
            <nav>
              <ul class="navbar-nav menu bd-navbar-nav flex-row smooth-scroll justify-content-center">
                <li class="nav-item"><router-link to="#aspirantes" class="nav-link">Aspirantes</router-link></li>
                <li class="nav-item"><span class="nav-link">|</span></li>
                <li class="nav-item"><router-link to="#nosotros" class="nav-link">Exige 3de3</router-link></li>
                <li class="nav-item"><span class="nav-link">|</span></li>
                <li class="nav-item"><router-link to="#transparencia" class="nav-link">Estadisitcas</router-link></li>
                <li class="nav-item"><span class="nav-link">|</span></li>
                <li class="nav-item"><router-link to="#contacto" class="nav-link">Publica tu 3de3</router-link></li>
              </ul>
            </nav>
          </div>
      </div>
    </header>
    
    <!--div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div-->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
</style>
