// Dark Mode Toggle
const toggleBtn = document.getElementById("darkModeToggle");
const toggleIcon = document.getElementById("toggleIcon");
const body = document.body;

toggleBtn.addEventListener("click", () => {
  body.classList.toggle("dark");
  body.classList.toggle("light");

  // Switch icon
  if (body.classList.contains("light")) {
    toggleIcon.classList.replace("bx-moon", "bx-sun");
  } else {
    toggleIcon.classList.replace("bx-sun", "bx-moon");
  }
});

const menuBtn = document.getElementById("menu");
const navLinks = document.getElementById("nav-links");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

const navItems = navLinks.querySelectorAll("a");
navItems.forEach(link => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("active");
  });
});

const contactHeroBtn = document.getElementById("contactHeroBtn");
const heroSocialLinks = document.getElementById("heroSocialLinks");

contactHeroBtn.addEventListener("click", () => {
  heroSocialLinks.classList.toggle("active");
  contactHeroBtn.textContent = heroSocialLinks.classList.contains("active")
    ? "Hide Contact Links"
    : "Contact Me";
});




