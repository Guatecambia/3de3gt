<template>
  <div class="home">
    <Header />
    <b-container class="faq">
      <b-row>
        <div class="col-12">
          <h1>Pr<span class="pink-font">e</span>guntas Fr<span class="blue-font">e</span>cu<span class="green-font">e</span>nt<span class="pink-font">e</span>s</h1>
        </div>
      </b-row>
      <b-row>
        <div v-for="(question, index) in interrogation" class="col-12">
          <div class="faq-question">
            <b-button class="question-btn" v-b-toggle="'quest'+index">
              {{ question.question }}
            </b-button>
            <b-collapse :id="'quest'+index" class="question-body">
              {{ question.answer }}
            </b-collapse>
          </div>
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
  name: 'Applicant',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      interrogation: [
        {
          question: "¿Qué es 3de3?",
          answer: "Es una iniciativa ciudadana que busca fortalecer el vínculo entre la ciudadanía y los políticos a través de la implementación de prácticas de transparencia y rendición de cuentas. En la plataforma electrónica www.3de3.gt los candidatos y candidatas a cargos públicos harán públicas sus declaraciones de: intereses, patrimonial y fiscal."
        },
        {
          question: "¿Quién promueve 3de3?",
          answer: "Todas y todos los ciudadanos comprometidos con la democracia. Tú y yo somos los protagonistas de esta iniciativa."
        },
        {
          question: "¿Qué candidatos deben presentar su 3de3?",
          answer: "Todos los candidatos a un puesto de elección popular, como por ejemplo, los binomios presidenciales, diputados, alcaldes y diputados al PARLACEN."
        },
        {
          question: "¿Para qué sirve que los candidatos presenten su 3de3?",
          answer: "Para que los ciudadanos recuperemos la confianza en los candidatos y que a través de un acción concreta, den muestra de su compromiso con la construcción de una democracia firme, bajo principios de honestidad y transparencia."
        },
        {
          question: " ¿Por qué debo solicitar a los candidatos que se comprometan con la transparencia y rendición de cuentas?",
          answer: "Porque como ciudadanos tenemos derecho a conocer a nuestros candidatos."
        },
        {
          question: "¿Cómo puedo pedir a mi candidato que presente su 3de3?",
          answer: "Desde la plataforma www.3de3.gt puedes enviar un post o tuit directamente a las redes sociales del candidato. Comparte y divulga la información de nuestras plataformas en redes sociales y usa los hashtag #3de3guate #candidato3de3 #exijo3de3 ¡Juntos podemos lograr grandes cambios!"
        },
        {
          question: "¿Por qué es importante un gobierno transparente?",
          answer: "En una democracia sana, los candidatos electos deben representar los intereses de toda la población y velar por el bien común, para garantizar el desarrollo pleno en igualdad de condiciones y oportunidades para todos."
        },
      ]
    }
  }
}
</script>
<style scoped>
p {
  text-align: justify;
}
h1 {
  text-align:center;
}
.faq-question {
  text-align:justify;
  margin-top:20px;
}
.question-btn, .btn, .btn-secondary, .btn:hover, .btn-secondary:hover {
  background:none;
  color: #333;
  border:none;
}
.question-btn:focus, .question-btn:active, .btn-secondary:focus, .btn-secondary:active {
   outline: none !important;
   box-shadow: none;
}
.question-body {
  padding-left: 30px;
}
</style>
