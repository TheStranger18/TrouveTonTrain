<template>
  <div class="home">
  
 </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAutosuggest from 'vue-autosuggest'

Vue.use(VueAutosuggest)
Vue.use(axios)

var temp = []

export default {
  name: 'home',

  created() {
  axios.get('https://ressources.data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&rows=3270&sort=gare_alias_libelle_noncontraint&facet=gare_agencegc_libelle&facet=gare_regionsncf_libelle&facet=gare_ug_libelle&facet=pltf_departement_libellemin&facet=pltf_segmentdrg_libelle')
    .then(function (response) {
      // handle success
      // fields.gare_alias_libelle_noncontraint
      console.log(response.data.records)
      var i = null
      for (i = 0; i < 3270; i++) {
        temp[i] = response.data.records[i].fields.gare_alias_libelle_noncontraint
        //console.log(temp[i])
      } 
    })
  },

  data() {
      return {
        selected: '',
        options: [{
          data: ['Frodo', 'Samwise', 'Gandalf', 'Galadriel', 'Faramir', 'Éowyn', 'Peregrine Took', 'Boromir', 'Legolas', 'Gimli', 'Gollum', 'Beren', 'Saruman', 'Sauron', 'Théoden']
        }],
        filteredOptions: [],
        inputProps: {
          id: "autosuggest__input",
          onInputChange: this.onInputChange,
          placeholder: "Type 'e'"
        },
        limit: 10
      };
    },
    methods: {
      onSelected(option) {
          this.selected = option.item;
      },
      onInputChange(text) {
        if (text === '' || text === undefined) {
          return;
        }
        
        /* Full control over filtering. Maybe fetch from API?! Up to you!!! */
        const filteredData = this.options[0].data.filter(item => {
          return item.toLowerCase().indexOf(text.toLowerCase()) > -1;
        }).slice(0, this.limit);
        
        this.filteredOptions = [{
          data: filteredData
        }];
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

body {
      max-width: 800px;
      padding: 20px;
      margin-left: auto !important;
      margin-right: auto !important;
      font-family: monospace;
    }
    
    #autosuggest__input {
      outline: none;
      position: relative;
      display: block;
      font-family: monospace;
      font-size: 20px;
      border: 1px solid #616161;
      padding: 10px;
      width: 100%;
      box-sizing: border-box;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
    }
    
    #autosuggest__input.autosuggest__input-open {
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }
    
    .autosuggest__results-container {
      position: relative;
      width: 100%;
    }
    
    .autosuggest__results {
      font-weight: 300;
      margin: 0;
      position: absolute;
      z-index: 10000001;
      width: 100%;
      border: 1px solid #e0e0e0;
      border-bottom-left-radius: 4px;
      border-bottom-right-radius: 4px;
      background: white;
      padding: 0px;
      overflow: scroll;
      max-height: 200px;
    }
    
    .autosuggest__results ul {
      list-style: none;
      padding-left: 0;
      margin: 0;
    }
    
    .autosuggest__results .autosuggest__results_item {
      cursor: pointer;
      padding: 15px;
    }
    
    #autosuggest ul:nth-child(1) > .autosuggest__results_title {
      border-top: none;
    }
    
    .autosuggest__results .autosuggest__results_title {
      color: gray;
      font-size: 11px;
      margin-left: 0;
      padding: 15px 13px 5px;
      border-top: 1px solid lightgray;
    }
    
    .autosuggest__results .autosuggest__results_item:active,
    .autosuggest__results .autosuggest__results_item:hover,
    .autosuggest__results .autosuggest__results_item:focus,
    .autosuggest__results .autosuggest__results_item.autosuggest__results_item-highlighted {
      background-color: #ddd;
    }
</style>
