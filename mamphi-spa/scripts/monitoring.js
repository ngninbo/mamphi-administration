let monitoring = document.getElementById("monitoring-btn");

var planing = "";
fetch('http://127.0.0.1:5000/mamphi/monitor/planing')
    .then(response => response.json())
    .then(json => (planing = json))

monitoring.addEventListener('click', function() {

    let body = document.getElementById("app");

    body.innerHTML = `<h2>Monitoring-Plan</h2>
    <div><p>Nachfolgend ist die Planung, wann welcher Monitor welches Zentrum besuchen soll</p>
    <table>
    <thead>
        <tr>
            <th>Zentrum</th>
            <th>Land</th>
            <th>Ort</th>
            <th>Pr&#xFC;fer</th>
            <th>Monitor</th>
            <th>Anzahl Patienten</th>
            <th colspan="5">Monitorbesuche</th>
        </tr>
        </thead>
        <tbody id=monitoring-plan>
        </tbody>
    </table>
    </div>`;

    let plan = document.getElementById('monitoring-plan');

    for (let center of planing) {
        let row = document.createElement("tr");

        var visites = [];

        if (center.Monitor_Visite != undefined) {
            visites = center.Monitor_Visite;
        }

        row.innerHTML = `<td> ${ center.Zentrum_Id }</td>
        <td>${ center.Land } </td>
        <td>${ center.Ort }</td>
        <td>${ center.Pruefer }</td>
        <td>${ center.Monitor }</td>
        <td>${ center.NP}</td>
        <td>${ visites[0] !=undefined ? visites[0] : "Kein Termin" }</td>
        <td>${ visites[1] !=undefined ? visites[1] : "Kein Termin" }</td>
        <td>${ visites[2] !=undefined ? visites[2] : "Kein Termin" }</td>
        <td>${ visites[3] !=undefined ? visites[3] : "Kein Termin" }</td>
        <td>${ visites[4] !=undefined ? visites[4] : "Kein Termin" }</td>`

        plan.appendChild(row);


    }
});