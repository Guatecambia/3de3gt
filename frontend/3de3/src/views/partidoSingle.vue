<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Partido</h2></div>
      </b-row>
      <b-form @submit.prevent="delInstance">
        <b-row>
          <div class="col-11"></div>
          <div class="col-1">
            <b-button v-if="this.$route.params.id" type="submit" class="btn-submit btn-lg justify-content-end">Borrar</b-button>
          </div>
        </b-row>
      </b-form>
      <b-form @submit.prevent="processForm">
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.name"
              @input="$v.party['name'].$touch()"
              :class="{ error: $v.party['name'].$error }"
              type="text" 
              placeholder="Nombre del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.shortName"
              type="text" 
              placeholder="Nombre corto del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-select 
              v-model="party.tType" 
              :options="party_types"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.phone"
              type="text" 
              placeholder="Telefono del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.twitter"
              type="text" 
              placeholder="Twitter del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.facebook"
              type="text" 
              placeholder="Facebook del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="party.secretary"
              type="text" 
              placeholder="Secretario del partido" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 justify-content-center" >
            <b-button type="submit" class="btn-submit btn-lg">Guardar</b-button>
          </div>
        </b-row>
      </b-form>
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
import {HTTP} from '../../http-constants'
import { required } from 'vuelidate/lib/validators';
export default {
  name: 'partidoSingle',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      party: {
        id: '',
        name: '',
        shortName: '',
        tType: '',
        phone: '',
        facebook: '',
        twitter: '',
        secretary: '',
      },
      party_types: [
        { value: "PP", text: "Partido Político"},
        { value: "CC", text: "Comité Civico" }
      ]
    }
  },
  methods: {
    getParty: function() {
      HTTP.get('/3de3-admin/partido/'+this.$route.params.id)
        .then(response => {
          this.party = response.data
        })
        .catch(e => {
          this.errors = e
        })
    },
    processForm: function() {
      this.$v.$touch()
      if (this.$v.$invalid) {
        alert("Por favor ingrese todos los campos obligatorios para continuar");
      }
      else {
        var self = this;
        let formData = new FormData();
        formData.append("name", this.party.name);
        formData.append("tType", this.party.tType);
        formData.append("shortName", this.party.shortName);
        formData.append("phone", this.party.phone);
        formData.append("facebook", this.party.facebook);
        formData.append("twitter", this.party.twitter);
        formData.append("secretary", this.party.secretary);
        if (this.$route.params.id) {
          HTTP.put(
            '/3de3-admin/partido/'+this.$route.params.id, 
            formData, 
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            console.log("Datos Guardados");
            self.$router.push('/3de3-admin/partidos');
          })
          .catch(function (error) {
            alert("Error al guardar " + error);
          });
        }
        else {
          HTTP.post(
            '/3de3-admin/partidos/',
            formData,
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            console.log("Datos Guardados");
            self.$router.push('/3de3-admin/partidos');
          })
          .catch(function (error) {
            alert("Error al guardar " + error);
          });
        }
      }
    },
    delInstance: function() {
      var self = this;
      HTTP.delete(
        '/3de3-admin/partido/'+this.$route.params.id, 
        {
          headers: {
              'Content-Type': 'text/plain'
          }
        }
      )
      .then(function (response) {
        console.log("Datos Guardados");
        self.$router.push('/3de3-admin/partidos');
      })
      .catch(function (error) {
        alert("Error al guardar " + error);
      });
    }
  },
  mounted() {
    if (this.$route.params.id)
      this.getParty()
  },
  validations: {
    party: {
      name: { required },
      tType: { required }
    }
  }
}
</script>
<style scoped>
h2 {
  margin-top:45px;
  margin-bottom: 45px;
}
input {
  font-size: 1.5em;
}
.row {
  margin-top:45px;
}
.btn-submit {
  background-color: #EF2466;
  border:none;
}
.error {
  border: 1px solid red;
  background-color: #e69fa6;
}
</style>
