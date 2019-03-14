<template>
  <div class="home">
    <Header />
    <b-container class="privacy">
      <b-row>
        <div class="col-12">
          <h2><span class="pink-font">E</span>stadisticas</h2>
        </div>
      </b-row>
    </b-container>
    <div class="applicant-menu">
      <b-container>
        <b-row>
          <div class="col-12">
            <ul class="nav nav-fill">
              <li class="nav-item" v-bind:class="{ active: applicantPositions.exActive }">
                <a class="nav-link" href="#" v-b-toggle.executiveStatistics v-on:click.prevent="activateMenu('EX')">Ejecutivo</a>
              </li>
              <li class="nav-item"  v-bind:class="{ active: applicantPositions.legActive }">
                <a class="nav-link" href="#" v-b-toggle.legislativeStatistics v-on:click.prevent="activateMenu('LEG')"">Legislativo</a>
              </li>
              <li class="nav-item" v-bind:class="{ active: applicantPositions.muniActive }">
                <a class="nav-link" href="#" v-b-toggle.muniStatistics v-on:click.prevent="activateMenu('M')"">Municipal</a>
              </li>
            </ul>
          </div>
        </b-row>
      </b-container>
    </div>
    <b-container id="statistics">
    
    
      <b-collapse id="executiveStatistics" accordion="statistics">
        <b-row>
          <div class="col-12 col-md-6">
            <b-row>
              <div class="col-12" style="margin-bottom:20px;">
                <span class="bold final-numbers">Presidenciables</span>
              </div>
              <div class="col-7">
                <canvas id="president-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/female.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.femalePresident }}</span><br/>
                    <span>{{ Math.round((statistics.femalePresident * 100)/(statistics.femalePresident + statistics.malePresident))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/male.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.malePresident }}</span><br/>
                    <span>{{ Math.round((statistics.malePresident * 100)/(statistics.femalePresident + statistics.malePresident))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
              </div>
            </b-row>
          </div>
          <div class="col-12 col-md-6">
            <b-row>
              <div class="col-12" style="margin-bottom:20px;">
                <span class="bold final-numbers">Vicepresidenciables</span>
              </div>
              <div class="col-7">
                <canvas id="vicepresident-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/female.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.femaleVicepresident }}</span><br/>
                    <span>{{ Math.round((statistics.femaleVicepresident * 100)/(statistics.femaleVicepresident + statistics.maleVicepresident))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/male.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.maleVicepresident }}</span><br/>
                    <span>{{ Math.round((statistics.maleVicepresident * 100)/(statistics.femaleVicepresident + statistics.maleVicepresident))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
      <b-collapse id="legislativeStatistics" accordion="statistics">
        <b-row>
          <div class="col-12" style="margin-bottom:20px;">
            <span class="bold final-numbers">Declarantes por el listado en el que participan</span>
          </div>
          <div class="col-12">
            <b-row>
              <div class="col-md-1 col-2"></div>
              <div class="col-md-4 col-8">
                <div class="lNac final-numbers">
                  <span class="lTitle">Listado Nacional</span>
                  {{ statistics.congressNac }}
                </div>
              </div>
              <div class="col-md-1 col-2"></div>
              <div class="col-md-1 col-2"></div>
              <div class="col-md-4 col-8">
                <div class="lDistr final-numbers">
                  <span class="lTitle">Listado Distrital</span>
                  <span class="lNum">{{ statistics.congressDistr }}</span>
                </div>
              </div>
              <div class="col-md-1 col-2"></div>
            </b-row>
          </div>
          <div class="col-12 col-md-6">
            <b-row>
              <div class="col-12" style="margin-bottom:20px;">
                <span class="bold final-numbers">Listado Nacional</span>
              </div>
              <div class="col-7">
                <canvas id="congressNac-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/female.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.femaleCongressNac }}</span><br/>
                    <span>{{ Math.round((statistics.femaleCongressNac * 100)/(statistics.femaleCongressNac + statistics.maleCongressNac))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/male.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.maleCongressNac }}</span><br/>
                    <span>{{ Math.round((statistics.maleCongressNac * 100)/(statistics.femaleCongressNac + statistics.maleCongressNac))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
              </div>
            </b-row>
          </div>
          <div class="col-12 col-md-6">
            <b-row>
              <div class="col-12" style="margin-bottom:20px;">
                <span class="bold final-numbers">Listado Distrital</span>
              </div>
              <div class="col-7">
                <canvas id="congressDistr-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/female.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.femaleCongressDistr }}</span><br/>
                    <span>{{ Math.round((statistics.femaleCongressDistr * 100)/(statistics.femaleCongressDistr + statistics.maleCongressDistr))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/male.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.maleCongressDistr }}</span><br/>
                    <span>{{ Math.round((statistics.maleCongressDistr * 100)/(statistics.femaleCongressDistr + statistics.maleCongressDistr))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
      <b-collapse id="muniStatistics" accordion="statistics">
        <b-row>
          <div class="col-12" style="margin-bottom:20px;">
            <span class="bold final-numbers">Declarantes por género</span>
          </div>
          <div class="col-12">
            <b-row>
              <div class="col-7">
                <canvas id="muni-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/female.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.femaleMuni }}</span><br/>
                    <span>{{ Math.round((statistics.femaleMuni * 100)/(statistics.femaleMuni + statistics.maleMuni))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-4">
                    <img src="../assets/male.jpg" />
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.maleMuni }}</span><br/>
                    <span>{{ Math.round((statistics.maleMuni * 100)/(statistics.femaleMuni + statistics.maleMuni))||0 }}%</span>
                  </div>
                  <div class="col-4"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
    </b-container>
    <Footer />
  </div>
</template>
<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import {HTTP} from '../../http-constants'
export default {
  name: 'estadisticas',
  components: {
    Header,
    Footer
  },
  data: function() {
    return {
      applicantPositions: {
        exActive: true,
        legActive: false,
        muniActive: false,
      },
      statistics: {
        malePresident: 0,
        femalePresident: 0,
        maleVicepresident: 0,
        femaleVicepresident: 0,
        congressNac: 0,
        congressDistr: 0,
        maleCongressNac: 0,
        femaleCongressNac: 0,
        maleCongressDistr: 0,
        femaleCongressDistr: 0,
        maleMuni: 0,
        femaleMuni: 0,
      },
    }
  },
  methods: {
    activateMenu: function(menu) {
      if ((menu == 'EX') && (this.applicantPositions.exActive))
        this.$root.$emit('bv::toggle::collapse', 'executiveStatistics')
      else if ((menu == 'LEG') && (this.applicantPositions.legActive))
        this.$root.$emit('bv::toggle::collapse', 'legislativeStatistics')
      else if ((menu == 'M') && (this.applicantPositions.muniActive))
        this.$root.$emit('bv::toggle::collapse', 'muniStatistics')
        
        
      this.applicantPositions.exActive = (menu == 'EX') ? true : false;
      this.applicantPositions.legActive = (menu == 'LEG') ? true : false;
      this.applicantPositions.muniActive = (menu == 'M') ? true : false;
      if (!(this.applicantPositions.exActive || this.applicantPositions.legActive || this.applicantPositions.muniActive)) {
        this.applicantPositions.exActive = true;
        menu = 'EX';
      }
    },
    drawDonut: function(elementId,maleValue,femaleValue) {
      var canvas=document.getElementById(elementId);
      var ctx=canvas.getContext("2d");
      var colors=['#333','#EF2466','gainsboro'];
      var values=[0,0,100];
      if ((maleValue + femaleValue)>0) {
        values=[
          ((maleValue*100)/(maleValue + femaleValue)*100),
          ((femaleValue*100)/(maleValue + femaleValue)*100),
          0
        ];
      }
      var cx=100;
      var cy=100;
      var radius=75;
      var arcwidth=45;
      var tot=0;
      var accum=0;
      var PI=Math.PI;
      var PI2=PI*2;
      var offset=-PI/2;
      ctx.lineWidth=arcwidth;
      for(var i=0;i<values.length;i++){tot+=values[i];}
      for(var i=0;i<values.length;i++){
          ctx.beginPath();
          ctx.arc(cx,cy,radius,
              offset+PI2*(accum/tot),
              offset+PI2*((accum+values[i])/tot)
          );
          ctx.strokeStyle=colors[i];
          ctx.stroke();
          accum+=values[i];
      }
    },
    draw: function() {
      this.drawDonut("president-div", this.statistics.malePresident, this.statistics.femalePresident);
      this.drawDonut("vicepresident-div", this.statistics.maleVicepresident, this.statistics.femaleVicepresident);
      this.drawDonut("congressNac-div", this.statistics.maleCongressNac, this.statistics.femaleCongressNac);
      this.drawDonut("congressDistr-div", this.statistics.maleCongressDistr, this.statistics.femaleCongressDistr);
      this.drawDonut("muni-div", this.statistics.maleMuni, this.statistics.femaleMuni);
    },
    getStatistics: function() {
      HTTP.get('/generico/estadisticas/')
        .then(response => {
          this.statistics = response.data;
          this.draw();
        })
        .catch(e => {
          this.errors = e
        });
    }
  },
  beforeMount() {
    this.getStatistics();
  },
  mounted() {
    this.$root.$emit('bv::toggle::collapse', 'executiveStatistics')
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
.final-numbers {
  font-size:1.7em;
}
.applicant-menu {
  background:#333;
  margin-top:50px;
}
a.nav-link {
  height: 4em;
  margin-top: 1em;
  color: #fff;
  font-weight: bold;
}
li.nav-item {
  background: #333;
  color: #FFF;
  border-right:none;
}
li.nav-item:hover, li.nav-item.active {
  background: #fff;
  color: #EF2466;
}
li.nav-item:hover a, li.nav-item.active a{
  color: #EF2466;
}
#statistics {
  margin-top:100px;
  margin-bottom: 100px;
}
.lNac {
  border: 1px solid #EF2466;
  margin: 15px 0;
  color: #EF2466;
  font-weight: bolder;
  font-size: 3em;
}
.lDistr {
  margin: 15px 0;
  border: 1px solid #0096DB;
  color: #0096DB;
  font-weight: bolder;
  font-size: 3em;
}
.lTitle {
  margin-top:10px;
  font-size: 15px;
  color: #333;
  font-weight: bold;
  display: block;
}
.lNum {
  font-size: 1em;
}
</style>
