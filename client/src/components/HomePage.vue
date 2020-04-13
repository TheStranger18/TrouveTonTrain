<template>
  <div class="hello">

  </div>
</template>

<script>
import axios from 'axios'

var temp = []

export default {
  name: 'HelloWorld',
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