<template>
  <div>
    <section>
      <h2>Liste der Patienten Einwilligungen</h2>
    <div>
      <p><label>Bitte eine Liste auswählen: </label>
      <select name="consentChoice" v-model="choosenTable" class="consent-mgmnt">
        <option v-for="element in options" v-bind:key="element.value">{{ element.text }}</option>
      </select>
      </p>
    </div>
    <div id="consent-table">
        <span v-if="choosenTable ==='Vollstandige Liste der Einwilligungen'">
          <consent-table></consent-table>
        </span>
        <span v-else-if="choosenTable === 'Liste der fehlenden Einwilligungen'">
          <consent-missing></consent-missing>
        </span>
        <span v-else-if="choosenTable === 'Liste der unvollständigen Einwillungen'">
          <consent-incomplete></consent-incomplete>
        </span>
        <span v-else-if="choosenTable === 'Liste der verspätete Einwilligungen'">
          <late-consent></late-consent>
        </span>
        <span v-else>
        </span>
    </div>
    <div id="verwaltung">
      <div>
        <label>Eintrag löschen/anlegen: </label>
        <select v-model="actionChoosen">
          <option value="Null"></option>
          <option value="1">Neue Patienteneinwilligung anlegen</option>
          <option value="2">Patienteneinwilligung löschen</option>
        </select>
      </div>
      <div id="consent-admin">
        <span v-if="actionChoosen == '1'">
          <consent-form></consent-form>
        </span>
        <span v-else-if="actionChoosen == '2'">
          <consent-delete></consent-delete>
        </span>
      </div>
    </div>
  </section>
  </div>
</template>

<script>
import ConsentTable from './ConsentTable'
import ConsentIncomplete from './ConsentIncomplete'
import ConsentMissing from './ConsentMissing'
import LateConsent from './LateConsent'
import ConsentForm from './ConsentForm'
import ConsentDelete from './ConsentDelete'

export default {
  name: "informed-consent",
  data: function(){
    return{
      choosenTable: '',
      actionChoosen: '',
      options: [
        {text: "", value: "Null"},
        {text: "Vollstandige Liste der Einwilligungen", value: "1"},
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
    LateConsent: LateConsent, 
    ConsentForm: ConsentForm, 
    ConsentDelete: ConsentDelete
  },

};
</script>