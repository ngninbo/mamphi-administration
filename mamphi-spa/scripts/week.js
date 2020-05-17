let week = document.getElementById("week-btn");

week.addEventListener('click', function() {
    let body = document.getElementById("app");

    body.innerHTML = `<section>
    <div>
            <div class="navbar">
                <a href="#" class="navbar-item" id="rand-w1-btn">Randomisierungswoche 1</a>
                <a href="#" class="navbar-item" id="rand-w2-btn">Randomisierungswoche 2</a>
            </div>
        </div>`
});