<template>
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
</template>
<script>
export default {
  name: 'Applicant',
  data() {
    return {
      interrogation: [
        {
          question: "¿Qué es una declaración patrimonial y por qué consideramos que es importante hacerla pública?",
          answer: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS."
        },
        {
          question: "¿Qué es una declaración patrimonial y por qué consideramos que es importante hacerla pública?",
          answer: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS."
        }
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
