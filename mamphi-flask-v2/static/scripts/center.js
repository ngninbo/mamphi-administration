let zentren = document.querySelector("#center-list-btn");

var center_list = "";
fetch('http://127.0.0.1:5000/mamphi/center')
    .then(response => response.json())
    .then(json => (center_list = JSON.parse(json)))

zentren.addEventListener('click', function() {
    let body = document.getElementById("app");
    body.innerHTML = `<section>
    <div id="center-content">
        <h2>Liste der Zentren</h2>
        <div>
        <p><label>Liste Verwaltung: </label>
        <select id="selection">
        <option value="Null"></option>
        <option value="1">Neues Zentrum anlegen</option>
        <option value="2">Zentrum löschen</option>
        <option value="3">Liste aller Zentren anzeigen</option>
        </select><button id="action-btn">Ausführen</button>
        </p>
        </div>
        <div id="center-admin"></div>
    </div>`

    let action = document.getElementById("action-btn");

    action.addEventListener('click', function() {
        let selection = document.getElementById("selection").value;

        switch (selection) {
            case "1":
                centerForm();
                break;
            case "2":
                deleteCenter();
                break;
            case "3":
                showCenterList();
                break;
            default:
                showCenterList();
                break;
        }
    });

});

function showCenterList() {
    let center_form = document.getElementById("center-admin");

    center_form.innerHTML = `<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Land</th>
            <th>Ort</th>
            <th>Pr&#xFC;fer</th>
            <th>Monitor</th>
        </tr>
        </thead>
        <tbody id=center-list>
        </tbody>
    </table>`

    let list = document.getElementById("center-list");

    for (let center of center_list) {
        let prop = document.createElement("tr");
        prop.innerHTML = `<td>${center.Zentrum_Id}</td>
                                <td>${center.Land === "D" ? "Deutschland": "Großbritanien"}</td>
                                <td>${center.Ort}</td>
                                <td>${center.Pruefer}</td>
                                <td>${center.Monitor}</td>`;

        list.appendChild(prop);
    }
};

function deleteCenter() {

    let center_form = document.getElementById("center-admin");

    center_form.innerHTML = `<p>Bitte wählen Sie das Zentrums (ID) aus, welche Sie löschen wollen.</p>
    <p><label for="center-to-delete">Zentrum_ID: </label>
    <select id="center-to-delete">
    <option value="Null"></option>
    </select><button id="del-btn">Löschen</button>
    </p>`

    let zentrum = document.getElementById("center-to-delete");

    for (let center of center_list) {
        let option = document.createElement("option");
        option.setAttribute("value", center.Zentrum_Id);
        option.innerHTML = center.Zentrum_Id;

        zentrum.append(option);
    }

    let delation = document.getElementById("del-btn");

    delation.addEventListener('click', function() {
        let center_id = document.getElementById("center-to-delete").value;
        alert("Sie sind gerade dabei das Zentrum mit der ID = " + center_id + " zu löschen!")
        deleteCenterItem(center_id);
    });
};

function centerForm() {
    let center_form = document.getElementById('center-admin');

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

function deleteCenterItem(center_id) {
    let xhr = new XMLHttpRequest();
    xhr.open("Delete", "http://127.0.0.1:5000/mamphi/center/delete");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.responseType = "json";
    xhr.send(center_id);
    xhr.onload = () => {
        alert("Das Zentrum wurde gelöschen!");
    };
};