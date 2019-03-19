<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Distritos<b-button class="addNew" to="/3de3-admin/distrito" type="button">+</b-button></h2></div>
      </b-row>
      <b-row class="title">
        <div class="col-2 justify-content-center">Id</div>
        <div class="col-10 justify-content-center">Nombre</div>
      </b-row>
      <b-row v-for="(district, index) in districts">
        <div class="col-2">
          <div class="district-number">
            {{ district.id }}
          </div>
        </div>
        <div class="col-10">
          <div class="district-item">
            <router-link :to="'/3de3-admin/distrito/'+district.id" class="nav-link">{{ district.name }}</router-link></li>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
import {HTTP} from '../../http-constants'
export default {
  name: 'distritos',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      districts: [
      ]
    }
  },
  methods: {
    getDistricts: function() {
      HTTP.get('/3de3-admin/distritos/')
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
