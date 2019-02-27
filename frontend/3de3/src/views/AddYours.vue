<template>
  <div class="home">
    <b-container>
      <b-row>
        <div class="col-2"></div>
        <div class="col-10">
          <h2>Publica tu #3d<span class="blue-font">e</span>3</h2>
        </div>
      </b-row>
      <b-row class="text">
        <div class="col-2"></div>
        <div class="col-10">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat scelerisque laoreet. Nunc ut mattis magna. Sed gravida nisi lacinia bibendum aliquet. Fusce feugiat felis ut sem porta luctus. In et leo a dui pretium sollicitudin nec vitae nunc. Praesent interdum ipsum ac luctus egestas. Aenean nec neque vitae mauris maximus posuere. Quisque scelerisque quam eu mi ornare, ac semper tellus vestibulum. Proin dapibus vehicula dui. In ornare quam mauris, id tristique arcu semper a. Nunc eget lacus quis orci cursus rhoncus vitae at elit. Aliquam pharetra massa eu orci volutpat, quis iaculis tellus tempus. Integer eu neque massa. Suspendisse arcu libero, pharetra vel dolor nec, sollicitudin accumsan nisl. Ut risus ligula, iaculis sit amet leo quis, placerat interdum augue. Cras iaculis ante sed suscipit posuere.</p>
        </div>
      </b-row>
      <b-row>
        <div class="col-12"><h4>Formulario 3de3 Guatemala</h4></div>
        <div class="col-12"><h5>Datos del declarante</h5></div>
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
              v-model="form.otherGender" 
              :disabled="form.gender != 'O'" 
              :class="{ error: $v.form['otherGender'].$error }" 
              @input="$v.form['otherGender'].$touch()"
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
              v-model="form.otherEthnic" 
              :disabled="form.ethnicGroup != 'O'" 
              :class="{ error: $v.form['otherEthnic'].$error }" 
              @input="$v.form['otherEthnic'].$touch()"
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
              v-model="form.civilStatus" 
              :options="civilStatusList"
              :class="{ error: $v.form['civilStatus'].$error }" 
              @input="$v.form['civilStatus'].$touch()"
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
              v-model="form.committee" 
              :class="{ error: $v.form['committee'].$error }" 
              @input="$v.form['committee'].$touch()"
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
              v-model="form.otherName" 
              type="text" 
              placeholder="Nombres" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.otherLastname" 
              type="text" 
              placeholder="Apellidos"
            />
          </div>
        </b-row>
        <b-row>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.otherPhone" 
              type="text" 
              placeholder="Teléfono" 
            />
          </div>
          <div class="col-12 col-lg-6">
            <b-form-input 
              v-model="form.otherEmail" 
              type="text" 
              placeholder="Correo electrónico"
            />
          </div>
        </b-row>
        <b-row class="justify-content-center buttonholder">
          <b-button variant="dark" size="lg">Carta de autorización<img class="form-input-img" src="../assets/download.png"/></b-button>
        </b-row>
        <b-row class="justify-content-center buttonholder">
          <div class="col-lg-2"></div>
          <div class="col-lg-2">
            <label class="btn-dark btn-lg upload" :class="{ error: $v.form['authLetter'].$error }" @input="$v.form['authLetter'].$touch()"><img class="form-input-img-big" alt="Carta de autorización" src="../assets/up.png"><span class="inner-button">Carta de autorización</span><b-form-file v-model="form.authLetter" hidden /></label>
          </div>
          <div class="col-lg-2">
            <label class="btn-dark btn-lg upload" :class="{ error: $v.form['solvencia'].$error }" @input="$v.form['solvencia'].$touch()"><img class="form-input-img-big" alt="Solvencia Fiscal" src="../assets/sf_up.png"><span class="inner-button">Solvencia fiscal</span><b-form-file v-model="form.solvencia" hidden /></label>
          </div>
          <div class="col-lg-2">
            <b-button class="upload" variant="dark" size="lg"><img class="form-input-img-big" alt="Declaración de intereses" src="../assets/di.png"><span class="inner-button">Declaración de intereses</span></b-button>
          </div>
          <div class="col-lg-2">
            <b-button class="upload" variant="dark" size="lg"><img class="form-input-img-big" alt="Declaración patrimonial" src="../assets/dp.png"><span class="inner-button">Declaración patrimonial</span></b-button>
          </div>
          <div class="col-lg-2"></div>
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
import { required, requiredIf, email } from 'vuelidate/lib/validators';
export default {
  name: 'AddYours',
  data: function() {
    return {
      form: {
        name: '',
        lastname: '',
        gender: null,
        otherGender: '',
        ethnicGroup: null,
        otherEthnic: '',
        twitter: '',
        facebook: '',
        civilStatus: null,
        aspiredPosition: '',
        executivePosition: null,
        district: null,
        seat: '',
        municipality: null,
        partyType: '',
        party: null,
        committee: null,
        celphone: '',
        phone: '',
        email: '',
        otherName: '',
        otherLastname: '',
        otherPhone: '',
        otherEmail: '',
        authLetter: '',
        solvencia: '',
        
      },
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
      civilStatusList: [
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
        {value: "GT", text: "Guatemala"},
        {value: "DC", text: "Distrito central"},
      ],
      munis: [
        {value: null, text: "Municipio"},
      ],
      parties: [
        {value: null, text: "Seleccione partido"},
        {value: "PAN", text: "PAN" }
      ],
      civicCommittees: [
        {value: null, text: "Seleccione comité civico"},
        {value: "CCC", text: "comité civico C"}
      ],
      isSubmitted: false,
      isError: false,
      errorHeader: 'error.invalidFields',
      errors: [],
      submitting: false
    }
  },
  methods: {
    processForm: function() {
      this.$v.$touch()
      if (this.$v.$invalid) 
        console.log("FORM IS INVALID");
      console.log({ name: this.form.name, email: this.form.email });
    }
  },
  validations: {
    form: {
      name: { required },
      lastname: { required },
      gender: { required },
      otherGender: { required: requiredIf(function() {
                                            return (this.form.gender == "O") ? true : false;
                                            })
      },
      ethnicGroup: { required },
      otherEthnic: { required: requiredIf(function() {
                                            return (this.form.ethnicGroup == "O") ? true : false;
                                            })
      },
      twitter: { required },
      facebook: { required },
      civilStatus: { required },
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
                                            })
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
      authLetter: { required },
      solvencia: { required },
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
