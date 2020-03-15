<template>
    <div>
        <p>Bitte wählen Sie das Zentrums (ID) aus, welche Sie löschen wollen.</p>
        <p>
            <label for="center-to-delete">Zentrum_ID: </label>
            <select id="center-to-delete" v-model="center_id">
                <option value="Null"></option>
                <option v-for="center in center_ids" v-bind:key="center.Zentrum_Id">{{ center.Zentrum_Id }}</option>
            </select>
            <button id="del-btn" v-on:click="deleteCenter()">Löschen</button>
        </p>
    </div>
</template>

<script>
export default {
    name: 'center-delete',

    data: function(){
        return {
            center_ids: [],
            center_id: ''
        }
    },

    methods: {
        deleteCenter(){
            let xhr = new XMLHttpRequest();
            xhr.open("Delete", "http://127.0.0.1:5000/mamphi/center/delete");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.responseType = "json";
            xhr.send(this.center_id);
            xhr.onload = () => {
                alert("Das Zentrum wurde gelöschen!");
            };
        }
    },

    mounted() {
        fetch('http://127.0.0.1:5000/mamphi/center/ids')
        .then(response => response.json())
        .then(json => (this.center_ids = JSON.parse(json)))
    }
}
</script>