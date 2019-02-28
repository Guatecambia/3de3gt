<template>
  <!--header class="page-navbar sticky-top container"-->
  <header class="page-navbar container">
    <div class="row page-menu">
        <div class="col-1">
            <router-link id="navbar-brand" to="/"><img class="img-fluid" src="../assets/3de3.png" alt="3de3 Guatemala" /></router-link>
        </div>
        <div class="col-11 page-menu-block">
          <nav>
            <ul class="navbar-nav nav-fill menu bd-navbar-nav flex-row smooth-scroll justify-content-center">
              <li class="nav-item"><router-link to="/3de3-admin/ingresos" class="nav-link">Ingresos</router-link></li>
              <li class="nav-item"><router-link to="/3de3-admin/candidatos" class="nav-link">Candidatos</router-link></li>
              <li class="nav-item"><router-link to="/3de3-admin/estadisticas" class="nav-link">Estadísticas</router-link></li>
              <b-nav-item-dropdown text="Catálogos" right>
                <b-dropdown-item to="/3de3-admin/partidos">Partidos y Comités</b-dropdown-item>
                <b-dropdown-item to="/3de3-admin/distritos">Distritos</b-dropdown-item>
                <b-dropdown-item to="/3de3-admin/municipios">Municipios</b-dropdown-item>
              </b-nav-item-dropdown>
            </ul>
          </nav>
        </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AdminHeader',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.dropdown-item {
  color: #0096DB;
}
.dropdown-item.active {
  color: white;
}
</style>
