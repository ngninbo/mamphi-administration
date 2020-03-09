let center_list = document.querySelector("#center-list-btn");

center_list.addEventListener('click', function() {
    let body = document.getElementById("app");
    /*
    TODO Add function for creating and deleting center
    */
    body.innerHTML = `<section>
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
});