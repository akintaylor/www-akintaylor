const copyEmailButton = document.getElementById("copy-email");

copyEmailButton.addEventListener("click", () => {
  let text = document.getElementById("email-address");
  text.select();
  text.setSelectionRange(0, 99999);
  document.execCommand("copy");
});
