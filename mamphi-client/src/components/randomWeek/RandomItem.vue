<template>
    <tr>
        <td>{{patient.Patient_Id}}</td>
        <td>{{patient.Zentrum}}</td>
        <td>{{patient.Behandlungsarm}}</td>
        <td>{{patient.Datum}}</td>
    </tr>
</template>

<script>
export default {
    name: 'random-item',
    props: ['patient']
}
</script>