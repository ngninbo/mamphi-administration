<template>
  <div>
    <section>
      <h2>Liste der Patienten Einwilligungen</h2>
    <div>
      <div id="consent-table">
        <consent-table></consent-table>
      </div>
      <!--<button v-bind:click="showMissingConsents()">Fehlende Einwilligungen</button>
      <button v-bind:click="showIncompletedConsents()">Unvollständige Einwilligungen</button>
      <button v-bind:click="showLaterConsents()">Spätere Einwilligungen</button>-->
    </div>
  </section>
  </div>
</template>

<script>
import ConsentTable from './ConsentTable'
export default {
  name: "informed-consent",

  components: {
    ConsentTable: ConsentTable
  }

};
</script>