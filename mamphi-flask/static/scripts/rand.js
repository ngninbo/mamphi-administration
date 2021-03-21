let rand_w1_list = document.querySelector("#rand-w1-btn");

var data_week1 = "";
fetch('http://127.0.0.1:5000/mamphi/patient/center/week1')
    .then(response => response.json())
    .then(json => (data_week1 = json))

rand_w1_list.addEventListener('click', function() {

    let body = document.getElementById("app");

    body.innerHTML = `<section>
    <div>
        <h2>Randomisierung erste Woche</h2>
        <p>
        <select id="selection">
        <option value="Null">Bitte Liste auswählen</option>
        <option value="1">Vollständige Liste</option>
        <option value="2">Wochenliche Liste Deutschland: Anzahl der Patienten pro Zentrum</option>
        <option value="3">Wochenliche Liste Großbritanien: Anzahl der Patienten pro Zentrum</option>
        </select><button id="rand-list-btn">Anzeigen</button>
        </p>
        <div id="rand-week1-table">
        </div>
    </div>`;

    let randbtn = document.getElementById("rand-list-btn");

    randbtn.addEventListener('click', function() {
        displayTable();
    });

});

function createRandTable() {
    let rand_table = document.getElementById("rand-week1-table");

    rand_table.innerHTML = `<table>
    <thead>
        <tr>
            <th>Patient_ID</th>
            <th>Zentrum</th>
            <th>Behandlungsarm</th>
            <th>Datum</th>
        </tr>
        </thead>
        <tbody id="rand-list">
        </tbody>
    </table>`;
};

function weeklyList() {
    list = document.getElementById("rand-week1-table");

    list.innerHTML = `<table>
    <thead>
        <tr>
            <th>Zentrum</th>
            <th>Anzahl Patienten</th>
        </tr>
        </thead>
        <tbody id="weekly-list-table">
        </tbody>
    </table>`
};

function displayTable() {

    var selection = document.getElementById("selection").value;

    switch (selection) {
        case "1":
            createRandTable();
            // 1. XHR-Instanz erstellen
            let xhr = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von Zentren liefert)
            xhr.open("Get", "http://127.0.0.1:5000/mamphi/random/week1");
            // 3 Gewünschtes Datenformat setzen
            xhr.responseType = "json"
                // 4. Anfrage senden
            xhr.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr.onload = () => {
                let body = document.getElementById("rand-list");

                for (let patient of xhr.response) {
                    let prop = document.createElement("tr");

                    prop.innerHTML = `<td>${patient.Patient_Id}</td>
                                <td>${patient.Zentrum}</td>
                                <td>${patient.Behandlungsarm}</td>
                                <td>${patient.Datum}</td>`;

                    body.appendChild(prop);
                }
            };
            break;

        case "2":
            weeklyList();
            let body = document.getElementById("weekly-list-table");
            for (let center of data_week1["Germany"]) {
                let prop = document.createElement("tr");

                prop.innerHTML = `<td>${center.Zentrum}</td>
                            <td>${center.Number_Of_Patient}</td>`;

                body.appendChild(prop);
            }
            break;

        case "3":
            weeklyList();
            let content = document.getElementById("weekly-list-table");
            for (let center of data_week1["UK"]) {
                let prop = document.createElement("tr");

                prop.innerHTML = `<td>${center.Zentrum}</td>
                            <td>${center.Number_Of_Patient}</td>`;

                content.appendChild(prop);
            }
            break;
    }

};