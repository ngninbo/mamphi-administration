<template>
<div>
    <consent-table v-bind:consents="late_consents"></consent-table>
    <button v-bind:click="navBack()">Zurück zur Liste der Einwilligungen</button>
</div>
</template>

<script>
import ConsentTable from './ConsentTable';
export default {
    name: 'consent-incomplete',
    data: function(){
        return {
            late_consents: []
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
        fetch("http://127.0.0.1:5000/mamphi/consents/later")
        .then(response => response.json())
        .then(json => (this.late_consents = JSON.parse(json)));
    }

}
</script>