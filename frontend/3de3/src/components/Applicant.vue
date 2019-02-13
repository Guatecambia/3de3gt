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
    <b-container id="filters">
      <b-row>
        <div class="col-4">
          <div class="filter-title">Buscar por cargo</div>
          <select class="custom-select" id="select-position">
            <option selected>Todos</option>
            <option value="presidente">Presidente</option>
            <option value="vicepresidente">Vicepresidente</option>
          </select>
        </div>
        <div class="col-4">
          <div class="filter-title">Buscar por partido</div>
          <select class="custom-select" id="select-party">
            <option selected>Todos</option>
            <option value="presidente">Presidente</option>
            <option value="vicepresidente">Vicepresidente</option>
          </select>
        </div>
        <div class="col-4">
          <div class="filter-title">Buscar por género</div>
          <select class="custom-select" id="select-gender">
            <option selected>Todos</option>
            <option value="presidente">Presidente</option>
            <option value="vicepresidente">Vicepresidente</option>
          </select>
        </div>
      </b-row>
    </b-container>
    <b-container id="with-3de3">
      <b-row>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
        <div class="col-3 aspirant-box">
          <div class="party"> 
            <img class="party-icon" src="https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg" />
          </div>
          <div class="aspirant-pic">
            <img class="img-fluid" src="http://3de3.mx/assets/photo-eb27110938cffff97427c79b76cdbe4f1e0b8583db5104f15b84c794fc67ed0c.jpg" />
          </div>
          <div class="aspirant-name">
            Nombre y Apellido
          </div>
          <div class="aspirant-position">
            Puesto
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </a>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <a href="#">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </a>
            </div>
          </b-row>
        </div>
      </b-row>
    </b-container>
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
#filters {
  margin-top:45px;
}
.filter-title {
  background:#333;
  color:#fff;
  padding: 30px 0;
  border-radius: 5px 5px 0px 0px;
}
.custom-select {
  color:#fff;
  border: none;
  border-radius: 0px 0px 5px 5px;
}
#select-position {
  background-color: #EF2466;
}
#select-party {
  background-color: #0096DB;
}
#select-gender {
  background-color: #60bd55;
}
.custom-select::after {
    display: none;
}
#with-3de3 {
  margin-top:50px;
}
.aspirant-box {
  margin: 15px 0 25px 0;
}
.party-icon {
  width:60px;
  position:absolute;
  border: 5px solid #fff;
  border-radius: 50% !important;
  top:5px;
  right:25px;
}
.aspirant-pic img {
  border: 5px solid #000;
  border-radius: 50% !important;
}
.aspirant-name {
  font-weight:bolder;
  font-size:1.2em;
}
.aspirant-position {
  font.size: 0.9em;
}
</style>
