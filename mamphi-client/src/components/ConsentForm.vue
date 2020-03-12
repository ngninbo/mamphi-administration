<template>
    <div>
        <p><label for="zentrum">Zentrum: </label>
        <select id="zentrum" v-model="consent.Zentrum">
        <option value="Null"></option>
        <option v-for="item in centerList" v-bind:key="item.Zentrum_Id">{{ item.Zentrum_Id }}</option>
        </select></p>
        <p><label for="informed-consent">Einwilligung erteilt?: </label>
        <select id="informed-consent" v-model="consent.Einwilligung">
        <option value="Null"></option>
        <option value="ja" name="ja">Ja</option>
        <option value="nein" name="nein">Nein</option>
        </select></p>
        <p><label for="datum">Datum: </label>
        <input id="datum" type="date" v-model="consent.Datum"/></p>
        <p><button id="save-consent-btn" v-on:click="saveConsent()">Speichern</button>
        </p>
    </div>
</template>

<script>
export default {
    name: 'consent-form',

    data() {
        return {
            consent: {
                Zentrum: '',
                Einwilligung: '',
                Datum: ''
            },
            centerList: [],
        }
    },

    methods: {
        saveConsent() {
            // 1. XHR-Instanz erstellen
            let xhr = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren 
            xhr.open("Post", "http://127.0.0.1:5000/mamphi/consents/update");
            // 3 HTTP-Header für das Datenformat in der Anfrage setzen
            xhr.setRequestHeader("Content-Type", "application/json");
            // 4. Gewünsche Datenformat für die Antwort setzen und Anfrage senden (hier mit JSON-Daten)
            xhr.responseType = "json";
            xhr.send(JSON.stringify(this.consent));
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, 
            // sobald die Antwort vollstandig vorliegt
            xhr.onload = () => {
                alert("Ein neues Zentrum wurde erstellt!");
            };
        }
    },

    mounted() {
        fetch('http://127.0.0.1:5000/mamphi/center')
        .then(response => response.json())
        .then(json => (this.centerList = JSON.parse(json)))
    }
}
</script>