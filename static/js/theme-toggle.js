// static/js/main.js

// При завантаженні сторінки встановлюємо тему, зчитуючи значення з localStorage
document.addEventListener("DOMContentLoaded", function() {
  const currentTheme = localStorage.getItem('theme') || 'dark';
  document.body.className = 'theme-' + currentTheme;
});

// Функція для перемикання теми
function toggleTheme() {
  // Якщо поточна тема темна, перемикаємо на світлу, і навпаки
  const theme = document.body.classList.contains('theme-dark') ? 'light' : 'dark';
  document.body.className = 'theme-' + theme;
  localStorage.setItem('theme', theme);
}

function toggleFilter() {
    document.getElementById("filterSidebar").classList.toggle("open");
}
