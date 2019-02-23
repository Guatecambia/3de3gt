<template>
  <div class="section ask3de3" id="exige">
    <b-container-fluid>
      <div class="row title">
        <div class="col-4">
          <hr class="line col-12">
        </div>
        <div class="col-4">
          <h2><span class="pink-font">E</span>xig<span class="blue-font">e</span> #3de3</h2>
        </div>
        <div class="col-4">
          <hr class="line col-12">
        </div>
      </div><!--title-->
    </b-container-fluid>
    <b-container>
      <b-row class="title">
        <div class="col-4">Nombre</div>
        <div class="col-4">Partido</div>
        <div class="col-3">Cargo</div>
        <div class="col-1">Escribele en</div>
      </b-row>
      <b-row v-for="(applicant, index) in aspirant" class="ask">
        <div class="col-4">{{ applicant.name }} {{ applicant.lastname }}</div>
        <div class="col-4">{{ applicant.party }}</div>
        <div class="col-3">{{ applicant.aspiredPosition }}</div>
        <div class="col-1">
          <a :href="'https://twitter.com/intent/tweet?text=Esto%20es%20una%20prueba%20%40'+applicant.twitter+'%20fin%20de%20prueba'" data-show-count="false"><img class="sn-btn" src="../assets/twitter-logo.png"/></a>
          <b-button class="ask-icon" v-b-modal="'applicant'+index">
            <img class="sn-btn" alt="Declaración de Intereses" src="../assets/fb-logo.png"/>
          </b-button>
          <b-modal ok-title="Aceptar" ok-only :id="'applicant'+index" size="lg" title="Instrucciones para compartir en Facebook">
            <div class="declarant-data">
              <span class="modal-text">Presiona el siguiente botón para abrir el dialogo de compartir en Facebook</span><br/>
              <b-button class="btn btn-fb shareFb" v-on:click="shareFb()">Compartir en Facebook</b-button><br/>
              <span class="modal-text">Copia el siguiente texto y pegalo en facebook</span><br/>
              <span class="modal-text">{{ message.fbCopy }}</span><b-button v-clipboard:copy="message.fbCopy" v-clipboard:error="copyError" size="sm" variant="outline-light">Copiar</b-button><br/>
              <span class="modal-text">Copia y pega el siguiente usuario, en la lista desplegable selecciona al candidato</span><br/>
              <span class="modal-text">@{{ applicant.twitter }}</span><b-button v-clipboard:copy="' @'+applicant.twitter" v-clipboard:error="copyError" size="sm" variant="outline-light">Copiar</b-button><br/>
              <span class="modal-text">Copia y pega el siguiente usuario, en la lista desplegable selecciona al partido del candidato</span><br/>
              <span class="modal-text">@{{ applicant.party }}</span><b-button v-clipboard:copy="' @'+applicant.party" v-clipboard:error="copyError" size="sm" variant="outline-light">Copiar</b-button><br/>
              <span class="modal-text">Presiona el botón "Publicar en Facebook"</span><br/>              
            </div>
          </b-modal>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Ask3de3',
  data: function() {
    return {
      message: {
        copySucceeded: null,
        fbCopy: "Publica tu #3de3 para que todos podamos conocer tus intereses",
        cpError: "La versión de tu navegador no permite usar el botón de copiar, selecciona el texto y copialo manualmente"
      },
      aspirant: [
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
      ]
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
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title div {
  font-weight:bolder;
  font-size: 1.1em;
  text-align:left;
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
</style>
