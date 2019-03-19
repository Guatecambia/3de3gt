<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Municipio</h2></div>
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
              v-model="muni.department"
              @input="$v.muni['department'].$touch()"
              :class="{ error: $v.muni['department'].$error }"
              type="text" 
              placeholder="Nombre del departamento" 
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-form-input 
              v-model="muni.name"
              @input="$v.muni['name'].$touch()"
              :class="{ error: $v.muni['name'].$error }"
              type="text" 
              placeholder="Nombre del municipio" 
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
  name: 'muniSingle',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      muni: {
        id: '',
        department: '',
        name: '',
      }
    }
  },
  methods: {
    getMuni: function() {
      HTTP.get('/3de3-admin/muni/'+this.$route.params.id)
        .then(response => {
          this.muni = response.data
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
        formData.append("department", this.muni.department);
        formData.append("name", this.muni.name);
        if (this.$route.params.id) {
          HTTP.put(
            '/3de3-admin/muni/'+this.$route.params.id, 
            formData, 
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            console.log("Datos Guardados");
            self.$router.push('/3de3-admin/municipios');
          })
          .catch(function (error) {
            alert("Error al guardar " + error);
          });
        }
        else {
          HTTP.post(
            '/3de3-admin/munis/',
            formData,
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            console.log("Datos Guardados");
            self.$router.push('/3de3-admin/municipios');
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
        '/3de3-admin/muni/'+this.$route.params.id, 
        {
          headers: {
              'Content-Type': 'text/plain'
          }
        }
      )
      .then(function (response) {
        console.log("Datos Guardados");
        self.$router.push('/3de3-admin/municipios');
      })
      .catch(function (error) {
        alert("Error al guardar " + error);
      });
    }
  },
  mounted() {
    if (this.$route.params.id)
      this.getMuni()
  },
  validations: {
    muni: {
      name: { required },
      department: { required }
    },
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
