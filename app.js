fetch("market.json")
.then(response => response.json())
.then(data => {


document.getElementById("date").innerHTML =
`
<h3>${data.date}</h3>
<p>${data.condition}</p>
`;



let html = "";


data.markets.forEach(market => {


html += `

<div class="card">

<h2>${market.name}</h2>


<h3>Market Structure</h3>
<p>${market.structure}</p>


<button onclick="copyText('${market.structure}')">
Copy Analysis
</button>


</div>

`;

});


document.getElementById("content").innerHTML = html;


})

.catch(error=>{

document.getElementById("content").innerHTML =
"資料載入失敗";

console.log(error);

});



function copyText(text){

navigator.clipboard.writeText(text);

alert("已複製");

}
