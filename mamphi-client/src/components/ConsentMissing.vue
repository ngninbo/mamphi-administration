<template>
<div>
    <consent-table v-bind:consents="missing_consents"></consent-table>
    <button v-bind:click="navBack()">Zurück zur Liste der Einwilligungen</button>
</div>
</template>

<script>
import ConsentTable from './ConsentTable';
export default {
    name: 'consent-missing',
    data: function(){
        return {
            missing_consents: []
        };
    },
    components: {
        ConsentTable: ConsentTable
    },

    methods: {
        navBack: function(){
            this.$router.push('/description');
        }
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/consents/missing")
        .then(response => response.json())
        .then(json => (this.missing_consents = JSON.parse(json)));
    }

}
</script>