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
      <b-row v-for="(party, index) in parties">
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
      <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage" size="sm" align="center" @change="getParties" />
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
import {HTTP} from '../../http-constants'
export default {
  name: 'partidos',
  components: {
    AdminHeader,
  },
  
  data: function() {
    return {
      parties: [
      ],
      rows: 0,
      perPage: 24,
      currentPage: 0
    }
  },
  methods: {
    getParties: function(page) {
      if (page)
        this.currentPage = page;
      else
        this.currentPage = 1;
      HTTP.get('/3de3-admin/partidos/'+'?limit='+this.perPage+'&offset='+(this.perPage*(this.currentPage-1)))
        .then(response => {
          this.parties = response.data['results']
          this.rows = response.data['count']
        })
        .catch(e => {
          this.errors = e
        })
    }
  },
  mounted() {
    this.getParties()
  }
}
</script>
<style scoped>
h2 {
  margin-top:45px;
}
.title {
  margin-top:45px;
}
.district-number {
  padding: 30px 0;
}
.district-item {
  padding: 25px 0;
  text-align: justify;
}
.addNew {
  margin-left:25px;
  border-radius:50px;
  padding: 0 10px;
  border:none;
  background-color: #0096DB;
  color:white;
}
</style>
