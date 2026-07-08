fetch("./market.json")
.then(response => response.json())
.then(data => {

document.getElementById("date").innerText = data.日期;

let html = "";

data.市場.forEach(market => {

html += `
<div class="card">

<h2>${market.商品名}</h2>

<h3>📌 市場結構</h3>
<p>${market.市場結構}</p>

<h3>💧 流動性</h3>
<p>${market.流動性}</p>

<h3>📊 Order Flow</h3>
<p>${market.訂單流}</p>

<h3>🎯 交易計畫</h3>
<p>${market.交易計畫}</p>

</div>
`;

});


document.getElementById("content").innerHTML = html;

});
