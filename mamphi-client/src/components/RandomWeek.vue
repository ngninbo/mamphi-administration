<template>
    <section>
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
            <tbody class=rand-list>
                <random-item class="rand-list-item" v-for="patient in list" v-bind:patient="patient" v-bind:key="patient.Patient_Id"></random-item>
            </tbody>
        </table>
    </div>
    </section>
</template>


<script>
import RandomItem from './RandomItem'
export default {
    name: 'random-week',
    data: function(){
        return{
            list: []
        };
    },

    components:{
        RandomItem: RandomItem
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/random-week1")
        .then(response => response.json())
        .then(json => (this.list = JSON.parse(json)));
    }
}
</script>