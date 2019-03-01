<template>
  <div class="home">
    <AdminHeader />
    <b-container>
      <b-row>
        <div class="col-12 justify-content-center"><h2>Revisión de Ingreso</h2></div>
      </b-row>
      <b-form @submit.prevent="processForm">
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
            <b-form-select 
              v-model="form.gender" 
              :options="genders"
              :class="{ error: $v.form['gender'].$error }" 
              @input="$v.form['gender'].$touch()"
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.genderOther" 
              :disabled="form.gender != 'O'" 
              :class="{ error: $v.form['genderOther'].$error }" 
              @input="$v.form['genderOther'].$touch()"
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
              :class="{ error: $v.form['ethnicGroup'].$error }" 
              @input="$v.form['ethnicGroup'].$touch()"
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.ethnicOther" 
              :disabled="form.ethnicGroup != 'O'" 
              :class="{ error: $v.form['ethnicOther'].$error }" 
              @input="$v.form['ethnicOther'].$touch()"
              type="text" 
              placeholder="Especifique grupo étnico"
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
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.maritalStatus" 
              :options="maritalStatusList"
              :class="{ error: $v.form['maritalStatus'].$error }" 
              @input="$v.form['maritalStatus'].$touch()"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12"><h5>Datos del cargo</h5></div>
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
              :class="{ error: $v.form['executivePosition'].$error }" 
              @input="$v.form['executivePosition'].$touch()"
            />
          </div>
        </b-row>
        <b-row v-show="form.aspiredPosition == 'LEG'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.district" 
              :options="districts"
              :class="{ error: $v.form['district'].$error }" 
              @input="$v.form['district'].$touch()"
            />
          </div>
          <div class="colr-12 col-lg-6">
            <b-form-input 
              v-model="form.seat" 
              :class="{ error: $v.form['seat'].$error }" 
              @input="$v.form['seat'].$touch()"
              type="text" 
              placeholder="Casilla" 
            />
          </div>
        </b-row>
        <b-row v-show="form.aspiredPosition == 'M'">
          <div class="col-12 col-lg-6">
            <b-form-select 
              v-model="form.municipality" 
              :class="{ error: $v.form['municipality'].$error }" 
              @input="$v.form['municipality'].$touch()"
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
          <div class="col-12"><h5>Información de contacto</h5></div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.celphone" 
              type="text" 
              placeholder="Celular" 
              :class="{ error: $v.form['celphone'].$error }" 
              @input="$v.form['celphone'].$touch()"
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.phone" 
              type="text" 
              placeholder="Oficina/Casa"
              :class="{ error: $v.form['phone'].$error }" 
              @input="$v.form['phone'].$touch()"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.email"
              @input="$v.form['email'].$touch()"
              :class="{ error: $v.form['email'].$error }"
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
            <a :href="fileURL+'/'+form.authLetter"><label class="btn-dark btn-lg upload"><img class="form-input-img-big" alt="Carta de autorización" src="../assets/up.png"><span class="inner-button">Carta de autorización</span></label></a>
          </div>
          <div class="col-lg-2">
            <a :href="fileURL+'/'+form.solvencia"><label class="btn-dark btn-lg upload"><img class="form-input-img-big" alt="Solvencia Fiscal" src="../assets/sf_up.png"><span class="inner-button">Solvencia fiscal</span></label></a>
          </div>
          <div class="col-lg-4"></div>
        </b-row>
        <b-row>
          <div class="col-12">
            <b-button @click="chStatus('N')" :pressed="(form.status == 'N')" variant="outline-dark" class="btn-lg statusBtn">Nuevo</b-button>
            <b-button @click="chStatus('BV')" :pressed="(form.status == 'BV')" variant="outline-warning" class="btn-lg statusBtn">Verificando</b-button>
            <b-button @click="chStatus('C')" :pressed="(form.status == 'C')" variant="outline-success" class="btn-lg statusBtn">Convertido</b-button>
            <b-button @click="chStatus('D')" :pressed="(form.status == 'D')" variant="outline-danger" class="btn-lg statusBtn">Descartado</b-button>
          </div>
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
        status: ''
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
    chStatus: function(newStatus) {
      this.form.status = newStatus;
    },
    getIngreso: function() {
      HTTP.get('/3de3-admin/presentado/'+this.$route.params.id)
        .then(response => {
          this.form = response.data
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
        let formData = new FormData();
        formData.append("name", this.form.name);
        formData.append("lastname", this.form.lastname);
        formData.append("gender", this.form.gender);
        if (this.form.genderOther != null)
          formData.append("genderOther", this.form.genderOther);
        formData.append("ethnicGroup", this.form.ethnicGroup);
        if (this.form.ethnicOther != null)
          formData.append("ethnicOther", this.form.ethnicOther);
        formData.append("twitter", this.form.twitter);
        formData.append("facebook", this.form.facebook);
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
        formData.append("celphone", this.form.celphone);
        formData.append("phone", this.form.phone);
        formData.append("email", this.form.email);
        if (this.form.helpName != null)
          formData.append("helpName", this.form.helpName);
        if (this.form.helpLastname != null)
          formData.append("helpLastname", this.form.helpLastname);
        if (this.form.helpCelphone != null)
          formData.append("helpCelphone", this.form.helpCelphone);
        if (this.form.helpEmail != null)
          formData.append("helpEmail", this.form.helpEmail);
        formData.append("status", this.form.status);
        var self = this;
        HTTP.put(
          '/3de3-admin/presentado/'+this.$route.params.id, 
          formData, 
          {
            headers: {
                'Content-Type': 'text/plain'
            }
          }
        )
        .then(function (response) {
          self.$router.push('/3de3-admin/ingresos');
        })
        .catch(function (error) {
          alert("No se pudo enviar su información"+error);
        });
      }
    }
  },
  beforeMount() {
    this.getIngreso()
  },
  validations: {
    form: {
      name: { required },
      lastname: { required },
      gender: { required },
      genderOther: { required: requiredIf(function() {
                                            return (this.form.gender == "O") ? true : false;
                                            })
      },
      ethnicGroup: { required },
      ethnicOther: { required: requiredIf(function() {
                                            return (this.form.ethnicGroup == "O") ? true : false;
                                            })
      },
      twitter: { required },
      facebook: { required },
      maritalStatus: { required },
      aspiredPosition: { required },
      executivePosition: { required: requiredIf(function() {
                                                  return (this.form.aspiredPosition == "EX") ? true : false;
                                                })
      },
      district: { required: requiredIf(function() {
                                        return (this.form.aspiredPosition == "LEG") ? true : false;
                                      })
      },
      seat: { required: requiredIf(function() {
                                            return (this.form.aspiredPosition == "LEG") ? true : false;
                                            }),
              minValue: minValue(0)
      },
      municipality: { required: requiredIf(function() {
                                            return (this.form.aspiredPosition == "M") ? true : false;
                                          })
      },
      partyType: { required },
      party: { required: requiredIf(function() {
                                      return (this.form.partyType == "PP") ? true : false;
                                    })
      },
      committee: { required: requiredIf(function() {
                                      return (this.form.partyType == "CC") ? true : false;
                                    })
      },
      celphone: { required },
      phone: { required },
      email: { required, email },
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
