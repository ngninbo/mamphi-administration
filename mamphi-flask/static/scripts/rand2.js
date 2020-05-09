var data_week2 = "";
fetch('http://127.0.0.1:5000/mamphi/patient/center/week2')
    .then(response => response.json())
    .then(json => (data_week2 = JSON.parse(json)))

let rand_w2_list = document.querySelector("#rand-w2-btn");

rand_w2_list.addEventListener('click', function() {
    let body = document.getElementById("app");

    body.innerHTML = `<section>
    <div>
        <h2>Randomisierung zweite Woche</h2>
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
    </div>`

    let randbtn = document.getElementById("rand-list-btn");

    randbtn.addEventListener('click', function() {
        displayTableWeek2();
    });

});

function displayTableWeek2() {

    var selection = document.getElementById("selection").value;

    switch (selection) {
        case "1":
            createRandTable();
            // 1. XHR-Instanz erstellen
            let xhr = new XMLHttpRequest();
            // 2. HTTP-Anfrage initialisieren (hier:
            // REST-Service, der die Liste von Zentren liefert)
            xhr.open("Get", "http://127.0.0.1:5000/mamphi/random-week2");
            // 3 Gewünschtes Datenformat setzen
            xhr.responseType = "json"
                // 4. Anfrage senden
            xhr.send();
            // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
            xhr.onload = () => {
                let body = document.getElementById("rand-list");

                for (let patient of JSON.parse(xhr.response)) {
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
            for (let center of data_week2["Germany"]) {
                let prop = document.createElement("tr");

                prop.innerHTML = `<td>${center.Zentrum}</td>
                            <td>${center.Number_Of_Patient}</td>`;

                body.appendChild(prop);
            }
            break;

        case "3":
            weeklyList();
            let content = document.getElementById("weekly-list-table");
            for (let center of data_week2["UK"]) {
                let prop = document.createElement("tr");

                prop.innerHTML = `<td>${center.Zentrum}</td>
                            <td>${center.Number_Of_Patient}</td>`;

                content.appendChild(prop);
            }
            break;
    }

};