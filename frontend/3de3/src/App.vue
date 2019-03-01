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
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

li.nav-item {
  padding: 5px 25px;
  background: #EF2466;
  color: #FFF;
}

li.nav-item a {
  color: #FFF;
}

li.nav-item a:hover {
  color: #0096DB;
}

.page-navbar{
  padding-top:10px;
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
.nav-item {
  border-right:1px solid #fff;
}
</style>
