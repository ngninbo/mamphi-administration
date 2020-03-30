<template>
  <div id="app">
    <header><h1>Willkommen auf der Webanwendung zur Mamphi-Studie Verwaltung!</h1>
    </header>
    
    <nav class="navbar">
      <router-link class="navbar-item" to="/description">Beschreibung</router-link>
      <router-link class="navbar-item" to="/center">Zentren</router-link>
      <router-link class="navbar-item" to="/consent">Patienteneinwilligungen</router-link>
      <router-link class="navbar-item" to="/firstrandomization">Erste Randomisierung Woche</router-link>
      <router-link class="navbar-item" to="/secondrandomization">Zweite Randomisierung Woche</router-link>
      <router-link class="navbar-item" to="/monitorplan">Monitorplan</router-link>
    </nav>
    <main>
      <router-view></router-view>
    </main>
    <hr/>
    <footer>
        <p>Studienmanagement und Software, Sommersemester 2019</p>
        <p>&copy; 2019-2020 FHDO Master MI Software zur Verwaltung der Mamphi-Studie.</p>
        <p>Developed and maintained by Beauclair Ngnintedem D.</p>
    </footer>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
  padding: 5px;
}
table {
    font-family: sans-serif;
    border-collapse: collapse;
}

td,
tr {
    border: 2px solid #dddddd;
    padding: 8px;
    text-align: center;
}

tr:nth-child(even) {
    background-color: aquamarine;
}

* {
    font-family: Arial, Helvetica, sans-serif;
}

body {
    margin: 5%;
}

.navbar {
    background-color: lightslategray;
    font-size: 1em;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    color: white;
    padding: 8px 5px 8px 5px;
}

.navbar a {
    text-decoration: none;
    color: inherit;
}

.navbar-brand {
    font-size: 1.2em;
    font-weight: 600;
}

.navbar-item {
    font-variant: small-caps;
    margin-left: 30px;
}

header>h1 {
    text-align: center;
}

.add-btn{
    cursor: pointer;
    background-color: aquamarine;
}

.add-btn:hover{
    opacity: 0.8;
}

#verwaltung {
    margin-top: 5%;
}

</style>
