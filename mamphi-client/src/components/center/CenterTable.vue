<template>
    <div>
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
                <center-card class="center-list-item" v-for="center in list" v-bind:center="center" v-bind:key="center.center_Id"></center-card>
            </tbody>
        </table>
    </div>
</template>

<script>
import CenterCard from './CenterCard'
export default {
    name: 'consent-table',

    data(){
        return {
            list: []
        }
    },

    components: {
        CenterCard: CenterCard
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/center")
        .then(response => response.json())
        .then(json => (this.list = JSON.parse(json)));
    }
    
}
</script>