<template>
  <div id="app">
    <nav>
      <ul>
        <li>
          <router-link to='/'>Home</router-link>
        </li>
        <li>
          <router-link to='/soap'>Soap</router-link>
        </li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    //HelloWorld
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
