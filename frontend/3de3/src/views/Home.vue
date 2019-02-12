<template>
  <div class="home">
    <b-container>
      <b-row>
        <div class="col-2"></div>
        <div class="col-10">
          <img class="img-fluid" alt="3 de 3 Guatemala" src="../assets/title.jpg">
        </div>
      </b-row>
      <b-row class="text">
        <div class="col-2"></div>
        <div class="col-10">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat scelerisque laoreet. Nunc ut mattis magna. Sed gravida nisi lacinia bibendum aliquet. Fusce feugiat felis ut sem porta luctus. In et leo a dui pretium sollicitudin nec vitae nunc. Praesent interdum ipsum ac luctus egestas. Aenean nec neque vitae mauris maximus posuere. Quisque scelerisque quam eu mi ornare, ac semper tellus vestibulum. Proin dapibus vehicula dui. In ornare quam mauris, id tristique arcu semper a. Nunc eget lacus quis orci cursus rhoncus vitae at elit. Aliquam pharetra massa eu orci volutpat, quis iaculis tellus tempus. Integer eu neque massa. Suspendisse arcu libero, pharetra vel dolor nec, sollicitudin accumsan nisl. Ut risus ligula, iaculis sit amet leo quis, placerat interdum augue. Cras iaculis ante sed suscipit posuere.</p>
          <p>Nunc in lorem luctus metus auctor tempor at id arcu. Etiam eu turpis ac odio euismod convallis sit amet vitae nisl. Suspendisse sed rutrum augue, ut aliquam neque. Donec volutpat consequat metus, eu pharetra ex sagittis in. Donec auctor ipsum sit amet luctus mattis. Suspendisse eu neque quis nunc accumsan dictum. Praesent non tellus vitae nibh hendrerit iaculis. Nulla facilisi. Proin faucibus, felis id consequat convallis, lacus elit rutrum quam, et volutpat turpis arcu aliquam nunc. Vestibulum sagittis leo a ante sodales, eu consequat urna imperdiet. Morbi semper dictum ipsum, quis iaculis tortor varius ut. Nulla cursus, orci cursus ornare mollis, lorem elit efficitur leo, quis bibendum erat lacus id mi. Maecenas malesuada augue sit amet erat interdum, at viverra nulla rutrum. Suspendisse et hendrerit eros. Sed molestie consequat vulputate.</p>
        </div>
      </b-row>
      <b-row class="icons">
        <div class="col-3"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Solvencia Fiscal" src="../assets/sf.jpg" v-b-tooltip.hover title="La solvencia fiscal es ...">
          <span>Solvencia Fiscal</span>
        </div>
        <div class="col-1"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Declaración de Intereses" src="../assets/di.jpg" v-b-tooltip.hover title="La Declaración de intereses es ...">
          <span>Declaración de Intereses</span>
        </div>
        <div class="col-1"></div>
        <div class="col-1">
          <img class="img-fluid" alt="Declaración Patrimonial" src="../assets/dp.jpg" v-b-tooltip.hover title="La Declaración Patrimonial es ...">
          <span>Declaración Patrimonial</span>
        </div>
        <div class="col-1"></div>
        <div class="col-3"></div>
      </b-row>
    </b-container>
    <Applicant />
  </div>
</template>

<script>
import Applicant from '@/components/Applicant.vue'

export default {
  name: 'home',
  components: {
    Applicant
  }
}

</script>

<style>
.text {
  text-align: justify;
}
.text p {
  margin-top:35px;
}
.icons {
  margin-top:35px;
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
