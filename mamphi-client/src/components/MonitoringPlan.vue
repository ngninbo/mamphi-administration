<template>
    <div>
        <h2>Monitoring-Plan</h2>
        <div>
            <p>Nachfolgend ist die Planung, wann welcher Monitor welches Zentrum besuchen soll</p>
            <table>
                <thead>
                    <tr>
                        <td>Zentrum</td>
                        <td>Land</td>
                        <td>Ort</td>
                        <td>Pr&#xFC;fer</td>
                        <td>Monitor</td>
                        <td>Anzahl Patienten</td>
                        <td colspan="5">Monitorbesuche</td>
                    </tr>
                </thead>
                <tbody id=monitoring-plan>
                    <tr v-for="item in list" v-bind:key="item.Zentrum_Id">
                        <td>{{ item.Zentrum_Id }}</td>
                        <td>{{ item.Land === "D" ? "Deutschland": "Großbritanien" }}</td>
                        <td>{{ item.Ort }}</td>
                        <td>{{ item.Pruefer }}</td>
                        <td>{{ item.Monitor }}</td>
                        <td>{{ item.NP }}</td>
                        <span v-if="item.Monitor_Visite != undefined">
                            <td v-for="date in item.Monitor_Visite" v-bind:key="date">{{ date }}</td>
                        </span>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name: 'monitoring-plan',

    data(){
        return{
            list: []
        }
    },

    mounted(){
        fetch('http://127.0.0.1:5000/mamphi/monitor/planing')
        .then(response => response.json())
        .then(json => (this.list = JSON.parse(json)))
    }
}
</script>