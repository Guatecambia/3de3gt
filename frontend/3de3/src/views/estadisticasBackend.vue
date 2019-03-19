<template>
  <div class="home">
    <AdminHeader />
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
          <div class="col-12">
            <b-row>
              <div class="col-7">
                <canvas id="executive-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #6ed3cf;" ></div>
                    <span class="final-numbers">Indigena</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.presidentIndigenous }}</span><br/>
                    <span>{{ Math.round((statistics.presidentIndigenous * 100)/(statistics.presidentIndigenous + statistics.presidentMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #9068be;" ></div>
                    <span class="final-numbers">Mestizo</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.presidentMixed }}</span><br/>
                    <span>{{ Math.round((statistics.presidentMixed * 100)/(statistics.presidentIndigenous + statistics.presidentMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #e62739;" ></div>
                    <span class="final-numbers">Otro</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.presidentOther }}</span><br/>
                    <span>{{ Math.round((statistics.presidentOther * 100)/(statistics.presidentIndigenous + statistics.presidentMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
      <b-collapse id="legislativeStatistics" accordion="statistics">
        <b-row>
          <div class="col-12">
            <b-row>
              <div class="col-7">
                <canvas id="legislative-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #6ed3cf;" ></div>
                    <span class="final-numbers">Indigena</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.congressIndigenous }}</span><br/>
                    <span>{{ Math.round((statistics.congressIndigenous * 100)/(statistics.congressIndigenous + statistics.congressMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #9068be;" ></div>
                    <span class="final-numbers">Mestizo</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.congressMixed }}</span><br/>
                    <span>{{ Math.round((statistics.congressMixed * 100)/(statistics.congressIndigenous + statistics.congressMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #e62739;" ></div>
                    <span class="final-numbers">Otro</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.congressOther }}</span><br/>
                    <span>{{ Math.round((statistics.congressOther * 100)/(statistics.congressIndigenous + statistics.congressMixed + statistics.presidentOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
      <b-collapse id="muniStatistics" accordion="statistics">
        <b-row>
          <div class="col-12">
            <b-row>
              <div class="col-7">
                <canvas id="munis-div" width=205 height=205></canvas>
              </div>
              <div class="col-5" style="margin-top:15px;">
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #6ed3cf;" ></div>
                    <span class="final-numbers">Indigena</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.muniIndigenous }}</span><br/>
                    <span>{{ Math.round((statistics.muniIndigenous * 100)/(statistics.muniIndigenous + statistics.muniMixed + statistics.muniOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #9068be;" ></div>
                    <span class="final-numbers">Mestizo</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.muniMixed }}</span><br/>
                    <span>{{ Math.round((statistics.muniMixed * 100)/(statistics.muniIndigenous + statistics.muniMixed + statistics.muniOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
                <b-row style="margin-top:10px;">
                  <div class="col-5">
                    <div class="color-box" style="background-color: #e62739;" ></div>
                    <span class="final-numbers">Otro</span>
                  </div>
                  <div class="col-4 final-numbers">
                    <span class="bold">{{ statistics.muniOther }}</span><br/>
                    <span>{{ Math.round((statistics.muniOther * 100)/(statistics.muniIndigenous + statistics.muniMixed + statistics.muniOther))||0 }}%</span>
                  </div>
                  <div class="col-3"></div>
                </b-row>
              </div>
            </b-row>
          </div>
        </b-row>
      </b-collapse>
      
      
    </b-container>
  </div>
</template>
<script>
import AdminHeader from '@/components/AdminHeader.vue'
import {HTTP} from '../../http-constants'
export default {
  name: 'estadisticasBackend',
  components: {
    AdminHeader,
  },
  data: function() {
    return {
      applicantPositions: {
        exActive: true,
        legActive: false,
        muniActive: false,
      },
      statistics: {
        presidentIndigenous: 0,
        presidentMixed: 0,
        presidentOther: 0,
        congressIndigenous: 0,
        congressMixed: 0,
        congressOther: 0,
        muniIndigenous: 0,
        muniMixed: 0,
        muniOther: 0,
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
    drawDonut: function(elementId,indigenous,mixed,other) {
      var canvas=document.getElementById(elementId);
      console.log(canvas);
      var ctx=canvas.getContext("2d");
      var colors=['#6ed3cf','#9068be','#e62739','gainsboro'];
      var values=[0,0,0,100];
      if ((indigenous + mixed + other)>0) {
        values=[
          ((indigenous*100)/(indigenous + mixed + other)*100),
          ((mixed*100)/(indigenous + mixed + other)*100),
          ((other*100)/(indigenous + mixed + other)*100),
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
      this.drawDonut("executive-div", this.statistics.presidentIndigenous, this.statistics.presidentMixed, this.statistics.presidentOther);
      this.drawDonut("legislative-div", this.statistics.congressIndigenous, this.statistics.congressMixed, this.statistics.congressOther);
      this.drawDonut("munis-div", this.statistics.muniIndigenous, this.statistics.muniMixed, this.statistics.muniOther);
      console.log("dibujado todo");
    },
    getStatistics: function() {
      HTTP.get('/3de3-admin/estadisticas/')
        .then(response => {
          this.statistics = response.data;
          this.draw();
        })
        .catch(e => {
          this.errors = e
        });
    }
  },
  mounted() {
    this.getStatistics();
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
.color-box {
    width: 30px;
    height: 30px;
    display: inline-block;
    background-color: #ccc;
    position: absolute;
    left: 5px;
    top: 5px;
}
</style>
