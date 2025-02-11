
document.addEventListener("DOMContentLoaded", function() {
  const currentTheme = localStorage.getItem('theme') || 'dark';
  document.body.className = 'theme-' + currentTheme;
});

function toggleTheme() {
  const theme = document.body.classList.contains('theme-dark') ? 'light' : 'dark';
  document.body.className = 'theme-' + theme;
  localStorage.setItem('theme', theme);
}

function toggleFilter() {
    document.getElementById("filterSidebar").classList.toggle("open");
}
//
// const input = document.getElementById("input");
// input.addEventListener(("click"), ()=>{
//   input.value = "das";
//   input.style.backgroundColor = "black"
// })
