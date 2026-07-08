fetch("./market.json")
.then(response => response.json())
.then(data => {

console.log(data);


// 日期
document.getElementById("date").innerText =
data.日期 || data.date || "每日市場更新";


let html = "";


// 標題
html += `
<div class="card">
<h2>AMRC Daily AI 市場分析</h2>
<p>${data.狀態 || data.condition || "AI Generated"}</p>
</div>
`;


// 市場資料
const markets = data.市場 || data.markets || [];


markets.forEach(market => {


const name =
market.商品 ||
market.name ||
market.symbol ||
"XAUUSD";


const structure =
market.市場結構 ||
market.market_structure ||
"資料更新中";


const liquidity =
market.流動性 ||
market.liquidity ||
"資料更新中";


const orderFlow =
market.訂單流程 ||
market.order_flow ||
market.orderFlow ||
"資料更新中";


const plan =
market.交易計畫 ||
market.trading_plan ||
"資料更新中";


html += `

<div class="card">


<h2>${name}</h2>


<h3>📌 Market Structure</h3>
<p>${structure}</p>


<h3>💧 Liquidity</h3>
<p>${liquidity}</p>


<h3>📊 Order Flow</h3>
<p>${orderFlow}</p>


<h3>🎯 Trading Plan</h3>
<p>${plan}</p>


<button onclick="copyText(
\`${name}

Market Structure:
${structure}

Liquidity:
${liquidity}

Order Flow:
${orderFlow}

Trading Plan:
${plan}\`
)">
複製分析
</button>


</div>

`;

});


document.getElementById("content").innerHTML = html;


})
.catch(error => {

console.error("資料載入錯誤:", error);

document.getElementById("content").innerHTML =
"<h3>資料載入失敗</h3>";

});



function copyText(text){

navigator.clipboard.writeText(text);

alert("分析已複製");

}
