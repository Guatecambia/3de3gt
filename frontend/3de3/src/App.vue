<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
export default {
  components: {
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Heebo:400,900');

html, body {
  font-family: 'Heebo', sans-serif;
}

body {
  font-family: 'Heebo', sans-serif;
}

#app {
  font-family: 'Heebo', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.section {
  margin-top: 35px;
}

hr.line {
  border-top: 1px solid;
  border-color: #000;
}
h1{
  font-size:4em;
  text-align:left !important;
}
h2 {
  font-size: 2em;
}
h2,h1 {
  text-align:center;
  text-transform:uppercase;
  font-weight: bolder;
}
.pink-font {
  color: #EF2466;
}
.blue-font{
  color: #0096DB;
}
.green-font {
  color: #60bd55;
}
@media (max-width: 768px) {
  h2 {
    font-size: 1.4em;
  }
}
</style>
