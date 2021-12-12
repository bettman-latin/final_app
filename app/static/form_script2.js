
document.getElementById("button").addEventListener("click", validate);
var b = document.getElementById("button");
var i = document.getElementsByClassName("input");

var form = document.getElementById('Form');

//for every element with id required, make sure not null/validate

//make this loop through and check each element with class:required or something like that
function validate() {
   var username = document.getElementById('username');
   var password = document.getElementById('password');

   if(!/\S/.test(username.value) && !/\S/.test(password.value)){
      username.classList.remove('shake');
      password.classList.remove('shake');
      void username.offsetWidth;
      void password.offsetWidth;
      username.classList.add('shake');
      password.classList.add('shake');
      console.log("Empty");
   }
   else if(!/\S/.test(username.value)){
      username.classList.remove('shake');
      void username.offsetWidth;
      username.classList.add('shake');
      console.log("Empty");
   }
   else if(!/\S/.test(password.value)){
      password.classList.remove('shake');
      void password.offsetWidth;
      password.classList.add('shake');
      console.log("Empty");
   }
   else{
      console.log("Filled");
      document.getElementById("form").submit();
   }
}

document.getElementById("username").addEventListener("focus", Nbrighten);
function Nbrighten(){
   var nb = document.getElementById('username_Text');
   nb.classList.remove('brighten');
   void nb.offsetWidth;
   nb.classList.add('brighten');
}

document.getElementById("password").addEventListener("focus", Ebrighten);
function Ebrighten(){
   var eb = document.getElementById('password_Text');
   eb.classList.remove('brighten');
   void eb.offsetWidth;
   eb.classList.add('brighten');
}  

document.getElementById("username").addEventListener("focusout", Ndim);
function Ndim(){
   var nd = document.getElementById('username_Text');
   nd.classList.remove('brighten');
}

document.getElementById("password").addEventListener("focusout", Edim);
function Edim(){
   var ed = document.getElementById('password_Text');
   ed.classList.remove('brighten');
}

