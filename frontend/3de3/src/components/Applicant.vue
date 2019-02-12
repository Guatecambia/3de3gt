<template>
  <div class="section aspirant">
    <b-container-fluid>
      <div class="row title">
        <div class="col-4">
          <hr class="line col-12">
        </div>
        <div class="col-4">
          <h2>Aspirant<span class="blue-font">e</span>s</h2>
        </div>
        <div class="col-4">
          <hr class="line col-12">
        </div>
      </div><!--title-->
    </b-container-fluid>
    <b-container>
      <div class="row statistics">
        <div class="col-12 statInfo">
          <h3>Aspirantes que ya publicaron su 3de3</h3>
          <div class="row">
            <div class="col-3">
              <div class="big-num blue-font">10</div>
              <div class="desc">Aspirantes a la Presidencia</div>
            </div>
            <div class="col-3">
              <div class="big-num pink-font">10</div>
              <div class="desc">Aspirantes a Alcaldías por Comités Cívicos</div>
            </div>
            <div class="col-3">
              <div class="big-num pink-font">10</div>
              <div class="desc">Aspirantes a Alcaldías por Partidos Políticos</div>
            </div>
            <div class="col-3">
              <div class="big-num green-font">10</div>
              <div class="desc">Aspirantes al Congreso</div>
            </div>
          </div>
        </div>
      </div>
    </b-container>
    <div class="applicant-menu">
      <b-container>
        <b-row>
          <div class="col-12">
            <ul class="nav nav-fill">
              <li class="nav-item">
                <a class="nav-link" href="#">Ejecutivo</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Legislativo</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Munis</a>
              </li>
            </ul>
          </div>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Applicant',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.statInfo {
  background: #333;
}
.statInfo h3 {
  color: #fff;
  text-transform:uppercase;
  font-weight: bolder;
  padding:35px;
}
.big-num {
  font-size: 4em;
  font-weight: bolder;
}
.statInfo .desc{
  color:#fff;
}
.applicant-menu {
  background:#333;
  margin-top:50px;
}
li.nav-item {
  background: #333;
  color: #FFF;
  border-right:none;
}
li.nav-item:hover {
  background: #fff;
  color: #EF2466;
}
li.nav-item:hover a{
  color: #EF2466;
}
</style>
