// Scroll to section
function scrollToSection(id) {
  document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

// Contact form demo
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();
  const note = document.getElementById("formNote");

  if (!name || !email || !message) {
    note.innerText = "⚠️ Please fill in all fields.";
    note.style.color = "red";
    return;
  }

  note.innerText = "✅ Message ready to send! (Demo only)";
  note.style.color = "green";
  this.reset();
});

// Footer year
document.getElementById("year").textContent = new Date().getFullYear();
