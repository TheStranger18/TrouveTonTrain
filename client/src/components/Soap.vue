<script>
export default {
  name: 'SOAP',
}

var soap = require('soap');
var url = 'localhost:5000/soap/someservice?wsdl';
var args = {name: 'value'};
soap.createClientAsync(url).then((client) => {
  return client.MyFunctionAsync(args);
}).then((result) => {
  console.log(result);
});
</script>
<template>
  <form @submit.prevent="submitForm">
    <p><strong>Ville 1 :</strong></p>
    <p>Longitude : 
    <input v-model.number="longitudeA" type="number"></p>
    <p>Latitude : 
    <input v-model.number="latitudeA" type="number"></p>

    <p><strong>Ville 2</strong></p>
    <p>Longitude : 
    <input v-model.number="longitudeB" type="number"></p>
    <p>Latitude : 
    <input v-model.number="latitudeB" type="number"></p>
  </form>
</template>