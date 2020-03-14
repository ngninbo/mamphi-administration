<template>
  <div>
    <section>
      <h2>Liste der Patienten Einwilligungen</h2>
    <div>
      <p><label>Bitte eine Liste auswählen: </label>
      <select name="consentChoice" v-model="choice" class="consent-mgmnt">
        <option v-for="element in options" v-bind:key="element.value">{{ element.text }}</option>
      </select>
      </p>
    </div>
    <div id="consent-table">
        <span v-if="choice ==='Vollstandige Liste der Einwilligungen'">
          <consent-table></consent-table>
        </span>
        <span v-else-if="choice === 'Liste der fehlenden Einwilligungen'">
          <consent-missing></consent-missing>
        </span>
        <span v-else-if="choice === 'Liste der unvollständigen Einwillungen'">
          <consent-incomplete></consent-incomplete>
        </span>
        <span v-else-if="choice === 'Liste der verspätete Einwilligungen'">
          <late-consent></late-consent>
        </span>
        <span v-else>
          <consent-table></consent-table>
        </span>
    </div>
    <div id="verwaltung">
        <p><button class="add-btn" v-on:click="setIsClick()">Neue Eintrag zur Einwilligungsliste erstellen</button></p>
        <div id="consent-form">
          <span v-if="isClick == true">
            <consent-form></consent-form>
          </span>
          <span v-else></span>
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

export default {
  name: "informed-consent",
  data: function(){
    return{
      choice: '',

      options: [
        {text: "", value: "Null"},
        {text: "Vollstandige Liste der Einwilligungen", value: "1"},
        {text: "Liste der fehlenden Einwilligungen", value: "2"},
        {text: "Liste der unvollständigen Einwillungen", value: "3"},
        {text: "Liste der verspätete Einwilligungen", value: "4"}
      ],
      
      isClick: false
    }
  },

  methods: {
    setIsClick(){
      this.isClick = true;
    }
  },

  components: {
    ConsentTable: ConsentTable,
    ConsentIncomplete: ConsentIncomplete,
    ConsentMissing: ConsentMissing,
    LateConsent: LateConsent, 
    ConsentForm: ConsentForm
  },

};
</script>