/* IKIGAI CLICK */
function showInfo(type){

let text = "";

if(type==="passion"){
text="What you love doing.";
}
else if(type==="skills"){
text="What you are good at.";
}
else if(type==="income"){
text="What you can earn from.";
}
else{
text="How you help the world.";
}

document.getElementById("ikigai-info").innerHTML = `<p>${text}</p>`;
}


/* RESULT LOGIC */
let data = JSON.parse(localStorage.getItem("quizData"));

if(data){

document.getElementById("user").innerText="Hello "+data.name;

let c = data.confidence;

document.getElementById("fill").style.width=(c*10)+"%";

document.getElementById("confidenceText").innerText=
c<4?"Low":c<7?"Medium":"High";

let career="",skills="";

if(data.interest==="Technology"){
career="Software Developer";
skills="Coding, Logic";
}
else if(data.interest==="Business"){
career="Entrepreneur";
skills="Finance, Marketing";
}
else if(data.interest==="Helping People"){
career="Teacher";
skills="Communication";
}
else{
career="Designer";
skills="Creativity";
}

careerEl=document.getElementById("career");
skillsEl=document.getElementById("skills");
adviceEl=document.getElementById("advice");

if(careerEl) careerEl.innerText=career;
if(skillsEl) skillsEl.innerText=skills;
if(adviceEl) adviceEl.innerText=
c<4?"Explore more":
c<7?"Build skills":
"You're ready!";
}