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
          {{ applicant.twitter }} fb
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
      aspirant: [
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "@prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "@prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
        {
          name: "Nombre 1",
          lastname: "Apellido 1",
          party: "TODOS",
          twitter: "@prueba",
          aspiredPosition: "EX",
          executivePosition: "P",
        },
      ]
    }
  },
  props: {
    msg: String
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
</style>
