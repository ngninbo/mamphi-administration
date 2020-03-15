<template>
<section>
    <h2>Liste der Zentren</h2>
    <div>
        <p>
        <label>Liste Verwaltung: </label>
        <select class="center-admin" name="center-admin" v-model="choice">
            <option value="Null"></option>
            <option value="1">Neues Zentrum erstellen</option>
            <option value="2">Zentrum löschen</option>
            <option value="3">Vollständige Liste anzeigen</option>
        </select>
        </p>
    </div>
    <div id="center-form">
        <span v-if="choice == '1'">
            <center-form></center-form>
        </span>
        <span v-else-if="choice == '2'">
            <center-delete></center-delete>
        </span>
        <span v-else-if="choice == '3'">
            <center-table></center-table>
        </span>
        </div>
    
</section>
</template>

<script>
import CenterForm from './CenterForm'
import CenterTable from './CenterTable'
import CenterDelete from './CenterDelete'

export default {
    name: 'center-list',
    data: function(){
        return {
            choice: ""
        };
    },
    components: {
        CenterForm: CenterForm,
        CenterTable: CenterTable,
        CenterDelete: CenterDelete
    }
}
</script>