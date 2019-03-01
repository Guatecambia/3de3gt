<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Candidatos<b-button class="addNew" to="/3de3-admin/candidato" type="button">+</b-button></h2></div>
      </b-row>
      <b-row>
        <div class="col-12 buttonsMenu">
          <b-button @click="chStatus('ALL')" :pressed="(status == 'ALL')" variant="outline-primary" class="btn-lg statusBtn">Todos</b-button>
          <b-button @click="chStatus('ASK')" :pressed="(status == 'ASK')" variant="outline-warning" class="btn-lg statusBtn">Exige #3de3</b-button>
          <b-button @click="chStatus('PUB')" :pressed="(status == 'PUB')" variant="outline-success" class="btn-lg statusBtn">Publicados</b-button>
        </div>
      </b-row>
      <b-row>
        <div v-for="(applicant, index) in candidatos" class="col-3 aspirant-box">
          <div class="picture-frame">
            <div class="aspirant-pic">
              <router-link :to="'/3de3-admin/candidato/'+applicant.id"><img class="img-fluid" :src="'http://avatars.io/twitter/'+applicant.twitter" /></router-link>
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
  name: 'candidatos',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      candidatos: [
      ],
      status: 'ALL'
    }
  },
  methods: {
    getCandidatos: function() {
      HTTP.get('/3de3-admin/candidatos/')
        .then(response => {
          this.candidatos = response.data
        })
        .catch(e => {
          this.errors = e
        })
    },
    chStatus: function(newStatus) {
      this.status = newStatus;
      if (newStatus == 'ALL')
        newStatus = '';
      HTTP.get('/3de3-admin/candidatos/'+newStatus)
        .then(response => {
          this.candidatos = response.data
        })
        .catch(e => {
          this.errors = e
        })
    },
  },
  beforeMount() {
    this.getCandidatos()
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
.ASK {
  background-color: rgba(255,193,7,0.2)
}
.PUB {
  background-color: rgba(40,167,69,0.2);
}
.statusBtn {
  margin-left:10px;
  margin-right:10px;
}
.buttonsMenu {
  margin-top:45px;
  margin-bottom:45px;
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
