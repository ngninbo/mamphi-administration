<template>
    <section>
    <div>
        <h2>Randomisierung zweite Woche</h2>
        <p><label id="rand-list-btn">Liste auswählen</label>
        <select id="selection" v-model="selection">
        <option value="Null">-- Bitte auswählen --</option>
        <option value="1">Vollständige Liste: Standard</option>
        <option value="2">Wochenliche Liste Deutschland: Anzahl der Patienten pro Zentrum</option>
        <option value="3">Wochenliche Liste Großbritanien: Anzahl der Patienten pro Zentrum</option>
        </select>
        </p>  
    </div>
    <div>
        <span v-if="selection === '1'">
            <random-table></random-table>
        </span>
        <span v-else-if="selection === '2'">
            <weekly-list v-bind:weeklyTable="list.Germany"></weekly-list>
        </span>
        <span v-else-if="selection === '3'">
            <weekly-list v-bind:weeklyTable="list.UK"></weekly-list>
        </span>
        <span v-else>
            <random-table></random-table>
        </span>
    </div>
    </section>
</template>


<script>
import RandomTable from './RandomTable'
import WeeklyList from './WeeklyList'
export default {
    name: 'random-week',
    data: function(){
        return{
            selection: 'Null',
            list: []
        };
    },

    components:{
        RandomTable: RandomTable,
        WeeklyList: WeeklyList
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/patient/center/week2")
        .then(response => response.json())
        .then(json => (this.list = json));
    }
}
</script>