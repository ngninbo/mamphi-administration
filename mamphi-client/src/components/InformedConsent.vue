<template>
  <div>
    <section>
      <h2>Liste der Patienten Einwilligungen</h2>
    <div>
      <p>
      <select name="consentChoice" v-model="choice" class="consent-mgmnt">
        <option v-for="option in options" v-bind:key="option.value">{{ option.text }}</option>
      </select>
      <button>Anzeigen</button>
      </p>
    </div>
    <div id="consent-table">
        <span v-if="choice ==='1'">
          <consent-table></consent-table>
        </span>
        <span v-else-if="choice === '2'">
          <consent-missing></consent-missing>
        </span>
        <span v-else-if="choice === '3'">
          <consent-incomplete></consent-incomplete>
        </span>
        <span v-else-if="choice === '4'">
          <late-consent></late-consent>
        </span>
        <span v-else>
          <consent-table></consent-table>
        </span>
    </div>
  </section>
  </div>
</template>

<script>
import ConsentTable from './ConsentTable'
import ConsentIncomplete from './ConsentIncomplete'
import ConsentMissing from './ConsentMissing'
import LateConsent from './LateConsent'

export default {
  name: "informed-consent",
  data: function(){
    return{
      choice: '',

      options: [
        {text: "Bitte Liste auswählen", value: "null"},
        {text: "Vollstandige Liste der Einwilligungen", value: '1'},
        {text: "Liste der fehlenden Einwilligungen", value: "2"},
        {text: "Liste der unvollständigen Einwillungen", value: "3"},
        {text: "Liste der verspätete Einwilligungen", value: "4"}
      ]
    }
  },

  components: {
    ConsentTable: ConsentTable,
    ConsentIncomplete: ConsentIncomplete,
    ConsentMissing: ConsentMissing,
    LateConsent: LateConsent
  },

};
</script>