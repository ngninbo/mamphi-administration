<template>
    <div>
        <p><label for="land">Land: </label>
        <select id="land" v-model="center.Land">
        <option value="Null">-- Bitte Land auswählen --</option>
        <option value="D">Deutschland</option>
        <option value="GB">Großbritanien</option>
        </select></p>
        <p><label for="ort">Ort: </label>
        <input id="ort" type="text" name="ort" v-model="center.Ort"/></p>
        <p><label for="pruefer">Prüfer: </label>
        <input id="pruefer" type="text" name="pruefer" v-model="center.Pruefer"/>
        </p>
        <p><label for="monitor">Monitor: </label>
        <input id="monitor" type="text" name="monitor" v-model="center.Monitor"/>
        </p>
        <p><button class="add-btn" v-on:click="saveCenter()">Anlegen</button></p>
    </div>
</template>

<script>
export default {
    name: 'center-form',
    data: function(){
        return{
            center: {
                Land: "Null",
                Ort: '',
                Pruefer: '',
                Monitor: ''
            },
        }
    },

    methods: {
        saveCenter() {
            // 1. XHR-Instanz erstellen
            let xhr = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren 
            xhr.open("Post", "http://127.0.0.1:5000/mamphi/center/update");
            // 3 HTTP-Header für das Datenformat in der Anfrage setzen
            xhr.setRequestHeader("Content-Type", "application/json");
            // 4. Gewünsche Datenformat für die Antwort setzen und Anfrage senden (hier mit JSON-Daten)
            xhr.responseType = "json";
            xhr.send(JSON.stringify(this.center));
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, 
            // sobald die Antwort vollstandig vorliegt
            xhr.onload = () => {
                alert("Ein neuer Eintrag wurde erstellt!");
            };
        }
    }
}
</script>