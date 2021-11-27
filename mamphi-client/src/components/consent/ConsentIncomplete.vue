<template>
<div>
    <table>
          <thead>
            <tr>
              <td>Patienten_ID</td>
              <td>Zentrum</td>
              <td>Einwillung erteilt</td>
              <td>Datum der Einwilligung</td>
            </tr>
          </thead>
          <tbody id="consent-list">
            <consent-card
              class="consent-item"
              v-for="consent in incompleted_consents"
              v-bind:consent="consent"
              v-bind:key="consent.Patient_Id"
            ></consent-card>
          </tbody>
        </table>
</div>
</template>

<script>
import ConsentCard from './ConsentCard'
export default {
    name: 'consent-incomplete',
    data: function(){
        return {
            incompleted_consents: []
        };
    },
    components: {
        ConsentCard: ConsentCard
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/consents/incomplete")
        .then(response => response.json())
        .then(json => (this.incompleted_consents = JSON.parse(json)));
    }

}
</script>