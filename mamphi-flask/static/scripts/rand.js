let rand_w1_list = document.querySelector("#rand-w1-btn");

rand_w1_list.addEventListener('click', function() {
    let body = document.getElementById("app");

    body.innerHTML = `<section>
    <div>
        <h2>Randomisierung erste Woche</h2>
        <table>
        <thead>
            <tr>
                <td>Patient_ID</td>
                <td>Zentrum</td>
                <td>Behandlungsarm</td>
                <td>Datum</td>
            </tr>
            </thead>
            <tbody id=rand-list>
            </tbody>
        </table>
    </div>`

    // 1. XHR-Instanz erstellen
    let xhr = new XMLHttpRequest();
    // 2. HTTP-Anfrage initialisieren (hier:
    // REST-Service, der die Liste von Zentren liefert)
    xhr.open("Get", "http://127.0.0.1:5000/mamphi/random-week1");
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
});