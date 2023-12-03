const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    adaptiveHome()
})

function adaptiveHome() {
    setTimeout(() => {
        document.querySelector('.home').style.width = document.querySelector('body').offsetWidth - document.querySelector('.sidebar').offsetWidth - 10 + 'px';
    }, 300);
}

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
})

// sidebar.addEventListener("mouseover", () => {
//     sidebar.classList.remove("close")
// })

// sidebar.addEventListener("mouseout", () => {
//     sidebar.classList.add("close")
//     adaptiveHome()
// })