let center_list = document.querySelector("#center-list-btn");

center_list.addEventListener('click', function() {
    let body = document.getElementById("app");
    /*
    TODO Add function for deleting center
    */
    body.innerHTML = `<section>
    <div id="center-content">
        <div>
        <h2>Liste der Zentren</h2>
        <table>
        <thead>
            <tr>
                <td>ID</td>
                <td>Land</td>
                <td>Ort</td>
                <td>Pr&#xFC;fer</td>
                <td>Monitor</td>
            </tr>
            </thead>
            <tbody id=center-list>
            </tbody>
        </table>
        </div>
        
        <div>
        <p><button id="center-add-btn">Neues Zentrum erstellen</button></p>
        <div id="center-form"></div>
        </div>
    </div>`

    // 1. XHR-Instanz erstellen
    let xhr = new XMLHttpRequest();
    // 2. HTTP-Anfrage initialisieren (hier:
    // REST-Service, der die Liste von Zentren liefert)
    xhr.open("Get", "http://127.0.0.1:5000/mamphi/center");
    // 3 Gewünschtes Datenformat setzen
    xhr.responseType = "json"
        // 4. Anfrage senden
    xhr.send();
    // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, sobald die Antwort vollstandig vorliegt
    xhr.onload = () => {
        let body = document.getElementById("center-list");

        for (let center of JSON.parse(xhr.response)) {
            let prop = document.createElement("tr");

            prop.innerHTML = `<td>${center.Zentrum_Id}</td>
                                <td>${center.Land === "D" ? "Deutschland": "Großbritanien"}</td>
                                <td>${center.Ort}</td>
                                <td>${center.Pruefer}</td>
                                <td>${center.Monitor}</td>`;

            body.appendChild(prop);
        }
    };

    centerForm();
});

function centerForm() {
    let center_addbtn = document.getElementById("center-add-btn");

    center_addbtn.addEventListener('click', function() {
        let center_form = document.getElementById('center-form');

        center_form.innerHTML = `<p><label for="land">Land: </label>
                                <select id="land">
                                <option value="Null">Bitte Land auswählen</option>
                                <option value="1">Deutschland</option>
                                <option value="2">Großbritanien</option>
                                </select></p>
                                <p><label for="ort">Ort: </label>
                                <input id="ort" type="text" name="ort"></input></p>
                                <p><label for="pruefer">Prüfer: </label>
                                <input id="pruefer" type="text" name="pruefer"></input></p>
                                <p><label for="monitor">Monitor: </label>
                                <input id="monitor" type="text" name="monitor" />
                                </p>
                                <p>
                                <button id="add-btn">Anlegen</button>
                                </p>`

        let add_btn = document.getElementById("add-btn");

        add_btn.addEventListener('click', function() {
            var newCenter = {
                Land: document.getElementById("land").value == "1" ? "D" : "GB",
                Ort: document.getElementById("ort").value,
                Pruefer: document.getElementById("pruefer").value,
                Monitor: document.getElementById("monitor").value
            };

            console.log(newCenter);
            uploadCenterTable(newCenter);
        });
    });
};

function uploadCenterTable(center) {
    // 1. XHR-Instanz erstellen
    let xhr = new XMLHttpRequest();
    // 2. HTTP-Anfrage initialisieren 
    xhr.open("Post", "http://127.0.0.1:5000/mamphi/center/update");
    // 3 HTTP-Header für das Datenformat in der Anfrage setzen
    xhr.setRequestHeader("Content-Type", "application/json");
    // 4. Gewünsche Datenformat für die Antwort setzen und Anfrage senden (hier mit JSON-Daten)
    xhr.responseType = "json";
    xhr.send(JSON.stringify(center));
    // 5. Callback-Funtion für das "load"-Erreignis registrieren - die Funktion wird aufgerufen, 
    // sobald die Antwort vollstandig vorliegt
    xhr.onload = () => {
        alert("Ein neues Zentrum wurde erstellt!");
    };
};