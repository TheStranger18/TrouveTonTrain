<template>
  <div >
    <h3>Departure :</h3>
    <suggestions
    v-model="departure"
    :options="options"
    :onInputChange="onDepartureInputChange"
    :onItemSelected="onDepartureSelected"></suggestions>

  <br>
  <br>

  <h3>Arrival :</h3>
    <suggestions
    v-model="arrival"
    :options="options"
    :onInputChange="onArrivalInputChange"
    :onItemSelected="onArrivalSelected"></suggestions>

    <p v-if="ifDistance">La distance est de <span id="sum"></span> km.<br>
      Le prix de ce trajet est le suivant <span id="price"> €.</span>  
    </p>
</div>

</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import Suggestions from 'v-suggestions'
import 'v-suggestions/dist/v-suggestions.css' // you can import the stylesheets also (optional)

Vue.component('suggestions', Suggestions)

//var url = 'http://localhost:5000'
var url = 'https://tttserver.ew.r.appspot.com'
var temp = [] // name of all cities that we receive from the sncf api
var allInfomations = [] // all infomationsthat we receive from the sncf api
var indexDeparture = 0
var indexArrival = 0
//var coorDeparture = new Map()
//var coorArrival = new Map()
var latitudeD = 0
var longitudeD = 0
var latitudeA = 0
var longitudeA = 0
var distance = null
var price = null

// this function permit us to know the index for the cities
function findCity(departure, arrival){
  for(var i = 0; i<3270; i++){
    if(departure===temp[i]){
      indexDeparture = i
    }
    if(arrival===temp[i]){
      indexArrival = i
    }
  }
}

// this function permit us to get the coor of the each city
function getCoor(indexDeparture, indexArrival){
  latitudeD = allInfomations[indexDeparture].fields.pltf_latitude_entreeprincipale_wgs84
  longitudeD = allInfomations[indexDeparture].fields.pltf_longitude_entreeprincipale_wgs84
  latitudeA = allInfomations[indexArrival].fields.pltf_latitude_entreeprincipale_wgs84
  longitudeA = allInfomations[indexArrival].fields.pltf_longitude_entreeprincipale_wgs84
}

function getDistance(latitudeD, longitudeD, latitudeA, longitudeA){
  axios.get(url+'/calculdistance/'+latitudeD+'/'+longitudeD+'/'+latitudeA+'/'+longitudeA)
    .then(function(response){
      distance = response.data.distance
      document.getElementById("sum").innerHTML=distance;
      axios.get(url+'/calculprice/'+distance)
        .then(function(response){
        price = response.data.price
        document.getElementById("price").innerHTML=price;
      })
    })
}

export default {
  name: 'HelloWorld',
  created() {
  axios.get('https://ressources.data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&rows=3270&sort=gare_alias_libelle_noncontraint&facet=gare_agencegc_libelle&facet=gare_regionsncf_libelle&facet=gare_ug_libelle&facet=pltf_departement_libellemin&facet=pltf_segmentdrg_libelle')
    .then(function (response) {
      // fields.gare_alias_libelle_noncontraint
      console.log(response.data.records)
      var i = null
      allInfomations = response.data.records
      for (i = 0; i < 3270; i++) {
        temp[i] = response.data.records[i].fields.gare_alias_libelle_noncontraint
        //console.log(temp[i])
      }
      //console.log(allInfomations[0].fields.pltf_latitude_entreeprincipale_wgs84)
    })
  },
  data () {
    let countries=temp
    //let countries = ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'AndorrA', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize']
    return {
      departure: '',
      arrival: '',
      countries: countries,
      selectedDeparture: null,
      selectedArrival: null,
      options: {},
      ifDistance: false
    }
  },
  methods: {

    onDepartureInputChange (departure) {
      if (departure.trim().length === 0) {
        return null
      }
      // return the matching countries as an array
      return this.countries.filter((country) => {
        return country.toLowerCase().includes(departure.toLowerCase())
      })
    },
    onArrivalInputChange (arrival) {
      if (arrival.trim().length === 0) {
        return null
      }
      // return the matching countries as an array
      return this.countries.filter((country) => {
        return country.toLowerCase().includes(arrival.toLowerCase())
      })
    },
    onDepartureSelected (item) {
      this.selectedDeparture = item
      this.departure = item
      if(this.selectedArrival != null){
        findCity(this.departure, this.arrival)
        getCoor(indexDeparture, indexArrival)
        getDistance(latitudeD, longitudeD, latitudeA, longitudeA)
        this.ifDistance=true
      }
    },
    onArrivalSelected (item) {
      this.selectedArrival = item
      this.arrival = item
      if(this.selectedDeparture != null){
        console.log(allInfomations)
        findCity(this.departure, this.arrival)
        getCoor(indexDeparture, indexArrival)
        getDistance(latitudeD, longitudeD, latitudeA, longitudeA)
        this.ifDistance=true
      }
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