<template>
  <div class="home">
    <Header />
    <b-container>
      <b-row>
        <div class="col-4"></div>
        <div class="col-8">
          <h1>Información d<span class="blue-font">e</span> Candidatos</h1>
        </div>
      </b-row>
      <b-row class="text">
        <div class="col-2"></div>
        <div class="col-10">
          <p>3de3 es una iniciativa ciudadana que promueve la honestidad de los candidatos y candidatas a cargos de elección popular, para reconstruir la confianza en los políticos, a través de la publicación voluntaria  de su declaración patrimonial, declaración de interés y la declaración fiscal (solvencia), como muestra de su compromiso con la transparencia y rendición de cuentas.</p>
        </div>
      </b-row>
      <b-row class="icons">
        <div class="col-4"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Declaración fiscal (solvencia)" src="../assets/sf.png" v-b-tooltip.hover title="Es el documento por medio del cual la Superintendencia de Administración Tributaria (SAT) hace constar que el candidato o candidata, se encuentran al día en el cumplimiento de sus deberes tributarios formales.">
          <span>Declaración fiscal (solvencia)</span>
        </div>
        <div class="col-1"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Declaración de interés" src="../assets/di.png" v-b-tooltip.hover title="Es la información sobre las relaciones y vínculos económicos, profesionales, familiares y sociales de los candidatos para prevenir que sus intereses influyan indebidamente o afecten las decisiones del funcionario durante su gestión.">
          <span>Declaración de interés</span>
        </div>
        <div class="col-1"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Declaración patrimonial" src="../assets/dp.png" v-b-tooltip.hover title="Es la declaración de los bienes y obligaciones que los candidatos deben presentar para dar cuenta de su patrimonio y el comportamiento del mismo durante su gestión.">
          <span>Declaración patrimonial</span>
        </div>
        <div class="col-1"></div>
        <div class="col-2"></div>
      </b-row>
    </b-container>
    <Applicant />
    <Ask3de3 />
    <Footer />
  </div>
</template>

<script>
import Applicant from '@/components/Applicant.vue'
import Ask3de3 from '@/components/Ask3de3.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
export default {
  name: 'home',
  components: {
    Applicant,
    Ask3de3,
    Header,
    Footer
  },
  async mounted() {
    let twitterScript = document.createElement('script')
    twitterScript.setAttribute('src', 'https://platform.twitter.com/widgets.js')
    twitterScript.setAtt
    document.head.appendChild(twitterScript)
  },
}
</script>

<style scoped>
.text {
  text-align: justify;
}
.text p {
  margin-top:35px;
}
.icons {
  margin-top:45px;
  margin-bottom:75px;
}
.tooltip-inner {
  color: #fff;
  background-color: #EF2466;
  border-radius: .25rem;
}

/*tooltip arrows*/
.tooltip.bs-tooltip-top .arrow::before {
  border-top-color: #EF2466 !important;
}
.tooltip.bs-tooltip-right .arrow::before {
  border-right-color: #EF2466 !important;
}
.tooltip.bs-tooltip-bottom .arrow::before {
  border-bottom-color: #EF2466 !important;
}
.tooltip.bs-tooltip-left .arrow::before {
  border-left-color: #EF2466 !important;
}
</style>
