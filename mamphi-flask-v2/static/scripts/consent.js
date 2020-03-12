let consent_btn = document.getElementById("consent-list-btn");

consent_btn.addEventListener('click', function() {
    let body = document.getElementById("app");

    /*
    TODO add function for deleting consent
    */

    body.innerHTML = `<section>
    <div>
        <p>
            <label>Einwillungen:</label>
            <select id="selected-option">
            <option value="default">Bitte einzuzeigende Liste der Einwillungen auswählen</option>
            <option value="Vollständige Liste">Vollständige Liste</option>
            <option value="Liste der Patienten bei denen die Einwilligung fehlt">Liste der Patienten bei denen die Einwilligung fehlt</option>
            <option value="Liste von Patienten bei denen Daten fehlen">Liste von Patienten bei denen Daten fehlen</option>
            <option value="Liste von Patienten bei denen die Einwilligung nach der Randomisierung kommt">Liste von Patienten bei denen die Einwilligung nach der Randomisierung kommt</option>
            </select><button id="list-show-btn">Anzeigen</button>
        </p>
        <div id="consent-table"></div>
        <div id="verwaltung">
        <p><button id="consent-add-btn">Neue Eintrag zur Einwilligungsliste erstellen</button></p>
        <div id="consent-form"></div>
        </div>
    </div>`;

    let display = document.getElementById("list-show-btn");

    display.addEventListener('click', function() {
        displayConsents();
    });

    consentForm();
});

function consentForm() {
    let consentbtn = document.getElementById("consent-add-btn");
    var center_table = "";
    fetch('http://127.0.0.1:5000/mamphi/center')
        .then(response => response.json())
        .then(json => (center_table = JSON.parse(json)))

    consentbtn.addEventListener("click", function() {
        let consentForm = document.getElementById("consent-form");

        consentForm.innerHTML = `<p><label for="zentrum">Zentrum: </label>
                                <select id="zentrum">
                                <option value="Null"><option>
                                <select></p>
                                <p><label for="informed-consent">Einwilligung erteilt?: <label>
                                <select id="informed-consent">
                                <option value="Null"></option>
                                <option value="ja" name="ja">Ja</option>
                                <option value="nein" name="nein">Nein</option>
                                </select></p>
                                <p><label for="datum">Datum: </label>
                                <input id="datum" type="date"></input></p>
                                <p>
                                <button id="save-consent-btn">Speichern</button>
                                </p>`;

        let zentrum = document.getElementById("zentrum");

        for (let center of center_table) {
            let option = document.createElement("option");
            option.setAttribute("value", center.Zentrum_Id);
            option.innerHTML = center.Zentrum_Id;

            zentrum.append(option);
        }

        let consent_addbtn = document.getElementById("save-consent-btn");

        consent_addbtn.addEventListener('click', function() {
            var informed_consent = {
                Zentrum: parseInt(document.getElementById("zentrum").value),
                Einwilligung: document.getElementById("informed-consent").value,
                Datum: document.getElementById("datum").value
            };
            console.log(informed_consent);
            uploadConsentTable(informed_consent);
        });
    });
};

function uploadConsentTable(consent) {
    // 1. XHR-Instanz erstellen
    let xhr = new XMLHttpRequest();
    // 2. HTTP-Anfrage initialisieren
    xhr.open("Post", "http://127.0.0.1:5000/mamphi/consents/update");
    // 3 HTTP-Header für das Datenformat in der Anfrage setzen
    xhr.setRequestHeader("Content-Type", "application/json");
    // 4. Gewünsche Datenformat für die Antwort setzen und Anfrage senden (hier mit JSON-Daten)
    xhr.responseType = "json";
    xhr.send(JSON.stringify(consent));
    // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen,
    // sobald die Antwort vollstandig vorliegt
    xhr.onload = () => {
        alert("Ein neues Zentrum wurde erstellt!");
    };
};

function makeTable() {
    consent_table = document.getElementById("consent-table");

    consent_table.innerHTML = `<table><thead>
        <tr>
            <td>Patienten_ID</td>
            <td>Zentrum</td>
            <td>Einwillung erteilt</td>
            <td>Datum der Einwilligung</td>
        </tr></thead>
        <tbody id="consent-list"></tbody></table>`;
};

function displayConsents() {
    var choice = document.getElementById("selected-option").value;

    switch (choice) {
        case "Liste der Patienten bei denen die Einwilligung fehlt":
            makeTable();
            // 1. XHR-Instanz erstellen
            let xhr1 = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von fehlende Einwilligungen liefert)
            xhr1.open("Get", "http://127.0.0.1:5000/mamphi/consents/missing");
            // 3 Gewünschtes Datenformat setzen
            xhr1.responseType = "json"
                // 4. Anfrage senden
            xhr1.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr1.onload = () => {
                let body = document.getElementById("consent-list");

                for (let patient of JSON.parse(xhr1.response)) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                <td>${patient.Zentrum}</td>
                                <td>${patient.Einwilligung}</td>
                                <td>${patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;

        case "Liste von Patienten bei denen Daten fehlen":
            makeTable();
            // 1. XHR-Instanz erstellen
            var xhr2 = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von unvollständigen Einwilligungen liefert)
            xhr2.open("Get", "http://127.0.0.1:5000/mamphi/consents/incomplete");
            // 3 Gewünschtes Datenformat setzen
            xhr2.responseType = "json"
                // 4. Anfrage senden
            xhr2.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr2.onload = () => {
                let body = document.getElementById("consent-list");

                for (let patient of JSON.parse(xhr2.response)) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                <td>${patient.Zentrum}</td>
                                <td>${ patient.Einwilligung}</td>
                                <td>${patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;

        case "Vollständige Liste":
            makeTable();
            // 1. XHR-Instanz erstellen
            var xhr3 = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von Einwilligungen liefert)
            xhr3.open("Get", "http://127.0.0.1:5000/mamphi/consents");
            // 3 Gewünschtes Datenformat setzen
            xhr3.responseType = "json"
                // 4. Anfrage senden
            xhr3.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr3.onload = () => {
                var body = document.getElementById("consent-list");

                for (let patient of JSON.parse(xhr3.response)) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                <td>${patient.Zentrum}</td>
                                <td>${patient.Einwilligung === "nan" ? "" : patient.Einwilligung}</td>
                                <td>${patient.Datum === "NaT" ? "": patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;

        case "Liste von Patienten bei denen die Einwilligung nach der Randomisierung kommt":
            makeTable();
            // 1. XHR-Instanz erstellen
            var xhr4 = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von Einwilligungen liefert)
            xhr4.open("Get", "http://127.0.0.1:5000/mamphi/consents/later");
            // 3 Gewünschtes Datenformat setzen
            xhr4.responseType = "json"
                // 4. Anfrage senden
            xhr4.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr4.onload = () => {
                var body = document.getElementById("consent-list");

                for (let patient of JSON.parse(xhr4.response)) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                    <td>${patient.Zentrum}</td>
                                    <td>${patient.Einwilligung}</td>
                                    <td>${patient.Datum === "NaT" ? "": patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;
    }
};