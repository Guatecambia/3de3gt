<template>
  <div class="home">
    <Header />
    <b-container class="privacy">
      <b-row>
        <div class="col-12">
          <h1>Privacidad</h1>
        </div>
      </b-row>
      <b-row>
        <div class="col-3"></div>
        <div class="col-9">
          <p>Siendo responsables con los datos personales que a través de esta plataforma electrónica se publicarán y comprometidos con la transparencia y rendición de cuentas, ponemos a su disposición el siguiente aviso de privacidad.</p>
          <p class="bold">I. Responsable</p>
          <p>La Iniciativa 3de3 Guatemala es impulsada por Acción Ciudadana, capítulo guatemalteco de Transparencia Internacional. Dirección: Avenida Reforma 12-01, Edificio Reforma Montufar, nivel 17, oficina 17-01. Teléfono: (502) 2388-3400. Sitio web: <a href="http://accionciudadana.org.gt/" target="_blank">http://accionciudadana.org.gt/</a>. </p>
          <ul>
            <li>Acción Ciudadana no asume compromisos ni responsabilidad alguna respecto a la veracidad o actualidad de la información presentada en la plataforma web, por el titular y para la cual se ha otorgado el consentimiento correspondiente para su publicación, reservándose el derecho de impedir el acceso de los usuarios o titulares que violenten el aviso de privacidad.</li>
            <li>No asume ninguna responsabilidad sobre el uso que los usuarios puedan darle a la publicación de la información contenida en las declaraciones.</li>
            <li>No se responsabiliza del contenido de los reportes o quejas que se publiquen en la plataforma. La veracidad de las mismas será responsabilidad del usuario o titular que las escribió. </li>
            <li>Acción Ciudadana se reserva el derecho de dar de baja toda la información que no cumpla con los requisitos solicitados en los formatos de las declaraciones. </li>
          </ul>
          <p class="bold">II. Definiciones</p>
          <p>Para efectos del presente aviso de privacidad se definirá como:</p>
          <ul>
            <li>Usuario: toda persona física que utilice la plataforma digital 3de3.gt, quien podrá acceder las veces que considere necesario. Al hacer uso de esta plataforma, el usuario acepta absolutamente el presente aviso de privacidad vigente al momento que se realice la visita.</li>
            <li>Titular: toda persona física que ostente a un cargo de elección popular, que proporcione información descrita en las declaraciones, otorgando expresamente su consentimiento para que sus datos puedan ser publicados en esta plataforma. Al hacer uso de esta, el titular acepta absolutamente el contenido del presente aviso de privacidad vigente al momento que se utilice.</li>
            <li>Información: son todos aquellos datos descritos en los documentos denominados como Declaración Patrimonial, Declaración fiscal y Declaración de Interés.</li>
          </ul>
          <p class="bold">III. Términos de uso de la plataforma 3de3.gt</p>
          <ul>
            <li>La publicación de las tres declaraciones, Patrimonial, de Interés y Fiscal, se hará únicamente con el consentimiento expreso a través de de la carta de consentimiento firmada por el titular, indicando su deseo de formar parte de la iniciativa 3de3 Guatemala.</li>
            <li>La publicación de las declaraciones se realiza con el único fin de que los ciudadanos puedan acceder de manera fácil y rápida a la información personal, patrimonial, fiscal, bancaria, financiera, intereses económicos, actividades empresariales privadas y con instituciones del Estado, información sobre su cónyuge o conviviente de hecho, hijos dependientes a fin de promover candidatos dispuestos a dar muestras de transparencia y rendición de cuentas. </li>
            <li>Acción Ciudadana y la iniciativa 3de3 Guatemala no asume compromiso respecto a la exactitud, la veracidad, la exhaustividad o la actualidad de la información presentada en la plataforma. La información es proporcionada por el titular y para lo cual se ha otorgado el consentimiento correspondiente para su publicación, tratamiento y uso descrito en el presente aviso de privacidad. </li>
            <li>La plataforma contendrá un perfil personal de cada candidato que decida de forma voluntaria ser parte de la iniciativa, el cual contendrá la siguiente información:</li>
            <ul>
              <li>Vista pública de las tres declaraciones contempladas en la iniciativa: Patrimonial, de Intereses, Fiscal. </li>
              <li>Información del candidato o candidata: Cargo de elección popular al que aspira y partido político o comité cívico por el que participa. </li>
              <li>Vinculación con los perfiles personales de Facebook y Tweeter de los candidatos. </li>
            </ul>
          </ul>
          <p class="bold">IV. Uso de la información</p>
          <p>El uso que se le dará a la información proporcionada por el titular a la plataforma electrónica 3de3 Guatemala se orienta a la recopilación y difusión del contenido de las declaraciones patrimonial, fiscal y de interés, con la finalidad de promover confianza en la ciudadanía en sus candidatos, a través de prácticas de transparencia y rendición de cuentas. </p>
          <ul>
            <li>La publicación de la información contenida en las declaraciones contempladas en la iniciativa, incentiva a la ciudadanía a informarse y participar activamente en el proceso electoral 2019.</li>
            <li>Los candidatos hacen públicas sus declaraciones con el objetivo de mostrar a sus electores, su disposición a ser transparentes y rendir cuentas. </li>
          </ul>
          <p class="bold">V. Cookies</p>
          <p>Utilizamos cookies para personalizar contenido y anuncios, proporcionar funciones de redes sociales y analizar nuestro tráfico. También compartimos información sobre cómo usted utiliza nuestro sitio con nuestros socios de analitica. </p>
          <p class="bold">VI. Cambios en el Aviso de Privacidad</p>
          <p>Es posible que se realicen modificaciones al presente aviso de privacidad por lo que se recomienda que lo revise periódicamente por si existiera algún cambio. La última actualización del presente se realizó en febrero del 20</p>
        </div>
      </b-row>
    </b-container>
    <Footer />
  </div>
</template>
<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
export default {
  name: 'about',
  components: {
    Header,
    Footer
  }
}
</script>
<style scoped>
p, li {
  text-align: justify;
}
h1 {
  text-align:left;
}
.bold {
  font-weight: bold;
}
</style>
