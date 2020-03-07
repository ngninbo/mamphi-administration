<template>
  <div>
    <section>
      <h2>Liste der Patienten Einwilligungen</h2>
    <div>
      <p>
      <select name="consentChoice" v-model="choice" class="consent-mgmnt">
        <option v-for="option in options" v-bind:key="option.value">{{ option.text }}</option>
      </select>
      </p>
      <!--<button v-bind:click="showConsents()">Anzeigen</button>-->
    </div>
    <div id="consent-table">
        <consent-table></consent-table>
    </div>
  </section>
  </div>
</template>

<script>
import ConsentTable from './ConsentTable'
export default {
  name: "informed-consent",
  data: function(){
    return{
      choice: '',

      options: [
        {text: "Bitte Liste auswählen", value: "null"},
        {text: "Liste der fehlenden Einwilligungen", value: "1"},
        {text: "Liste der unvollständigen Einwillungen", value: "2"},
        {text: "Liste der verspätete Einwilligungen", value: "3"}
      ]
    }
  },

  components: {
    ConsentTable: ConsentTable
  },

  methods: {
    showConsents: function(){
      switch(this.choice){
        case "1":
          this.$router.push('/missing');
          break;
        
        case "2":
          this.$router.push('/incomplete');
          break;

        case "3":
          this.$router.push('/late');
          break;
      }
      
    }
  }

};
</script>