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
        {value: null, text: "Distrito"},
        {value: 24, text:  "Nacional"},
        {value: 23, text:  "Central"},
        {value: 1, text:  " El Progreso"},
        {value: 2, text:  "Baja Verapaz"},
        {value: 3, text:  "Zacapa"},
        {value: 4, text:  "Chiquimula"},
        {value: 5, text:  "Jalapa "},
        {value: 6, text:  "Retalhuleu"},
        {value: 7, text:  "Sacatepéquez"},
        {value: 8, text:  "Sololá "},
        {value: 9, text:  "Izabal"},
        {value: 10, text:  "Santa Rosa"},
        {value: 11, text:  "Petén "},
        {value: 12, text:  "Totonicapán"},
        {value: 13, text:  "chimaltenango"},
        {value: 14, text:  "Suchitepéquez"},
        {value: 15, text:  "Jutiapa"},
        {value: 16, text:  "Escuintla"},
        {value: 17, text:  "Quiché"},
        {value: 18, text:  "Alta Verapaz"},
        {value: 19, text:  "Quetzaltenango"},
        {value: 20, text:  "Huehuetenango"},
        {value: 21, text:  "San Marcos"},
        {value: 22, text:  "Guatemala"},
        {value: 25, text:  "Parlacen"},      ],
      munis: [
        {value: null, text: "Municipio"},
        {value: 1, text: "Cobán"},
        {value: 2, text: "Santa Cruz Verapaz"},
        {value: 3, text: "San Cristobal Verapaz"},
        {value: 4, text: "Tactíc"},
        {value: 5, text: "Tamahú"},
        {value: 6, text: "San Miguel Tucurú"},
        {value: 7, text: "Panzos"},
        {value: 8, text: "Senahú"},
        {value: 9, text: "San Pedro Carchá"},
        {value: 10, text: "San Juan Chamelco"},
        {value: 11, text: "Lanquín"},
        {value: 12, text: "Santa María Cahabón"},
        {value: 13, text: "Chisec"},
        {value: 14, text: "Chahal"},
        {value: 15, text: "Fray Bartolomé de las Casas"},
        {value: 16, text: "Santa Catarina la Tinta"},
        {value: 17, text: "Raxruhá"},
        {value: 18, text: "Salamá"},
        {value: 19, text: "San Miguel Chicaj"},
        {value: 20, text: "Rabinal"},
        {value: 21, text: "Cubulco"},
        {value: 22, text: "Granados"},
        {value: 23, text: "Santa Cruz El Chol"},
        {value: 24, text: "San Jerónimo"},
        {value: 25, text: "Purulhá"},
        {value: 26, text: "Chimaltenango"},
        {value: 27, text: "San José Poaquil"},
        {value: 28, text: "San Martín Jilotepeque"},
        {value: 29, text: "San Juan Comalapa"},
        {value: 30, text: "Santa Apolonia"},
        {value: 31, text: "Tecpán Guatemala"},
        {value: 32, text: "Patzun"},
        {value: 33, text: "San Miguel Pochuta"},
        {value: 34, text: "Patzicia"},
        {value: 35, text: "Santa Cruz Balanyá"},
        {value: 36, text: "Acatenango"},
        {value: 37, text: "San Pedro Yepocapa"},
        {value: 38, text: "San Andrés Itzapa"},
        {value: 39, text: "Parramos"},
        {value: 40, text: "Zaragoza"},
        {value: 41, text: "El Tejar"},
        {value: 42, text: "Chiquimula"},
        {value: 43, text: "San José La Arada"},
        {value: 44, text: "San Juan Ermita"},
        {value: 45, text: "Jocotán"},
        {value: 46, text: "Camotán"},
        {value: 47, text: "Olopa"},
        {value: 48, text: "Esquipulas"},
        {value: 49, text: "Concepción Las Minas"},
        {value: 50, text: "Quetzaltepeque"},
        {value: 51, text: "San Jacinto"},
        {value: 52, text: "Ipala"},
        {value: 53, text: "Flores"},
        {value: 54, text: "San José"},
        {value: 55, text: "San Benito"},
        {value: 56, text: "San Andrés "},
        {value: 57, text: "La Libertad"},
        {value: 58, text: "San Francisco"},
        {value: 59, text: "Santa Ana"},
        {value: 60, text: "Dolores"},
        {value: 61, text: "San Luis"},
        {value: 62, text: "Sayaxche"},
        {value: 63, text: "Melchor de Mencos"},
        {value: 64, text: "Poptún"},
        {value: 65, text: "Guastatoya"},
        {value: 66, text: "Morazán"},
        {value: 67, text: "San Agustín Acasaguastlan"},
        {value: 68, text: "San Cristóbal Acasaguastlan"},
        {value: 69, text: "El Jícaro"},
        {value: 70, text: "Sansare"},
        {value: 71, text: "Sanarate"},
        {value: 72, text: "San Antonio La Paz"},
        {value: 73, text: "Santa Cruz del Quiche"},
        {value: 74, text: "Chiche"},
        {value: 75, text: "Chinique"},
        {value: 76, text: "Zacualapa"},
        {value: 77, text: "Chajul"},
        {value: 78, text: "Santo Tomás Chichicastenango"},
        {value: 79, text: "Patzité"},
        {value: 80, text: "San Antonio Ilotenango"},
        {value: 81, text: "San Pedro Jocopilas"},
        {value: 82, text: "Cunén"},
        {value: 83, text: "San Juan Cotzal"},
        {value: 84, text: "Joyabaj"},
        {value: 85, text: "Santa María Nebaj"},
        {value: 86, text: "San Andrés Sajcabajá"},
        {value: 87, text: "San Miguel Uspantán"},
        {value: 88, text: "Sacapulas"},
        {value: 89, text: "San Bartolomé Jocotenango"},
        {value: 90, text: "Canilla"},
        {value: 91, text: "Chicaman"},
        {value: 92, text: "Ixcán"},
        {value: 93, text: "Pachalúm"},
        {value: 94, text: "Playa Grande"},
        {value: 95, text: "Escuintla"},
        {value: 96, text: "Santa Lucía Cotzumalguapa"},
        {value: 97, text: "La Democracia"},
        {value: 98, text: "Siquinalá"},
        {value: 99, text: "Masagua"},
        {value: 100, text: "Pueblo Nuevo Tiquisate"},
        {value: 101, text: "La Gomera"},
        {value: 102, text: "Guanagazapa"},
        {value: 103, text: "Puerto de San José"},
        {value: 104, text: "Iztapa"},
        {value: 105, text: "Palín"},
        {value: 106, text: "San Vicente Pacaya"},
        {value: 107, text: "Nueva Concepción"},
        {value: 108, text: "Guatemala"},
        {value: 109, text: "Santa Catarina Pinula"},
        {value: 110, text: "San José Pinula"},
        {value: 111, text: "San José del Golfo"},
        {value: 112, text: "Palencia"},
        {value: 113, text: "Chinautla"},
        {value: 114, text: "San Pedro Ayampuc"},
        {value: 115, text: "Mixco"},
        {value: 116, text: "San Pedro Sacatepequez "},
        {value: 117, text: "San Juan Sacatepequez"},
        {value: 118, text: "San Raymundo"},
        {value: 119, text: "Chuarrancho"},
        {value: 120, text: "Fraijanes"},
        {value: 121, text: "Amatitlán"},
        {value: 122, text: "Villa Nueva"},
        {value: 123, text: "Villa Canales"},
        {value: 124, text: "San Miguel Petapa"},
        {value: 125, text: "Huehuetenango "},
        {value: 126, text: "Chiantla"},
        {value: 127, text: "Malacatancito"},
        {value: 128, text: "Cuilco"},
        {value: 129, text: "Nentón"},
        {value: 130, text: "San Pedro Necta"},
        {value: 131, text: "Jacaltenango"},
        {value: 132, text: "San Pedro Soloma"},
        {value: 133, text: "San Ildefonso Ixtachuacan"},
        {value: 134, text: "Santa Bárbara"},
        {value: 135, text: "La Libertad"},
        {value: 136, text: "La Democracia"},
        {value: 137, text: "San Miguel Acatán"},
        {value: 138, text: "San Rafael La Independencia"},
        {value: 139, text: "Todos Santos Cuchumatán"},
        {value: 140, text: "San Juan Atitlán"},
        {value: 141, text: "Santa Eulalia"},
        {value: 142, text: "San Mateo Ixtatan"},
        {value: 143, text: "Colotenango"},
        {value: 144, text: "San Sebastián Huehuetenango"},
        {value: 145, text: "Tectitán"},
        {value: 146, text: "Concepción Huista"},
        {value: 147, text: "San Sebastián Coatán"},
        {value: 148, text: "Santa Cruz Barillas"},
        {value: 149, text: "Aguacatán"},
        {value: 150, text: "San Rafael Petzal"},
        {value: 151, text: "San Gaspar Ixchil"},
        {value: 152, text: "Santiago Chimaltenango"},
        {value: 153, text: "Santa Ana Huista"},
        {value: 154, text: "Unión Cantil"},
        {value: 155, text: "Puerto Barrios"},
        {value: 156, text: "Livingston"},
        {value: 157, text: "El Estor"},
        {value: 158, text: "Morales"},
        {value: 159, text: "Los Amates"},
        {value: 160, text: "Jalapa"},
        {value: 161, text: "San Pedro Pinula"},
        {value: 162, text: "San Luis Jilotepeque"},
        {value: 163, text: "San Manuel Chaparrón"},
        {value: 164, text: "San Carlos Alzatate"},
        {value: 165, text: "Monjas"},
        {value: 166, text: "Mataquescuintla"},
        {value: 167, text: "Jutiapa"},
        {value: 168, text: "El Progreso"},
        {value: 169, text: "Santa Catarina Mita"},
        {value: 170, text: "Agua Blanca"},
        {value: 171, text: "Asunción Mita"},
        {value: 172, text: "Yupiltepeque"},
        {value: 173, text: "Atescatempa"},
        {value: 174, text: "Jerez"},
        {value: 175, text: "El Adelanto"},
        {value: 176, text: "Zapotitlán"},
        {value: 177, text: "Comapa"},
        {value: 178, text: "Jalpatagua"},
        {value: 179, text: "Conguaco"},
        {value: 180, text: "Moyuta"},
        {value: 181, text: "Pasaco"},
        {value: 182, text: "San José Acatempa"},
        {value: 183, text: "Quezada"},
        {value: 184, text: "Quetzaltenango "},
        {value: 185, text: "Salcajá"},
        {value: 186, text: "Olintepeque"},
        {value: 187, text: "San Carlos Sija"},
        {value: 188, text: "Sibilia"},
        {value: 189, text: "Cabrican"},
        {value: 190, text: "Cajola"},
        {value: 191, text: "San Miguel Siguila"},
        {value: 192, text: "San Juan Ostuncalco"},
        {value: 193, text: "San Mateo"},
        {value: 194, text: "Concepción Chiquirichapa"},
        {value: 195, text: "San Martín Sacatepequez"},
        {value: 196, text: "Almolonga"},
        {value: 197, text: "Cantel"},
        {value: 198, text: "Huitán"},
        {value: 199, text: "Zunil"},
        {value: 200, text: "Colomba Costa Cuca"},
        {value: 201, text: "San Francisco La Unión"},
        {value: 202, text: "El Palmar"},
        {value: 203, text: "Coatepeque"},
        {value: 204, text: "Génova Costa Cuca"},
        {value: 205, text: "Flores Costa Cuca"},
        {value: 206, text: "La Esperanza "},
        {value: 207, text: "Palestina de los Altos"},
        {value: 208, text: "Retalhuleu"},
        {value: 209, text: "San Sebastián"},
        {value: 210, text: "Santa Cruz Mulúa"},
        {value: 211, text: "San Martín Zapotitlán"},
        {value: 212, text: "San Felipe "},
        {value: 213, text: "San Andrés Villa Seca"},
        {value: 214, text: "Champerico"},
        {value: 215, text: "Nuevo San Carlos"},
        {value: 216, text: "El Asintal"},
        {value: 217, text: "Antigua Guatemala"},
        {value: 218, text: "Jocotenango"},
        {value: 219, text: "Pastores"},
        {value: 220, text: "Sumpango"},
        {value: 221, text: "Santo Domingo Xenacoj"},
        {value: 222, text: "Santiago Sacatepequez"},
        {value: 223, text: "San Bartolomé Milpas Altas"},
        {value: 224, text: "San Lucas Sacatepequez"},
        {value: 225, text: "Santa Lucía Milpas Altas"},
        {value: 226, text: "Magdalena Milpas Altas"},
        {value: 227, text: "Santa María de Jesús"},
        {value: 228, text: "Ciudad Vieja"},
        {value: 229, text: "San Miguel Dueñas"},
        {value: 230, text: "Alotenango"},
        {value: 231, text: "San Antonio Aguas Calientes"},
        {value: 232, text: "Santa Catarina Barahona"},
        {value: 233, text: "San Marcos"},
        {value: 234, text: "San Pedro Sacatepéquez"},
        {value: 235, text: "Comitancillo"},
        {value: 236, text: "San Antonio Sacatepéquez"},
        {value: 237, text: "San Miguel Ixtahuacan"},
        {value: 238, text: "Concepción Tutuapa"},
        {value: 239, text: "Tacaná"},
        {value: 240, text: "Sibinal"},
        {value: 241, text: "Tajumulco"},
        {value: 242, text: "Tejutla"},
        {value: 243, text: "San Rafael Pié de la Cuesta"},
        {value: 244, text: "Nuevo Progreso "},
        {value: 245, text: "El tumbador"},
        {value: 246, text: "San José El Rodeo"},
        {value: 247, text: "Malacatán"},
        {value: 248, text: "Catarina"},
        {value: 249, text: "Ayutla"},
        {value: 250, text: "Ocos "},
        {value: 251, text: "San Pablo "},
        {value: 252, text: "El Quetzal"},
        {value: 253, text: "La Reforma"},
        {value: 254, text: "Pajapita"},
        {value: 255, text: "Ixchiguan"},
        {value: 256, text: "San José Ojetenán"},
        {value: 257, text: "San CRistóbal Cucho"},
        {value: 258, text: "Sipacapa"},
        {value: 259, text: "Esquipulas Palo Gordo"},
        {value: 260, text: "Río Blanco"},
        {value: 261, text: "San Lorenzo"},
        {value: 262, text: "Cuilapa"},
        {value: 263, text: "Barberena"},
        {value: 264, text: "San Rosa de Lima"},
        {value: 265, text: "Casillas"},
        {value: 266, text: "San Rafael Las Flores"},
        {value: 267, text: "Oratorio"},
        {value: 268, text: "San Juan Tecuaco"},
        {value: 269, text: "Chiquimulilla"},
        {value: 270, text: "Taxisco"},
        {value: 271, text: "Santa María Ixhuatan"},
        {value: 272, text: "Guazacapán"},
        {value: 273, text: "Santa Cruz Naranjo"},
        {value: 274, text: "Pueblo Nuevo Viñas"},
        {value: 275, text: "Nueva Santa Rosa"},
        {value: 276, text: "Sololá"},
        {value: 277, text: "San José Chacaya"},
        {value: 278, text: "Santa María Visitación "},
        {value: 279, text: "Santa Lucía Utatlán"},
        {value: 280, text: "Nahualá"},
        {value: 281, text: "Santa Catarina Ixtahuacán"},
        {value: 282, text: "Santa Clara La Laguna"},
        {value: 283, text: "Concepción"},
        {value: 284, text: "San Andrés Semetabaj"},
        {value: 285, text: "Panajachel"},
        {value: 286, text: "Santa Catarina Palopó"},
        {value: 287, text: "San Antonio Palopó"},
        {value: 288, text: "San Lucas Tolimán"},
        {value: 289, text: "Santa Cruz La Laguna"},
        {value: 290, text: "San Pablo La Laguna"},
        {value: 291, text: "San Marcos La Laguna"},
        {value: 292, text: "San Pedro La Laguna"},
        {value: 293, text: "San Juan La  Laguna"},
        {value: 294, text: "Santiago Atitlán"},
        {value: 295, text: "Mazatenango"},
        {value: 296, text: "Cuyotenango"},
        {value: 297, text: "San Francisco Zapotitlán "},
        {value: 298, text: "San Bernardino"},
        {value: 299, text: "San José El Ídolo"},
        {value: 300, text: "Santo Domingo Suchitepequez"},
        {value: 301, text: "San Lorenzo"},
        {value: 302, text: "Samayac"},
        {value: 303, text: "San Pablo Jocopilas"},
        {value: 304, text: "San Antonio Suchitepéquez"},
        {value: 305, text: "San Miguel Panám"},
        {value: 306, text: "San Gabriel"},
        {value: 307, text: "Chicacao"},
        {value: 308, text: "Patulul"},
        {value: 309, text: "Santa Bárbara"},
        {value: 310, text: "San Juan Bautista"},
        {value: 311, text: "Santo Tomás La Unión"},
        {value: 312, text: "Zunilito"},
        {value: 313, text: "Pueblo Nuevo Suchitepequez"},
        {value: 314, text: "Río Bravo"},
        {value: 315, text: "Totonicapán"},
        {value: 316, text: "San Cristóbal Totonicapán"},
        {value: 317, text: "San Francisco El Alto"},
        {value: 318, text: "San Andrés Xecul"},
        {value: 319, text: "Momostenango"},
        {value: 320, text: "Santa María Chiquimula"},
        {value: 321, text: "Santa Lucía La Reforma"},
        {value: 322, text: "San Bartolo Aguas Calientes"},
        {value: 323, text: "Zacapa"},
        {value: 324, text: "Estanzuela"},
        {value: 325, text: "Río Hondo"},
        {value: 326, text: "Gualán"},
        {value: 327, text: "Teculután"},
        {value: 328, text: "Usumatlán"},
        {value: 329, text: "Cabañas"},
        {value: 330, text: "San  Diego"},
        {value: 331, text: "La Unión "},
        {value: 332, text: "Huite"},


      ],
      parties: [
        {value: null, text: "Seleccione partido"},
        {value: 1, text:  "Unidad Nacional de la Esperanza"},
        {value: 2, text:  "Partido de Avanzada Nacional"},
        {value: 3, text:  "VAMOS"},
        {value: 4, text:  "Unión del Cambio Nacional"},
        {value: 5, text:  "TODOS"},
        {value: 6, text:  "Encuentro por Guatemala"},
        {value: 7, text:  "VALOR"},
        {value: 8, text:  "Compromiso, Renovación y Orden"},
        {value: 9, text:  "Frente de Convergencia Nacional"},
        {value: 10, text:  "Visión con Valores"},
        {value: 11, text:  "FUERZA"},
        {value: 12, text:  "AVANZA"},
        {value: 13, text:  "Unidad Revolucionaria Nacional Guatemalteca"},
        {value: 14, text:  "Partido Productivdad y de Trabajo"},
        {value: 15, text:  "Movimiento Reformador"},
        {value: 16, text:  "Partido Liberal Guatemalteco"},
        {value: 17, text:  "Partido Humanista de Guatemala"},
        {value: 18, text:  "Partido Unionista"},
        {value: 19, text:  "Victoría"},
        {value: 20, text:  "Movimiento Político"},
        {value: 21, text:  "Partido Político Unidos"},
        {value: 22, text:  "Convergencia"},
        {value: 23, text:  "Bienestar Nacional"},
        {value: 24, text:  "Movimiento para la Liberación de los Pueblos"},
        {value: 25, text:  "Movimiento Semilla"},
        {value: 26, text:  "Libre"},
        {value: 27, text:  "Prosperidad Ciudadana"},      ],
      civicCommittees: [
        {value: null, text: "Seleccione comité civico"},
        {value: 28, text: "Nueva Ciudadanía"},
        {value: 29, text: "Partido REvolucionario Organizada"},
        {value: 30, text: "Rescate Nacional de Ciudades"},
        {value: 31, text: "Paz, Acción, Soberanía"},      ],
      isSubmitted: false,
      isError: false,
      errorHeader: 'error.invalidFields',
      errors: [],
      submitting: false
    }
  },
  methods: {
    soonMessage: function() {
      alert('Gracias por tu interés, prónto estaremos publicando los formularios para que puedas llenarlos.');
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
