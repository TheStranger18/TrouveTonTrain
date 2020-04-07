<template>
  <div id="app">
    <h1>Bonjour l'application !</h1>
    <p>
      <!-- utilisez le composant router-link pour la navigation. -->
      <!-- spécifiez le lien en le passant à la prop `to` -->
      <!-- `<router-link>` sera rendu en tag `<a>` par défaut -->
      <router-link to="/">Aller à l'acceuil</router-link>
      <router-link to="/soap">Aller à Soap</router-link>
    </p>
    <!-- balise pour le composant router-view -->
    <!-- le composant correspondant à la route sera rendu ici -->
    <router-view></router-view>
  </div>
  <!--<div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>-->
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
