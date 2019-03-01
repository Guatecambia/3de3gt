<template>
  <div class="home">
    <Header />
    <b-container class="about">
      <b-row>
        <div class="col-3"></div>
        <div class="col-9">
          <h1>Ac<span class="blue-font">e</span>rca d<span class="pink-font">e</span></h1>
        </div>
      </b-row>
      <b-row>
        <div class="col-3"></div>
        <div class="col-9">
          <p>La iniciativa es impulsada en el marco del consorcio de organizaciones de sociedad civil, denominado Mirador Electoral, que desde el 2003 ha contribuído para velar por la legalidad, legitimidad, participación, representación e inclusión de la ciudadanía en general, en los procesos electorales en el país.</p>
          <p>3de3 busca que los candidatos y candidatas a puestos de elección popular en las Elecciones Generales 2019, de manera voluntaria hagan públicas sus tres declaraciones: Declaración Patrimonial, Declaración de Intereses y Declaración Fiscal.</p>
        </div>
      </b-row>
    </b-container>
    <Footer />
  </div>
</template>
<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
export default {
  name: 'about',
  components: {
    Header,
    Footer
  }
}
</script>
<style scoped>
p {
  text-align: justify;
}
h1 {
  text-align:left;
}
</style>
