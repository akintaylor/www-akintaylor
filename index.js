const copyEmailButton = document.getElementById("copy-email");

copyEmailButton.addEventListener("click", () => {
  let text = document.getElementById("email-address");
  alert(text.innerHTML);
});
