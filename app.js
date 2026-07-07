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

data.markets.forEach(market => {

html += `

<div class="card">

<h2>${market.name}</h2>

<h3>📊 Market Structure</h3>
<p>${market.structure}</p>


<h3>💧 Liquidity</h3>
<p>${market.liquidity || "Waiting AI Update"}</p>


<h3>🔥 Order Flow</h3>
<p>${market.orderflow || "Waiting AI Update"}</p>


<h3>🎯 Trading Plan</h3>
<p>${market.plan || "Waiting AI Update"}</p>


<button onclick="copyText('${market.structure}')">
Copy Report
</button>


</div>

`;

});


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
