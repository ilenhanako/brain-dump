var msg = "hello";
var head = "hello world"

function run() {
  var p_elem = document.getElementById("msg1");
  var head_elem = document.getElementById("head");
  head_elem.innerText = head;
  p_elem.innerText = msg;
}
document.addEventListener("DOMContentLoaded", run);