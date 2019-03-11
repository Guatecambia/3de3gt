<template>
  <div class="home">
    <Header />
    <b-container>
      <b-row>
        <div class="col-2"></div>
        <div class="col-10">
          <h2>Publica tu #3d<span class="blue-font">e</span>3</h2>
        </div>
      </b-row>
      <b-row class="text">
        <div class="col-12">
          <div class="instrucciones-block">
            <b-button class="instrucciones-btn" variant="info" v-b-toggle="'instrucciones'">
              Instrucciones
            </b-button>
            <b-collapse :id="'instrucciones'" class="instrucciones-body">

              <h3>Manual para presentación de declaraciones</h3>
              <p>El presente instructivo está dirigido para todas y todos aquellos políticos comprometidos con la transformación política  de Guatemala, que reconocen la necesidad de reconstruir la confianza ciudadana en los políticos, y han decidido publicar de forma voluntaria sus tres declaraciones. </p>
              <p>El documento señala el proceso de revisión y validación de las declaraciones, así como indicaciones sobre el llenado de las declaraciones. </p>
              
              <h3>Proceso de revisión y validación de las declaraciones</h3>
              <p>La revisión consiste en verificar que los campos se llenaron de forma acertada y completa por parte del declarante. Una vez que un funcionario o candidato envía su información, se procurará atenderla a la brevedad posible e iniciar así el proceso de revisión. El orden de revisión se realizará conforme lleguen las declaraciones al sistema.</p>
              <p>La plataforma 3de3 cuenta con una sección donde el candidato o candidata declarante, ingresará su información de contacto, y también la información de un responsable designado, con quien se hará la validación y verificación de las declaraciones.</p>
              <p>Una vez recibidas las tres declaraciones y la carta de consentimiento de publicación firmada por el declarante, el equipo 3de3 llamará personalmente al candidato o persona designada como responsable por parte del partido o por el mismo candidato, para verificar que la información recibida haya sido enviada de manera consciente y voluntaria para su publicación en la plataforma electrónica 3de3.gt.</p>
              <p>Con la confirmación de la información se realizará una primera revisión de las declaraciones y de haber observaciones con respecto a información omitida en el formulario, se enviarán por correo electrónico y se contactará vía telefónica al candidato y contacto designado, para que se pueda completar.  Una vez que las observaciones han sido subsanadas -o en caso de no haber inconsistencias- se les notificará que sus declaraciones están listas para ser publicadas. Si el funcionario no atiende las observaciones señaladas, no se procederá a su publicación.</p>
              <p>Nota: No toda omisión genera observación. </p>
              
              <h3>Declaración Patrimonial</h3>
              <p>Sección I. Datos del declarante.</p>
              <ul>
                <li>Asegurar que los datos corresponden al declarante. </li>
                <li>Confirmar que se indique correctamente estado civil, pues ello permitirá saber si es necesario declarar información de cónyuge/concubinario o no.</li>
              </ul>
              <p>Sección II. Datos de identificación personal del cónyuge </p>
              <ul>
                <li>Llenar esta sección solo en caso de que el declarante sea casado/a</li>
                <li>Por favor llenar cada uno de los campos que aplique</li>
              </ul>
              <p>Sección IV. Nombres y apellidos de hijos dependientes. </p>
              <ul>
                <li>Llenar esta sección solo en caso de que el declarante tenga hijos</li>
                <li>Por favor llenar cada uno de los campos que aplique</li>
              </ul>
              <p>Sección V. Información Patrimonial</p>
              <p>5.1. Activos</p>
              <ul>
                <li>A) Bienes –Activo-, el mismo se integra por los siguientes rubros:</li>
                  <ul>
                    <li>a. Bienes Muebles:</li>
                      <ul>
                        <li>1. Acreencias: Detallar el nombre completo de las instituciones, y/o personas, de quienes se es acreedor.</li>
                        <li>2. Alhajas: Se debe individualizar separadamente las de oro, plata, platino y/o piedras preciosas, consignando el valor a que ascienden en conjunto.</li>
                        <li>3. Bancos: Especificar las diferentes cuentas de ahorro, depósitos monetarios. Debe especificar el banco en el que tiene la cuenta. No es necesario agregar números de cuentas.</li>
                        <li>4. Biblioteca: Sólo se debe consignar el valor a que ascienden en conjunto.</li>
                        <li>5. Diversos: Detalle de todos aquellos bienes que posea, tales como:</li>
                          <ul>
                            <li>5.1 Contratos funerarios, mausoleos;</li>
                            <li>5.2 Establecimientos comerciales;</li>
                            <li>5.3 Inversiones nacionales o internacionales;</li>
                            <li>5.4 Maquinaria, talleres;</li>
                            <li>5.5 Mobiliario y equipo de oficina profesional;</li>
                            <li>5.6 Acciones nominativas de Sociedades Mercantiles, así como cualquier otro ingreso de beneficio personal que se hayan obtenido.</li>
                            <li>5.7 Títulos de agua, y derechos telefónicos; y,</li>
                            <li>5.8 Títulos de Crédito.</li>
                          </ul>
                        <li>6. Menaje de casa: Indicar los muebles de su residencia consignando el valor a que ascienden en conjunto. Si se encuentran fuera del país por razón de su función pública, consignar su valor en conjunto, deberá indicar el país en donde se encuentran.</li>
                        <li>7. Semovientes: Si se trata de lotes formados por varios semovientes, indique la cantidad en que están compuestos cada lote, la clase de estos, (bovino, equino, porcino, caballar u otros) así como el valor  en conjunto de los mismos.</li>
                        <li>8. Vehículos: Se debe indicar tipo, marca, línea, serie, modelo, y color, consignando el valor estimado de cada uno.</li>
                        <li>Si tiene bienes muebles en el exterior del país, deberá indicar el país. </li>
                      </ul>
                    <li>b. Bienes Inmuebles Urbanos o Rústicos:</li>
                      <ul>
                        <li>1. Su ubicación (municipio y departamento), con el valor declarado o el estimado.</li>
                        <li>3. Detallar los bienes inmuebles que esté amortizando por medio de cuotas niveladas o abonos, indicando el valor nominal y el saldo deudor que a la fecha tenga.</li>
                        <li>4. Si tiene bienes inmuebles en el exterior del país, deberá indicar su ubicación geográfica, consignando el valor del inmueble, aclarando si ya canceló dicha propiedad o se encuentra amortizando el valor de la misma, indicando el saldo deudor que a la fecha tenga, si fuera el caso.</li>
                      </ul>
                  </ul>
                <li>B) Acreedores -Pasivo-, el mismo se integra de la siguiente forma:</li>
                  <ul>
                    <li>a. Bancos;</li>
                    <li>b. Casas Comerciales;</li>
                    <li>c. Personas Individuales; y</li>
                    <li>d. Personas Jurídicas.</li>
                  </ul>
              </ul>
              <p>Sección VI. Declaración Jurada</p>
              <ul>
                <li>Agregar nombre completo del declarante</li>
                <li>Agregar fecha en la que presenta la declaración</li>
              </ul>
              <h3>Declaración de Intereses</h3>
              <p>Sección I. Datos del declarante.</p>
              <ul>
                <li>Por favor llenar cada uno de los campos que aplique</li>
                <li>En el campo: “Cargo público de elección popular que ocupa actualmente” aplica para aquellos funcionarios que estén buscando una reelección.</li>
                <li>En el campo: “Cargo público por nombramiento que ocupa actualmente” se refiere a aquellos funcionarios públicos que son nombrados por autoridades competentes para ejercer el cargo (ministros, viceministros, secretarios, etc.).</li>
                <li>En el campo: “partido político” indicar el partido por el que postula en las Elecciones Generales 2019.</li>
                <li>En el campo: “Cargo público al que aspira” por favor llenarlo según corresponda:</li>
                <ul>
                  <li>En caso de ser al poder ejecutivo, solamente debe de indicar si es aspirante a Presidencia o Vicepresidencia, los otros campos de la sección debe dejarlos en blanco. </li>
                  <li>Si aspira al Legislativo, por el listado nacional, únicamente debe dejarlo indicado con el número de casilla que ocupa, ejemplo: Diputado por el Listado Nacional, primera casilla. Los otros campos de la sección debe dejarlos en blanco.</li>
                  <li>Si aspira al Legislativo, por listado distrital, debe de llenar los campos correspondientes. Cargo al que aspira, casilla que ocupa en el listado y distrito por el que se postula. Ejemplo: Diputado Distrital, primera casilla/Sacatepéquez.</li>
                  <li>Si aspira a una alcaldía, debe de llenar los campos de la sección que correspondan. Cargo al que aspira, departamento y municipio. Ejemplo: Alcalde municipal/Progreso/Guastatoya.</li>
                </ul>
              </ul>
              <p>Sección II. Grupo Familiar. </p>
              <ul>
                <li>Por favor declarar los datos solicitados en la sección, sobre su grupo familiar. En las instrucciones de la sección II, está detallado quienes son considerados grupo familiar en esta sección. Por familiares se considera: cónyuge, conviviente, hijos mayores de edad, hermanos, padres, cuñados, yernos, nueras.</li>
              </ul>
              <p>Sección III. Intereses económicos y Financieros. </p>
              <ul>
                <li>Por favor llenar todos los campos que corresponda. </li>
                <li>En esta sección se reporta la información sobre intereses de carácter económico y financiero que podría influir en las decisiones tomadas por el declarante en razón del cargo que ostentará en caso de ser electo.</li>
                <li>La parte No. 1 de esta sección, “Participación del declarante en direcciones y consejos administrativos”, corresponde a cargos o funciones que el declarante desempeña o ha desempeñado en los últimos 2 años  en órganos directivos de organizaciones con fines de lucro, es decir, empresas o sociedades mercantiles y organizaciones no lucrativas, pudiendo  recibir o no remuneración por esta participación.</li>
                <li>La parte No. 2 de esta sección, “Participación en consejos de administración DE FAMILIARES Y DEPENDIENTES ECONÓMICOS”. Se refiere a cargos o funciones que al momento de la presentación de la declaración desempeña algún familiar (Cónyuge, conviviente, hijos, hermanos padres, yernos, nueras, suegros) del declarante o personas bajo su dependencia en órganos directivos de organizaciones con fines de lucro, es decir, empresas, pudiendo recibir o no una remuneración por esta participación. </li>
              </ul>
              <p>Sección IV. Actividades Profesionales y Empresariales. </p>
              <ul>
                <li>Por favor llenar todos los campos que apliquen.</li>
                <li>Esta sección aporta información sobre actividades profesionales y empresariales, así como cargos y funciones que podrían ser percibidos o susceptibles de influir en decisiones tomadas por el declarante en el ejercicio de sus funciones, esto incluye aquellas empresas de las que declarante es propietario, si fueron o no remuneradas. La sección contiene tres componentes: Posición y cargos desempeñados por el declarante en entidades durante los últimos cinco años; actividades profesionales y/o empresariales desempeñadas como persona fiscal por el declarante en los últimos cinco años; y actividades profesionales/empresariales, cargos y funciones de familiares y dependientes económicos. </li>
              </ul>
              <p>Sección V. Financiamiento Electoral.</p>
              <ul>
                <li>En esta sección se declara la información correspondiente al financiamiento de la campaña electoral del declarante. Enlista los montos recibidos, las organizaciones y financistas que aportaron a la campaña , los límites y presupuesto de la campaña electoral. </li>
              </ul>
              <h3>Declaración Fiscal (solvencia)</h3>
              <ul>
                <li>Es el documento extendido por la Superintendencia de Administración Tributaria (SAT) en el que se indica que el declarante está solvente en sus obligaciones fiscales. </li>
              </ul>
            </b-collapse>
          </div>
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
          <b-button variant="dark" size="lg" href="/static/carta_de_consentimiento_3de3.pdf" target="_blank">Carta de autorización<img class="form-input-img" src="../assets/download.png"/></b-button>
        </b-row>
        <b-row class="justify-content-center buttonholder">
          <div class="col-lg-2"></div>
          <div class="col-lg-2">
            <label class="btn-dark btn-lg upload" :class="{ error: $v.form['authLetter'].$error }" @input="$v.form['authLetter'].$touch()"><img class="form-input-img-big" alt="Carta de autorización" src="../assets/up.png"><span class="inner-button">Carta de autorización</span><b-form-file v-model="form.authLetter" accept="application/pdf" hidden /></label>
          </div>
          <div class="col-lg-2">
            <label class="btn-dark btn-lg upload" :class="{ error: $v.form['solvencia'].$error }" @input="$v.form['solvencia'].$touch()"><img class="form-input-img-big" alt="Solvencia Fiscal" src="../assets/sf_up.png"><span class="inner-button">Solvencia fiscal</span><b-form-file v-model="form.solvencia" accept="application/pdf" hidden /></label>
          </div>
          <div class="col-lg-2">
            <b-button class="upload" variant="dark" size="lg" href="https://docs.google.com/forms/d/e/1FAIpQLSfH9lLL5uOHOcAQw1Cvrof0w6WWUpVl4tpaYL_-_yEGP9F2MA/viewform" target="_blank"><img class="form-input-img-big" alt="Declaración de intereses" src="../assets/di.png"><span class="inner-button">Declaración de intereses</span></b-button>
          </div>
          <div class="col-lg-2">
            <b-button class="upload" variant="dark" size="lg" href="https://docs.google.com/forms/d/e/1FAIpQLSfkpGGDv727PXsfxq5Ui94biw07ACVc9lIlV3SKso7kAzMrXA/viewform" target="_blank"><img class="form-input-img-big" alt="Declaración patrimonial" src="../assets/dp.png"><span class="inner-button">Declaración patrimonial</span></b-button>
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
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import {HTTP} from '../../http-constants'
import { required, requiredIf, email, minValue } from 'vuelidate/lib/validators';
export default {
  name: 'AddYours',
  components: {
    Header,
    Footer
  },
  data: function() {
    return {
      form: {
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
      ],
      munis: [
      ],
      parties: [
      ],
      civicCommittees: [
      ],
      isSubmitted: false,
      isError: false,
      errorHeader: 'error.invalidFields',
      errors: [],
      submitting: false
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
        formData.append("authLetter", this.form.authLetter);
        formData.append("solvencia", this.form.solvencia);
        HTTP.post(
          '/candidatos/presentar/', 
          formData, 
          {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
          }
        )
        .then(function (response) {
          alert("Información enviada correctamente. Por favor ingrese sus declaraciones de interés y patrimonial. \
                  \nAlguien del equipo se comunicará con usted para corroborar los datos.");
        })
        .catch(function (error) {
          alert("No se pudo enviar su información, por favor revise que sus datos esten completos en el formulario y que haya adjuntado dos archivos PDF");
        });
      }
    }
  },
  beforeMount() {
    this.getGenerics()
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
      authLetter: { required },
      solvencia: { required },
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
.instrucciones-block {
  text-align:justify;
  margin-top:20px;
}
.instrucciones-btn,{
  background:none;
  color: #333;
  border:none;
}
.instrucciones-body {
  padding-left: 30px;
  margin-top:35px;
}
</style>
