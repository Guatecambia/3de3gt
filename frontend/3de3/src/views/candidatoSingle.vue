<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Candidato</h2></div>
      </b-row>
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
          <div class="col-12"><h5>Datos básicos</h5></div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model.trim="form.name" 
              :class="{ error: $v.form['name'].$error }" 
              @input="$v.form['name'].$touch()"
              type="text" 
              placeholder="Nombres" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.lastname"
              :class="{ error: $v.form['lastname'].$error }" 
              @input="$v.form['lastname'].$touch()" 
              type="text" 
              placeholder="Apellidos"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.twitter" 
              type="text" 
              placeholder="cuenta-twitter" 
              :class="{ error: $v.form['twitter'].$error }" 
              @input="$v.form['twitter'].$touch()"
            />
          </div>
          <div class="col-12 col-lg-6">
            <p class="text">En caso de no tener cuenta personal por favor registrar la cuenta del partido político al que pertenece.</p>
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.facebook" 
              type="text" 
              placeholder="cuenta-facebook"
              :class="{ error: $v.form['facebook'].$error }" 
              @input="$v.form['facebook'].$touch()"
            />
          </div>
          <div class="col-12 col-lg-6">
            <p class="text">En caso de no tener cuenta personal por favor registrar la cuenta del partido político al que pertenece.</p>
          </div>
        </b-row>
        <b-row>
          <b-form-radio-group 
            v-model="form.aspiredPosition"
            :class="{ error: $v.form['aspiredPosition'].$error }" 
            @input="$v.form['aspiredPosition'].$touch()"
          >
            <b-form-radio value="EX">Ejecutivo</b-form-radio>
            <b-form-radio value="LEG">Legislativo</b-form-radio>
            <b-form-radio value="M">Municipalidad</b-form-radio>
          </b-form-radio-group>
        </b-row>
        <b-row v-show="form.aspiredPosition == 'EX'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.executivePosition" 
              :options="executivePositions"
            />
          </div>
        </b-row>
        <b-row v-show="form.aspiredPosition == 'LEG'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.district" 
              :options="districts"
            />
          </div>
          <div class="colr-12 col-lg-6">
            <b-form-input 
              v-model="form.seat" 
              type="text" 
              placeholder="Casilla" 
            />
          </div>
        </b-row>
        <b-row v-show="form.aspiredPosition == 'M'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.municipality" 
              :options="munis"
            />
          </div>
        </b-row>
        <b-row>
          <b-form-radio-group 
            v-model="form.partyType"
            :class="{ error: $v.form['partyType'].$error }" 
            @input="$v.form['partyType'].$touch()"
          >
            <b-form-radio value="PP">Partido Político</b-form-radio>
            <b-form-radio value="CC">Comité Cívico</b-form-radio>
          </b-form-radio-group>
        </b-row>
        <b-row v-show="form.partyType == 'PP'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.party" 
              :class="{ error: $v.form['party'].$error }" 
              @input="$v.form['party'].$touch()"
              :options="parties"
            />
          </div>
        </b-row>
        <b-row v-show="form.partyType == 'CC'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.party" 
              :class="{ error: $v.form['party'].$error }" 
              @input="$v.form['party'].$touch()"
              :options="civicCommittees"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-button @click="chStatus('ASK')" :pressed="(form.inAskList == true)" variant="outline-warning" class="btn-lg statusBtn">Exige #3de3</b-button>
            <b-button @click="chStatus('PUB')" :pressed="(form.published == true)" variant="outline-success" class="btn-lg statusBtn">Publicado</b-button>
            <b-button @click="chStatus('NP')" :pressed="((form.inAskList == false) && (form.published == false))" variant="outline-dark" class="btn-lg statusBtn">No publicado</b-button>
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-button variant="primary" class="btn-lg" v-b-modal.declarations>Declaraciones patrimonial y de intereses</b-button>
          </div>
            <b-modal id="declarations" size="xl" title="Declaraciones" @ok="reloadLines">
              <div>
                <span>No. de respuesta para la declaración de intereses</span>
                <b-form-input
                  v-model="lineParameters.interestsLine" 
                  type="text"
                  placeholder="No. de respuesta declaración de intereses"
                />
                <span>No. de respuesta para la declaración patrimonial</span>
                <b-form-input 
                  v-model="lineParameters.patrimonialLine" 
                  type="text" 
                  placeholder="No. de respuesta declaración patrimonial" 
                />
              </div>
            </b-modal>
        </b-row>
        <b-row>
          <div class="col-12"><h5>Datos personales</h5></div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.gender" 
              :options="genders"
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.genderOther" 
              :disabled="form.gender != 'O'" 
              type="text" 
              placeholder="Especifique género"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.ethnicGroup" 
              :options="ethnics"
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.ethnicOther" 
              :disabled="form.ethnicGroup != 'O'" 
              type="text" 
              placeholder="Especifique grupo étnico"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.maritalStatus" 
              :options="maritalStatusList"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12"><h5>Información de contacto</h5></div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.celphone" 
              type="text" 
              placeholder="Celular" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.phone" 
              type="text" 
              placeholder="Oficina/Casa"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.email"
              placeholder="Correo electrónico"
            />
            <p class="error-message" v-if="!$v.form['email'].email">Ingrese una dirección de correo electrónico válida</p>
          </div>
        </b-row>
        <b-row>
          <div class="col-12">
            <p class="text">En caso de que exista una persona adicional al declarante que funja como contacto entre la iniciativa y el declarante, incluya la siguiente información.</p>
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.helpName" 
              type="text" 
              placeholder="Nombres" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.helpLastname" 
              type="text" 
              placeholder="Apellidos"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.helpCelphone" 
              type="text" 
              placeholder="Teléfono" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.helpEmail" 
              @input="$v.form['helpEmail'].$touch()"
              :class="{ error: $v.form['helpEmail'].$error }"
              type="text" 
              placeholder="Correo electrónico"
            />
            <p class="error-message" v-if="!$v.form['email'].email">Ingrese una dirección de correo electrónico válida</p>
          </div>
        </b-row>
        <b-row class="justify-content-center buttonholder">
          <div class="col-lg-4"></div>
          <div class="col-lg-2">
            <a target="_blank" :href="fileURL+'/'+form.authLetter"><label class="btn-dark btn-lg upload"><img class="form-input-img-big" alt="Carta de autorización" src="../assets/up.png"><span class="inner-button">Carta de autorización</span></label></a>
          </div>
          <div class="col-lg-2">
            <a target="_blank" :href="fileURL+'/'+form.solvencia"><label class="btn-dark btn-lg upload"><img class="form-input-img-big" alt="Solvencia Fiscal" src="../assets/sf_up.png"><span class="inner-button">Solvencia fiscal</span></label></a>
          </div>
          <div class="col-lg-4"></div>
        </b-row>
        <b-row>
          <div class="col-12 justify-content-center" >
            <b-button type="submit" class="btn-submit btn-lg">Enviar</b-button>
          </div>
        </b-row>
      </b-form>
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
import {HTTP} from '../../http-constants'
import {baseURL} from '../../http-constants'
import { required, requiredIf, email, minValue } from 'vuelidate/lib/validators';

export default {
  name: 'ingresoSingle',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      form: {
        id: null,
        name: '',
        lastname: '',
        gender: null,
        genderOther: '',
        ethnicGroup: null,
        ethnicOther: '',
        twitter: '',
        facebook: '',
        maritalStatus: null,
        aspiredPosition: '',
        executivePosition: null,
        district: null,
        seat: null,
        municipality: null,
        partyType: '',
        party: null,
        celphone: '',
        phone: '',
        email: '',
        helpName: null,
        helpLastname: null,
        helpCelphone: null,
        helpEmail: null,
        authLetter: '',
        solvencia: '',
        status: '',
        interestsLine: null,
        patrimonialLine: null,
      },
      lineParameters: {
        interestsLine: null,
        patrimonialLine: null,
      },
      fileURL: baseURL,
      genders: [
        {value: null, text: "Género"},
        {value: "M", text: "Masculino"},
        {value: "F", text: "Femenino"},
        {value: "O", text: "Otro"}
      ],
      ethnics: [
        {value: null, text: "Grupo étnico"},
        {value: "I", text: "Indígena"},
        {value: "ML", text: "Ladino/Mestizo"},
        {value: "O", text: "Otro"}
      ],
      maritalStatusList: [
        {value: null, text: "Estado civil (al presentar la declaración)"},
        {value: "S", text: "Soltero"},
        {value: "C", text: "Casado"},
        {value: "UH", text: "En unión de hecho"},
        {value: "O", text: "Otro"}
      ],
      executivePositions: [
        {value: null, text: "Cargo"},
        {value: "P", text: "Presidente"},
        {value: "V", text: "Vicepresidente"}
      ],
      districts: [
        {value: null, text: "Distrito"},
        {value: 1, text: "Guatemala"},
        {value: 2, text: "Distrito central"},
      ],
      munis: [
        {value: null, text: "Municipio"},
      ],
      parties: [
        {value: null, text: "Seleccione partido"},
        {value: 1, text: "PAN" }
      ],
      civicCommittees: [
        {value: null, text: "Seleccione comité civico"},
        {value: 2, text: "comité civico C"}
      ],
    }
  },
  methods: {
    getGenerics: function() {
      HTTP.get('/generico/distritos?limit=1000&offset=0')
        .then(response => {
          this.districts = response.data['results'];
          this.districts.unshift({value: null, text: "Listado"});
        })
        .catch(e => {
          this.errors = e
        });
      HTTP.get('/generico/municipios?limit=1000&offset=0')
        .then(response => {
          this.munis = response.data['results'];
          this.munis.unshift({value: null, text: "Municipio"});
        })
        .catch(e => {
          this.errors = e
        })
      HTTP.get('/generico/partidos?limit=1000&offset=0')
        .then(response => {
          this.parties = response.data['results'];
          this.parties.unshift({value: null, text: "Seleccione partido"});
        })
        .catch(e => {
          this.errors = e
        })
      HTTP.get('/generico/comites?limit=1000&offset=0')
        .then(response => {
          this.civicCommittees = response.data['results'];
          this.civicCommittees.unshift({value: null, text: "Seleccione comité civico"});
        })
        .catch(e => {
          this.errors = e
        })
    },
    chStatus: function(newStatus) {
        if (newStatus == 'NP') {
          this.form.inAskList = false
          this.form.published = false
        }
        if (newStatus == 'ASK') {
          this.form.inAskList = true
          this.form.published = false
        }
        if (newStatus == 'PUB') {
          if (this.lineParameters.interestsLine && this.lineParameters.patrimonialLine) {
            if (this.form.solvencia && this.form.authLetter) {
              this.form.inAskList = false
              this.form.published = true
            }
            else {
              alert("Para poder publicar debe tener solvencia y carta de autorización. Para eso debe convertirlo desde un Ingreso");
            }
          }
          else {
            alert("Debe de configurar las declaraciones patrimonial y de intereses antes de poder publicar");
          }
        }
    },
    getCandidato: function() {
      HTTP.get('/3de3-admin/candidato/'+this.$route.params.id)
        .then(response => {
          this.form = response.data
          /* null parameteres in general form, so if they don't change backend will do nothing, but
          but if they are in the parameters, backend procedure will reload the lines */
          this.lineParameters.interestsLine = this.form.interestsLine;
          this.lineParameters.patrimonialLine = this.form.patrimonialLine;
          this.form.interestsLine = null;
          this.form.patrimonialLine = null;
        })
        .catch(e => {
          this.errors = e
        })
    },
    reloadLines: function() {
      if (this.lineParameters.patrimonialLine && this.lineParameters.interestsLine) {
        this.form.patrimonialLine = this.lineParameters.patrimonialLine;
        this.form.interestsLine = this.lineParameters.interestsLine;
      }
      else {
        alert("Debe ingresar número de respuesta en los dos archivos para poder cargar");
      }
    },
    processForm: function() {
      this.$v.$touch()
      if (this.$v.$invalid) {
        alert("Por favor ingrese todos los campos obligatorios para continuar");
      }
      else {
        let formData = new FormData();
        formData.append("name", this.form.name);
        formData.append("lastname", this.form.lastname);
        if (this.form.gender != null)
            formData.append("gender", this.form.gender);
        if (this.form.genderOther != null)
          formData.append("genderOther", this.form.genderOther);
        if (this.form.ethnicGroup != null)
          formData.append("ethnicGroup", this.form.ethnicGroup);
        if (this.form.ethnicOther != null)
          formData.append("ethnicOther", this.form.ethnicOther);
        formData.append("twitter", this.form.twitter);
        if (this.form.facebook != null)
            formData.append("facebook", this.form.facebook);
        if (this.form.maritalStatus != null)
            formData.append("maritalStatus", this.form.maritalStatus);
        formData.append("aspiredPosition", this.form.aspiredPosition);
        if ((this.form.executivePosition != null) && (this.form.aspiredPosition == "EX"))
          formData.append("executivePosition", this.form.executivePosition);
        if ((this.form.district != null) && (this.form.aspiredPosition == "LEG"))
          formData.append("district", this.form.district);
        if ((this.form.seat != null) && (this.form.aspiredPosition == "LEG"))
          formData.append("seat", this.form.seat);
        if ((this.form.municipality != null) && (this.form.aspiredPosition == "M"))
          formData.append("municipality", this.form.municipality);
        formData.append("party", this.form.party);
        if (this.form.celphone != null)
            formData.append("celphone", this.form.celphone);
        if (this.form.phone != null)
            formData.append("phone", this.form.phone);
        if (this.form.email != null)
            formData.append("email", this.form.email);
        if (this.form.helpName != null)
          formData.append("helpName", this.form.helpName);
        if (this.form.helpLastname != null)
          formData.append("helpLastname", this.form.helpLastname);
        if (this.form.helpCelphone != null)
          formData.append("helpCelphone", this.form.helpCelphone);
        if (this.form.helpEmail != null)
          formData.append("helpEmail", this.form.helpEmail);
        if (this.form.interestsLine != null)
          formData.append("interestsLine", this.form.interestsLine);
        if (this.form.patrimonialLine != null)
          formData.append("patrimonialLine", this.form.patrimonialLine);
        if (this.form.authLetter != null)
          formData.append("authLetter.name", this.form.authLetter);
        if (this.form.solvencia != null) 
          formData.append("solvencia.name", this.form.solvencia);
        formData.append("inAskList", this.form.inAskList);
        formData.append("published", this.form.published);
        var self = this;
        if (this.$route.params.id) {        
          HTTP.put(
            '/3de3-admin/candidato/'+this.$route.params.id, 
            formData, 
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            self.$router.push('/3de3-admin/candidatos');
          })
          .catch(function (error) {
            alert("No se pudo enviar su información"+error);
          });
        }
        else {
          HTTP.post(
            '/3de3-admin/candidatos/', 
            formData, 
            {
              headers: {
                  'Content-Type': 'text/plain'
              }
            }
          )
          .then(function (response) {
            self.$router.push('/3de3-admin/candidatos');
          })
          .catch(function (error) {
            alert("No se pudo enviar su información"+error);
          });
        }
      }
    },
    delInstance: function() {
      var self = this;
      HTTP.delete(
        '/3de3-admin/candidato/'+this.$route.params.id, 
        {
          headers: {
              'Content-Type': 'text/plain'
          }
        }
      )
      .then(function (response) {
        console.log("Candidato eliminado");
        self.$router.push('/3de3-admin/candidatos');
      })
      .catch(function (error) {
        alert("Error al borrar " + error);
      });
    }
  },
  mounted() {
    this.getGenerics()
    this.getCandidato()
  },
  validations: {
    form: {
      name: { required },
      lastname: { required },
      twitter: { required },
      facebook: { required },
      aspiredPosition: { required },
      partyType: { required },
      party: { required: requiredIf(function() {
                                      return (this.form.partyType == "PP") ? true : false;
                                    })
      },
      committee: { required: requiredIf(function() {
                                      return (this.form.partyType == "CC") ? true : false;
                                    })
      },
      email: { email },
      helpEmail: { email },
    }
  }
}
</script>
<style scoped>
.text {
  text-align:justify;
}
.text-right {
  text-align: right;
}
h4, h5 {
  margin:35px 0;
  text-align: justify;
  font-weight: bold;
}
.custom-radio {
  margin-left:65px;
}
.row {
  padding: 15px 0;
}
input, select {
  background-color: #e2e2e2;
  color: #333;
}
input::placeholder {
  color: #555;
}
.form-input-img {
  max-width:25px;
  margin-left:15px;
}
.form-input-img-big {
  max-width: 80px;
}
.row.buttonholder {
  margin-top: 50px;
}
.upload {
  margin-left: 15px;
  margin-right: 15px;
}
.inner-button {
  display: block;
  font-size: 0.8em;
}
.btn-submit {
  background: #EF2466;
  border-color: #EF2466;
}
.error {
  border: 1px solid red;
  background-color: #e69fa6;
}
.statusBtn {
  margin-left:10px;
  margin-right:10px;
}
</style>
<style>
.custom-control-input:checked ~ .custom-control-label::before {
  color: #EF2466;
  border-color: #333;
  background-color: #EF2466;
}
.custom-radio .custom-control-input:checked ~ .custom-control-label::after {
  background-image: none;
}
input:disabled {
  opacity: 0.5 !important;
}
select:invalid, select option[value=""], select option[value=null] {
  color: #888;
}
select option[value!=""] > select, select option[value!=null] > select {
  color: #333;
  background-color: #e2e2e2;
}
::selection {
  background: #EF2466; 
  color: white;
}
::-moz-selection {
  background: #EF2466; 
  color: white;
}
</style>
