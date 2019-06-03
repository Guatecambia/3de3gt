<template>
  <div class="section ask3de3" id="exige">
    <div class="container">
      <div class="row title">
        <div class="col-1 col-sm-2 col-md-4 line-container">
            <hr class="line col-8 col-lg-12" />
        </div>
        <div class="col-10 col-sm-8 col-md-4">
          <h2 class="justify-content-center"><span class="pink-font">E</span>xig<span class="blue-font">e</span> #3de3</h2>
        </div>
        <div class="col-1 col-sm-2 col-md-4 line-container">
            <hr class="line col-8 col-lg-12" />
        </div>
      </div><!--title-->
    </div>
    <b-container>
      <b-row class="title">
        <div class="col-4">Nombre</div>
        <div class="col-3">Partido</div>
        <div class="col-3">Cargo</div>
        <div class="col-2 text-center"></div>
      </b-row>
      <b-row class="filters">
        <div class="col-4"><b-form-input 
                              v-model="filters.name"
                              type="search"
                              placeholder="Búsqueda por nombre"
                              v-on:keyup.space.native="applyNameFilter"
                              @change="applyNameFilter"
                            />
        </div>
        <div class="col-3"><b-form-select
                              v-model="filters.party" 
                              :options="parties"
                              @change="applyPartyFilter"
                            />
        </div>
        <div class="col-3"><b-form-select
                              v-model="filters.position" 
                              :options="positions"
                              @change="applyPositionFilter"
                            />
        </div>
        <div class="col-2"></div>
      </b-row>
      <b-row v-for="(applicant, index) in aspirant" class="ask">
        <div class="col-4">{{ applicant.name }} {{ applicant.lastname }}</div>
        <div class="col-3">{{ applicant.party_name }}</div>
        <div class="col-3">{{ applicant.aspiredPosition }}</div>
        <div class="col-2 text-center">
          <a :href="'https://twitter.com/intent/tweet?text='+applicant.name+'%20'+applicant.lastname+'%20queremos%20pol%C3%ADticos%20cabales%20y%20muestras%20concretas%20de%20tu%20compromiso%20con%20la%20honestidad%20y%20la%20transparencia%2C%20%23exijo3de3%20%233de3guate%20%40'+applicant.twitter" data-show-count="false"><img class="sn-btn" src="../assets/twitter-logo.png"/></a>
          <b-button class="ask-icon" v-b-modal="'applicant'+index">
            <img class="sn-btn" alt="Declaración de Intereses" src="../assets/fb-logo.png"/>
          </b-button>
          <b-modal ok-title="Aceptar" ok-only :id="'applicant'+index" size="lg" title="Instrucciones para compartir en Facebook">
              <div class="declarant-data">
                <span class="modal-text">{{ message.fbCopy }} {{ applicant.name }} {{ applicant.lastname }} @{{ applicant.facebook }}</span><b-button v-clipboard:copy="message.fbCopy + applicant.name + ' ' + applicant.lastname + ' '+'@' + applicant.facebook" v-clipboard:error="copyError" size="sm" variant="outline-light">Copiar</b-button><br/>
                <b-button class="btn btn-fb shareFb" @click="shareFb()">Escribe tu publicación</b-button><br/>
              </div>
          </b-modal>
        </div>
      </b-row>
      <template v-if="aspirant.length == 0">
        <h3 class="text-center" style="margin-top: 45px;">No se han encontrado candidatos/as para esta selección</h3>
      </template>
      <template v-if="aspirant.length > 0">
        <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage" size="sm" align="center" @change="getAspirants" />
      </template>
    </b-container>
  </div>
</template>

<script>
import {HTTP} from '../../http-constants'
export default {
  name: 'Ask3de3',
  data: function() {
    return {
      message: {
        copySucceeded: null,
        fbCopy: "Queremos políticos cabales, tenemos derecho a conocer a quién le damos nuestro voto, presenta tu #3de3guate #exijo3de3 ",
        cpError: "La versión de tu navegador no permite usar el botón de copiar, selecciona el texto y copialo manualmente"
      },
      aspirant: 
        [
        ],
      filters: {
        party: null,
        position: null,
        name: null,
      },
      parties: [
      ],
      positions: [
        { value: null, text: "Seleccione cargo"},
        { value: "P", text: "Presidente" },
        { value: "V", text: "Vicepresidente" },
        { value: "LEG", text: "Diputado" },
        { value: "M", text: "Alcalde" },
      ],
      rows: 0,
      perPage: 25,
      currentPage: 0,
    }
  },
  props: {
    msg: String
  },
  methods: {
    shareFb: function(event) {
      FB.ui({
        method: 'share',
        href: 'http://www.3de3.gt'
      }, function(response){});
    },
    copyError: function(event) {
      alert(this.message.cpError);
    },
    getAspirants: function(page) {
      if (page)
        this.currentPage = page;
      else
        this.currentPage = 1;
      var filtersParam = '';
      for (var filterDetail in this.filters) {
        if (this.filters[filterDetail])
          filtersParam += '&'+filterDetail+'='+this.filters[filterDetail];
      }
      HTTP.get('/candidatos/exige?limit='+this.perPage+'&offset='+(this.perPage*(this.currentPage-1))+filtersParam)
        .then(response => {
          this.aspirant = response.data['results']
          this.rows = response.data['count']
        })
        .catch(e => {
          this.errors = e
        })
    },
    applyPartyFilter: function(selected) {
      this.filters.party = selected;
      this.getAspirants(1);
    },
    applyPositionFilter: function(selected) {
      this.filters.position = selected;
      this.getAspirants(1);
    },
    applyNameFilter: function(key) {
      this.getAspirants(1);
    },
    getFilters: function() {
      HTTP.get('/generico/partidosycomites?limit=1000&offset=0')
        .then(response => {
          this.parties = response.data['results'];
          this.parties.unshift({value: null, text: "Seleccione partido o comité civico"});
        })
        .catch(e => {
          this.errors = e
        })
    }
  },
  beforeMount() {
    this.getAspirants()
    this.getFilters()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title div {
  font-weight:bolder;
  font-size: 1.1em;
  text-align:left;
  margin-top:50px;
}
.ask div {
  text-align:left;
}
.ask {
  padding:15px 0 15px 0;
}
.sn-btn {
  width:25px;
  margin: 0 2px 0 2px;
}
.ask-icon {
  background-color:transparent;
  border:none;
  padding:0;
}
.ask-icon:focus,.ask-icon:active {
   outline: none !important;
   box-shadow: none;
}
.btn-fb {
  background-color: #3b5998;
}
.btn-sm {
  font-size: 0.7em;
  padding: 2px 1px;
  margin-left:10px;
}
.pagination {
  margin-top:50px;
  margin-bottom: 70px;
}
</style>
<style>
.page-link {
  border: none !important;
  color: #333;
}
.page-item.active .page-link {
  background-color: #333;
  color: #fff;
}
.page-item:hover .page-link, .page-item:focus .page-link{
  background: #333;
  color: #fff;
}
.pagination-sm .page-link {
  padding: 0.25rem 0.75rem;
}
.page-link:focus {
  box-shadow:none;
}
ul.pagination li:first-child a span, ul.pagination li:first-child span, ul.pagination li:last-child a span, ul.pagination li:last-child span{
  border-radius: 50%;
  border: 1px solid;
  padding: 0 6px;
  margin-top: 5px;
}
.line-container {
  overflow: hidden;
}
</style>
