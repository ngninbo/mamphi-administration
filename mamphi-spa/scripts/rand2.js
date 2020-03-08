var data = "";
fetch('http://127.0.0.1:5000/mamphi/patient/center/week2')
    .then(response => response.json())
    .then(json => (data = JSON.parse(json)))

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
        displayTable();
    });

});