
document.getElementById("button").addEventListener("click", validate);
var b = document.getElementById("button");
var i = document.getElementsByClassName("input");

var form = document.getElementById('Form');

//for every element with id required, make sure not null/validate

//make this loop through and check each element with class:required or something like that
function validate() {
   var title = document.getElementById('title');
   var body = document.getElementById('body');

   if(!/\S/.test(title.value) && !/\S/.test(body.value)){
      title.classList.remove('shake');
      body.classList.remove('shake');
      void title.offsetWidth;
      void body.offsetWidth;
      title.classList.add('shake');
      body.classList.add('shake');
      console.log("Empty");
   }
   else if(!/\S/.test(title.value)){
      title.classList.remove('shake');
      void title.offsetWidth;
      title.classList.add('shake');
      console.log("Empty");
   }
   else if(!/\S/.test(body.value)){
      body.classList.remove('shake');
      void body.offsetWidth;
      body.classList.add('shake');
      console.log("Empty");
   }
   else{
      console.log("Filled");
      document.getElementById("form").submit();
   }
}

document.getElementById("title").addEventListener("focus", Nbrighten);
function Nbrighten(){
   var nb = document.getElementById('title_Text');
   nb.classList.remove('brighten');
   void nb.offsetWidth;
   nb.classList.add('brighten');
}

document.getElementById("body").addEventListener("focus", Ebrighten);
function Ebrighten(){
   var eb = document.getElementById('body_Text');
   eb.classList.remove('brighten');
   void eb.offsetWidth;
   eb.classList.add('brighten');
}  

document.getElementById("title").addEventListener("focusout", Ndim);
function Ndim(){
   var nd = document.getElementById('title_Text');
   nd.classList.remove('brighten');
}

document.getElementById("body").addEventListener("focusout", Edim);
function Edim(){
   var ed = document.getElementById('body_Text');
   ed.classList.remove('brighten');
}

