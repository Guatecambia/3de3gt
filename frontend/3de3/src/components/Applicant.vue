<template>
  <div class="section aspirant" id="aspirantes" ref="aspirantes">
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
              <div class="big-num blue-font">{{ statistics.president }}</div>
              <div class="desc">Aspirantes a la Presidencia</div>
            </div>
            <div class="col-3">
              <div class="big-num pink-font">{{ statistics.civicComitee }}</div>
              <div class="desc">Aspirantes a Alcaldías por Comités Cívicos</div>
            </div>
            <div class="col-3">
              <div class="big-num pink-font">{{ statistics.muniByParty }}</div>
              <div class="desc">Aspirantes a Alcaldías por Partidos Políticos</div>
            </div>
            <div class="col-3">
              <div class="big-num green-font">{{ statistics.congress }}</div>
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
        <div v-for="(applicant, index) in aspirant" class="col-3 aspirant-box">
          <div class="picture-frame">
            <div class="pic-buttons">
              <a :href="'https://twitter.com/intent/tweet?text=Esto%20es%20una%20prueba%20%40'+applicant.twitter+'%20fin%20de%20prueba'" data-show-count="false"><img class="sn-btn" src="../assets/twitter-logo-tr.png"/></a>
              <a :href="'https://twitter.com/intent/tweet?text=Esto%20es%20una%20prueba%20%40'+applicant.twitter+'%20fin%20de%20prueba'" data-show-count="false"><img class="sn-btn" src="../assets/fb-logo-tr.png"/></a>
            </div>
            <div class="aspirant-pic">
              <img class="img-fluid" :src="applicant.aspirantPic" />
            </div>
          </div>
          <div class="party"> 
            <img class="party-icon" :src="applicant.partyPic" />
          </div>
          <div class="aspirant-name">
            {{ applicant.name }} {{ applicant.lastname }}
          </div>
          <div class="aspirant-position">
            {{ applicant.aspiredPosition }}
          </div>
          <b-row class="aspirant-docs">
            <div class="col-3">
              <b-button class="declaration-icon" v-b-modal="'fiscal'+index">
                <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg"/>
              </b-button>
              <b-modal :id="'fiscal'+ index" size="xl" title="Solvencia Fiscal">
                <h2>Modal {{ index }}</h2>
              </b-modal>
            </div>
            <div class="col-1"></div>
            <div class="col-3">              
              <b-button class="declaration-icon" v-b-modal="'interest'+index">
                <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg"/>
              </b-button>
              <b-modal :id="'interest'+ index" size="xl" title="Declaración de Intereses">
                <h6>Datos del declarante</h6>
                <div class="declarant-data">
                  <span class="modal-key">Nombres y apellidos</span>: <span class="modal-value">{{ aspirantData.name }} {{ aspirantData.lastname }}</span><br/>
                  <span class="modal-key">Género</span>: <span class="modal-value">{{ aspirantData.gender }}</span><br/>
                  <span class="modal-key">Grupo Étnico</span>: <span class="modal-value">{{ aspirantData.ethnicity }}</span><br/>
                  <span class="modal-key">Partído</span>: <span class="modal-value">{{ aspirantData.party }}</span><br/>
                </div>
                <h6>Declaración</h6>
                <div v-for="(dataItem, index) in interestDeclarationData" class="declarant-form">
                  <span class="modal-key">{{ dataItem.fieldName }}</span>: <span class="modal-value">{{ dataItem.fieldValue }}</span>
                </div>
              </b-modal>
            </div>
            <div class="col-1"></div>
            <div class="col-3">
              <b-button class="declaration-icon" v-b-modal="'patrimonial'+index">
                <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg"/>
              </b-button>
              <b-modal :id="'patrimonial'+ index" size="xl" title="Declaración Patrimonial">
                <h2>Modal {{ index }}</h2>
              </b-modal>
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
  data: function() {
    return {
      statistics: {
        president: "10",
        civicComitee: "20",
        muniByParty: "90",
        congress: "458"
      },
      aspirant: [
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 2",
          lastname: "Apellido 2",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
        {
          name: "Nombre 3",
          lastname: "Apellido 3",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
        },
      ],
      aspirantData: {
          name: "Declarante para",
          lastname: "popup information",
          gender: "M",
          ethnicity: "I",
          twitter: "@prueba",
          maritalStatus: "S",
          party: "TODOS",
          aspiredPosition: "EX",
          executivePosition: "P",
          partyPic: "https://3de3.mx/assets/partidos/morena-alianza-796e92d630b589fb98c5147352237b14c9ae51b8141f0c58dc4329b015182844.svg",
          aspirantPic: "http://avatars.io/twitter/lopezobrador_"
      },
      interestDeclarationData: [
        {
          fieldName: "field 1",
          fieldValue: "value"
        },
        {
          fieldName: "field 2",
          fieldValue: "value"
        },
        {
          fieldName: "field 3",
          fieldValue: "value"
        },
        {
          fieldName: "field 4",
          fieldValue: "value"
        },
        {
          fieldName: "field 5",
          fieldValue: "value"
        },
        {
          fieldName: "field 6",
          fieldValue: "value"
        },
        {
          fieldName: "field 7",
          fieldValue: "value"
        },
        {
          fieldName: "field 8",
          fieldValue: "value"
        },
        {
          fieldName: "field 9",
          fieldValue: "value"
        },
        {
          fieldName: "field 10",
          fieldValue: "Nunc in lorem luctus metus auctor tempor at id arcu. Etiam eu turpis ac odio euismod convallis sit amet vitae nisl. Suspendisse sed rutrum augue, ut aliquam neque. Donec volutpat consequat metus, eu pharetra ex sagittis in. Donec auctor ipsum sit amet luctus mattis. Suspendisse eu neque quis nunc accumsan dictum. Praesent non tellus vitae nibh hendrerit iaculis. Nulla facilisi. Proin faucibus, felis id consequat convallis, lacus elit rutrum quam, et volutpat turpis arcu aliquam nunc. Vestibulum sagittis leo a ante sodales, eu consequat urna imperdiet. Morbi semper dictum ipsum, quis iaculis tortor varius ut. Nulla cursus, orci cursus ornare mollis, lorem elit efficitur leo, quis bibendum erat lacus id mi. Maecenas malesuada augue sit amet erat interdum, at viverra nulla rutrum. Suspendisse et hendrerit eros. Sed molestie consequat vulputate."
        },
        {
          fieldName: "field 11",
          fieldValue: "value"
        },
      ],
      legislative: {
      },
      muni: {
      }
    }
  },
  props: {
    msg: String
  },
  methods: {
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

.picture-frame {
  border: 5px solid #000;
  border-radius: 50% !important;
  overflow:hidden;
}
.picture-frame:hover {
  border: 5px solid #a32b52;
}
.aspirant-pic {
  z-index:9;
}
.aspirant-pic:hover, .pic-buttons:hover + .aspirant-pic {
  background-color: #EF2466;
  border-radius: 50%;
  position:relative;
}
.aspirant-pic:hover img, .pic-buttons:hover + .aspirant-pic img {
  opacity: 0.5;
}
.aspirant-name {
  font-weight:bolder;
  font-size:1.2em;
}
.aspirant-position {
  font.size: 0.9em;
}
.pic-buttons {
  position:absolute;
  left:50%;
  top:50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  opacity:0;
  z-index:10;
}
.picture-frame:hover .pic-buttons {
  opacity:100;
}
.sn-btn {
  width:35px;
  margin: 0 2px 0 2px;
}
.declaration-icon {
  background-color:transparent;
  border:none;
  padding:0;
}
.declaration-icon:focus,.declaration-icon:active {
   outline: none !important;
   box-shadow: none;
}
</style>
<style>
.modal-content {
  background-color: #333333 !important;
  border: 5px solid;
  border-color: #ee2466;
}
.modal-header, .modal-footer {
  border:none;
}
.modal-header .close {
  font-weight: lighter;
  border: 2px solid white;
  border-radius: 50%;
  padding: 0 5px;
  color: white;
  opacity: 1;
  margin: 2px 3px 0 0;
}
h5.modal-title {
  margin-top: 25px;
  margin-left: 25px;
  text-transform: uppercase;
  font-weight: bolder;
  color:white;
}
.modal-body {
  margin-left: 25px;
  text-align: left;
  color: white;
}
.modal-body h6 {
  color: #ee2466;
  text-transform: uppercase;
  font-weight: bolder;
  text-align:left;
  margin-top: 20px;
}
</style>
