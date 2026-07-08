fetch("./market.json")
.then(response => response.json())
.then(data => {

console.log(data);

document.getElementById("date").innerText = data.日期 || "每日市場更新";

let html = "";

// 狀態
html += `
<div class="card">
<h2>${data.狀態 || "AMRC Daily AI"}</h2>
</div>
`;


// 市場資料
data.市場.forEach(market => {

html += `
<div class="card">

<h2>${market.商品名 || "Market"}</h2>

<h3>📌 Market Structure</h3>
<p>${market.市場結構 || "資料更新中"}</p>


<h3>💧 Liquidity</h3>
<p>${market.流動性 || "資料更新中"}</p>


<h3>📊 Order Flow</h3>
<p>${market.訂單流 || "資料更新中"}</p>


<h3>🎯 Trading Plan</h3>
<p>${market.交易計畫 || "資料更新中"}</p>


<button onclick="copyText('${market.商品名}
${market.市場結構}
${market.流動性}
${market.訂單流}
${market.交易計畫}')">
複製分析
</button>

</div>
`;

});


document.getElementById("content").innerHTML = html;


})
.catch(error => {

console.error("資料錯誤:", error);

document.getElementById("content").innerHTML =
"<h3>資料載入失敗</h3>";

});


// 複製功能
function copyText(text){

navigator.clipboard.writeText(text);

alert("分析已複製");

}
