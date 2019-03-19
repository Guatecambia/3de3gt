<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Partidos<b-button class="addNew" to="/3de3-admin/partido" type="button">+</b-button></h2></div>
      </b-row>
      <b-row class="title">
        <div class="col-2 justify-content-center">Id</div>
        <div class="col-10 justify-content-center">Nombre</div>
      </b-row>
      <b-row v-for="(district, index) in districts">
        <div class="col-2">
          <div class="district-number">
            {{ party.id }}
          </div>
        </div>
        <div class="col-10">
          <div class="district-item">
            <router-link :to="'/3de3-admin/partido/'+party.id" class="nav-link">{{ party.name }}</router-link></li>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
export default {
  name: 'partidos',
  components: {
    AdminHeader,
  },
  methods: {
    getDistricts: function() {
      HTTP.get('/3de3-admin/partidos/')
        .then(response => {
          this.districts = response.data
        })
        .catch(e => {
          this.errors = e
        })
    }
  },
  mounted() {
    this.getDistricts()
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
