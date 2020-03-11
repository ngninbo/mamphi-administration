<template>
<section>
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
                <center-card class="center-list-item" v-for="center in list" v-bind:center="center" v-bind:key="center.center_Id"></center-card>
            </tbody>
        </table>
    </div>
    <div>
        <p><button id="center-add-btn" v-on:click="setIsClick()">Neues Zentrum erstellen</button></p>
        <div id="center-form">
            <span v-if="isClick == true">
                <center-form></center-form>
            </span>
            <span v-else></span> 
        </div>
    </div>
</section>
</template>

<script>
import CenterCard from './CenterCard'
import CenterForm from './CenterForm'

export default {
    name: 'center-list',
    data: function(){
        return {
            list: [],
            isClick: false
        };
    },
    components: {
        CenterCard: CenterCard,
        CenterForm: CenterForm
    },

    methods: {
        setIsClick() {
            this.isClick = true;
        }
    },

    mounted(){
        fetch("http://127.0.0.1:5000/mamphi/center")
        .then(response => response.json())
        .then(json => (this.list = JSON.parse(json)));
    }
}
</script>