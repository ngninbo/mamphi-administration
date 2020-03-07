<template>
    <tr class="center-card">
        <td>{{ center.Zentrum_Id}}</td>
        <td>{{center.Land === "D" ? "Deutschland": "Großbritanien"}}</td>
        <td>{{center.Ort}}</td>
        <td>{{center.Pruefer}}</td>
        <td>{{center.Monitor}}</td>
    </tr>
</template>

<script>
export default {
    name: 'center-card',
    props: ['center']
};
</script>