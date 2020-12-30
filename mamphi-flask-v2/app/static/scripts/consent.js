let consent_btn = document.getElementById("consent-list-btn");

var consent_list = "";

var center_ids = "";
fetch('http://127.0.0.1:5000/mamphi/center/ids')
    .then(response => response.json())
    .then(json => (center_ids = JSON.parse(json)))

consent_btn.addEventListener('click', function() {
    let body = document.getElementById("app");

    body.innerHTML = `<section>
    <div>
        <h2>Liste der Patienteneinwilligungen</h2>
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
        <p></p>
        <label>Patienteneinwilligung anlegen/löschen?: </label>
        <select id="choice">
        <option value="Null">-- Bitte auswählen --</option>
        <option value="1">Neue Einwilligung anlegen</option>
        <option value="2">Patienteneiwilligung löschen</option>
        </select><button id="action-btn">Ausführen</button>
        </select>
        <div id="consent-form"></div>
        </div>
    </div>`;

    let display = document.getElementById("list-show-btn");

    display.addEventListener('click', function() {
        displayConsents();
    });

    let action = document.getElementById("action-btn");

    action.addEventListener('click', function() {
        let choice = document.getElementById("choice").value;

        switch (choice) {
            case "1":
                consentForm();
                break;
            case "2":
                deleteConsent();
                break;
        }
    });
});

function deleteConsent() {

    let center_form = document.getElementById("consent-form");

    center_form.innerHTML = `<p>Bitte wählen Sie die Einwilligung (ID) aus, welche Sie löschen wollen.</p>
    <p><label for="consent-to-delete">Patient_ID: </label>
    <select id="consent-to-delete">
    <option value="Null"></option>
    </select><button id="del-btn">Löschen</button>
    </p>`

    let consent = document.getElementById("consent-to-delete");

    for (let patient of consent_list) {
        let option = document.createElement("option");
        option.setAttribute("value", patient.Patient_Id);
        option.innerHTML = patient.Patient_Id;

        consent.append(option);
    }

    let delation = document.getElementById("del-btn");

    delation.addEventListener('click', function() {
        let patient_id = document.getElementById("consent-to-delete").value;
        alert("Sie sind gerade dabei die Patienteneinwilligung mit der ID = " + patient_id + " zu löschen!")
        deleteConsentItem(patient_id);
    });
};

function deleteConsentItem(patient_id) {
    let xhr = new XMLHttpRequest();
    xhr.open("Delete", "http://127.0.0.1:5000/mamphi/consent/delete");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.responseType = "json";
    xhr.send(patient_id);
    xhr.onload = () => {
        alert("Patienteneinwilligung wurde gelöschen!");
    };
};

function consentForm() {

    let consentForm = document.getElementById("consent-form");

    consentForm.innerHTML = `<p><label for="zentrum">Zentrum: </label>
                                <select id="zentrum">
                                <option value="Null"><option>
                                </select></p>
                                <p><label for="informed-consent">Einwilligung erteilt?: </label>
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

    for (let center of center_ids) {
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
        alert("Neue Patienteneinwilligung wurde erstellt!");
    };
};

function makeTable() {
    consent_table = document.getElementById("consent-table");

    consent_table.innerHTML = `<table><thead>
        <tr>
            <th>Patienten_ID</th>
            <th>Zentrum</th>
            <th>Einwillung erteilt</th>
            <th>Datum der Einwilligung</th>
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
                                <td>${patient.Einwilligung.toUpperCase()}</td>
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
                                <td>${patient.Einwilligung.toUpperCase()}</td>
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
                consent_list = JSON.parse(xhr3.response);
                for (let patient of consent_list) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                <td>${patient.Zentrum}</td>
                                <td>${patient.Einwilligung === "nan" ? "" : patient.Einwilligung.toUpperCase()}</td>
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
                                    <td>${patient.Einwilligung.toUpperCase()}</td>
                                    <td>${patient.Datum === "NaT" ? "": patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;
    }
};