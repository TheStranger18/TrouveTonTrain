<template>
  <div class="hello">
   <div v-if="selected">
      You have selected <code>{{selected}}</code>
    </div>
    <div>
      <vue-autosuggest
        v-model="query"
        :suggestions="filteredOptions"
        @focus="focusMe"
        @click="clickHandler"
        @input="onInputChange"
        @selected="onSelected"
        :get-suggestion-value="getSuggestionValue"
        :input-props="{id:'autosuggest__input', placeholder:'Do you feel lucky, punk?'}">
        <div v-if="query">
          <ul>
            <li v-for="suggestion in suggestions" :key="suggestion.name">
              {{suggestion.name}}
            </li>
          </ul>
        </div>
      </vue-autosuggest>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAutosuggest from "vue-autosuggest";

Vue.use(VueAutosuggest);

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

  data() {
    return {
      query: "",
      selected: "",
      suggestions: [
        
          {name: "Hobbit"},
           {name: "Samwise"},
            {name: "Gandalf"},
             {name: "Aragorn"}
          
        
      ]
    };
  },
  computed: {
    filteredOptions() {
      return [
        { 
          data: this.suggestions.filter(option => {
            console.log("option="+option)
            console.log("suggestions="+this.suggestions)
            return option.name.toLowerCase().indexOf(this.query.toLowerCase()) > -1;
          })
        }
      ];
    }
  },
  methods: {
    clickHandler(item) {
      // event fired when clicking on the input
      console.log(item)

    },
    onSelected(item) {
      this.selected = item.item.name;
    },
    onInputChange(text) {
      // event fired when the input changes
      console.log(text)
    },
    /**
     * This is what the <input/> value is set to when you are selecting a suggestion.
     */
    getSuggestionValue(suggestion) {
      return suggestion;
    },
    focusMe(e) {
      console.log(e) // FocusEvent
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