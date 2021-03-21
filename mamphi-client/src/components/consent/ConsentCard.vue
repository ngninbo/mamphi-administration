<template>
    <tr>
        <td>{{consent.Patient_Id}}</td>
        <td>{{consent.Zentrum}}</td>
        <td>{{consent.Einwilligung}}</td>
        <td>{{consent.Datum}}</td>
    </tr>
</template>
<script>
export default {
    name: 'consent-card',
    props: ['consent']
};
</script>