<template>
  <div class="home">
    <Header />
    <b-container class="privacy">
      <b-row>
        <div class="col-12">
          <h1><span class="pink-font">E</span>stadisticas</h1>
        </div>
      </b-row>
      <b-row>
        <div class="col-12">
          <p class="bold">Prónto podras ver las estadísticas</p>
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
p, li {
  text-align: justify;
}
h1 {
  text-align:left;
}
.bold {
  font-weight: bold;
}
</style>
