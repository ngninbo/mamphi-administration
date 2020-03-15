<template>
    <div>
        <p>Bitte wählen Sie die Einwilligung (ID) aus, welche Sie löschen wollen.</p>
        <p><label for="consent-to-delete">Patient_ID: </label>
        <select id="consent-to-delete" v-model="patient_id">
            <option value="Null"></option>
            <option v-for="consent in consent_list" v-bind:key="consent.Patient_Id">{{ consent.Patient_Id }}</option>
        </select>
        <button id="del-btn" v-on:click="deleteConsent()">Löschen</button>
        </p>
    </div>
</template>

<script>
export default {
    name: 'consent-delete',

    data: function(){
        return {
            consent_list: [],
            patient_id: ''
        }
    },

    methods: {
        deleteConsent(){
            let xhr = new XMLHttpRequest();
            xhr.open("Delete", "http://127.0.0.1:5000/mamphi/consent/delete");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.responseType = "json";
            xhr.send(this.patient_id);
            xhr.onload = () => {
                alert("Patienteneinwilligung wurde gelöschen!");
            };
        }
    },

    mounted(){
        fetch('http://127.0.0.1:5000/mamphi/consents')
        .then(response => response.json())
        .then(json => (this.consent_list = JSON.parse(json)))
    }
}
</script>