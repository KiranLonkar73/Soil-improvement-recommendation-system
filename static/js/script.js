document
.getElementById("soilForm")
.addEventListener("submit", function(e){

e.preventDefault();


let data = {

moisture:
document.getElementById("moisture").value,

nitrogen:
document.getElementById("nitrogen").value,

phosphorus:
document.getElementById("phosphorus").value,

potassium:
document.getElementById("potassium").value,

ph:
document.getElementById("ph").value,

rainfall:
document.getElementById("rainfall").value

};


fetch("/analyze", {

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})

.then(response=>response.json())

.then(result=>{

document.getElementById("result").innerHTML = `

<div class="result-item">💧 Water Recommendation:
${result.water}</div>

<div class="result-item">🌿 Nitrogen Status:
${result.nitrogen}</div>

<div class="result-item">🧪 Phosphorus Status:
${result.phosphorus}</div>

<div class="result-item">🌳 Potassium Status:
${result.potassium}</div>

<div class="result-item">⚖ Soil pH Status:
${result.ph}</div>

<div class="result-item health">
🌾 Soil Health Indicator:
${result.health}
</div>

`;

});

});