<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Ingresos</h2></div>
      </b-row>
      <b-row>
        <div class="col-12 buttonsMenu">
          <b-button @click="chStatus('ALL')" :pressed="(status == 'ALL')" variant="outline-primary" class="btn-lg statusBtn">Todos</b-button>
          <b-button @click="chStatus('N')" :pressed="(status == 'N')" variant="outline-dark" class="btn-lg statusBtn">Nuevo</b-button>
          <b-button @click="chStatus('BV')" :pressed="(status == 'BV')" variant="outline-warning" class="btn-lg statusBtn">Verificando</b-button>
          <b-button @click="chStatus('C')" :pressed="(status == 'C')" variant="outline-success" class="btn-lg statusBtn">Convertido</b-button>
          <b-button @click="chStatus('D')" :pressed="(status == 'D')" variant="outline-danger" class="btn-lg statusBtn">Descartado</b-button>
        </div>
      </b-row>
      <b-row>
        <div v-for="(applicant, index) in presentados" class="col-3 aspirant-box" :class="applicant.status">
          <div class="picture-frame">
            <div class="aspirant-pic">
              <router-link :to="'/3de3-admin/ingreso/'+applicant.id"><img class="img-fluid" :src="'http://avatars.io/twitter/'+applicant.twitter" /></router-link>
            </div>
          </div>
          <div class="party"> 
            <img class="party-icon" :src="applicant.partyPic" />
          </div>
          <div class="aspirant-name">
            {{ applicant.name }} {{ applicant.lastname }}
          </div>
          <div class="aspirant-position">
            {{ applicant.aspiredPosition }}
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
  name: 'ingresos',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      presentados: [
      ],
      status: "ALL",
    }
  },
  methods: {
    getPresentados: function() {
      HTTP.get('/3de3-admin/presentados/')
        .then(response => {
          this.presentados = response.data
        })
        .catch(e => {
          this.errors = e
        })
    },
    chStatus: function(newStatus) {
      this.status = newStatus;
      if (newStatus == 'ALL')
        newStatus = '';
      HTTP.get('/3de3-admin/presentados/'+newStatus)
        .then(response => {
          this.presentados = response.data
        })
        .catch(e => {
          this.errors = e
        })
    },
  },
  beforeMount() {
    this.getPresentados()
  }
}
</script>
<style scoped>
.aspirant-box {
  margin: 15px 0 25px 0;
  border-radius: 5px;
}
.party-icon {
  width:60px;
  position:absolute;
  border: 5px solid #fff;
  border-radius: 50% !important;
  top:5px;
  right:25px;
  z-index:11;
}

.picture-frame {
  border: 5px solid #000;
  border-radius: 50% !important;
  overflow:hidden;
}
.picture-frame:hover {
  border: 5px solid #a32b52;
}
.aspirant-pic {
  z-index:9;
}
.aspirant-pic:hover, .pic-buttons:hover + .aspirant-pic {
  background-color: #EF2466;
  border-radius: 50%;
  position:relative;
}
.aspirant-pic:hover img, .pic-buttons:hover + .aspirant-pic img {
  opacity: 0.5;
}
.aspirant-name {
  font-weight:bolder;
  font-size:1.2em;
}
.aspirant-position {
  font.size: 0.9em;
}
.N {
  background-color: rgba(255,255,255,0.2);
}
.BV {
  background-color: rgba(255,193,7,0.2)
}
.C {
  background-color: rgba(40,167,69,0.2);
}
.D {
  background-color: rgba(220,53,69,0.2);
}
.statusBtn {
  margin-left:10px;
  margin-right:10px;
}
.buttonsMenu {
  margin-top:45px;
  margin-bottom:45px;
}
</style>
