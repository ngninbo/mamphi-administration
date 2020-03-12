<template>
    <div>
        <table>
    <thead>
        <tr>
            <td>Zentrum</td>
            <td>Anzahl Patienten</td>
        </tr>
        </thead>
        <tbody id="weekly-list-table" >
            <tr v-for="element in weeklyTable" v-bind:key="element.Patient_Id">
            <td>{{element.Zentrum}}</td>
            <td>{{element.Number_Of_Patient}}</td></tr>   
        </tbody>
    </table>
    </div>
</template>

<script>
export default {
    name: 'weekly-list',
    props: ['weeklyTable']
}
</script>