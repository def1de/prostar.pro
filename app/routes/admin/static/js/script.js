const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    searchBtn = body.querySelector(".search-box");


sidebar.addEventListener("mouseover", () => {
    sidebar.classList.remove("close")
})

sidebar.addEventListener("mouseout", () => {
    sidebar.classList.add("close")
    adaptiveHome()
})

function adaptiveHome() {
    setTimeout(() => {
        document.querySelector('.home').style.width = document.querySelector('body').offsetWidth - document.querySelector('.sidebar').offsetWidth - 10 + 'px';
    }, 210);
}

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
})