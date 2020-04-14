<template>
<!--:suggestions="[{data:['Frodo', 'Samwise', 'Gandalf', 'Galadriel', 'Faramir', 'Éowyn']}]"-->
  <div >
    <suggestions
    v-model="query"
    :options="options"
    :onInputChange="onCountryInputChange"></suggestions>

</div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import Suggestions from 'v-suggestions'
import 'v-suggestions/dist/v-suggestions.css' // you can import the stylesheets also (optional)

Vue.component('suggestions', Suggestions)

var temp = []

export default {
  name: 'HelloWorld',
  created() {
  axios.get('https://ressources.data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&rows=3270&sort=gare_alias_libelle_noncontraint&facet=gare_agencegc_libelle&facet=gare_regionsncf_libelle&facet=gare_ug_libelle&facet=pltf_departement_libellemin&facet=pltf_segmentdrg_libelle')
    .then(function (response) {
      // fields.gare_alias_libelle_noncontraint
      //console.log(response.data.records)
      var i = null
      for (i = 0; i < 3270; i++) {
        temp[i] = response.data.records[i].fields.gare_alias_libelle_noncontraint
        //console.log(temp[i])
      } 
    })
  },
  data () {
    let countries=temp
    //let countries = ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'AndorrA', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize']
    return {
      query: '',
      countries: countries,
      selectedCountry: null,
      options: {}
    }
  },
  methods: {
    onCountryInputChange (query) {
      if (query.trim().length === 0) {
        return null
      }
      // return the matching countries as an array
      return this.countries.filter((country) => {
        return country.toLowerCase().includes(query.toLowerCase())
      })
    },
    onCountrySelected (item) {
      this.selectedCountry = item
    },
    onSearchItemSelected (item) {
      this.selectedSearchItem = item
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>