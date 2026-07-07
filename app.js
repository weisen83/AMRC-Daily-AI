fetch("./market.json")
.then(response => response.json())
.then(data => {

    document.getElementById("date").innerText = data.date;

    let html = "";

    html += `
    <div class="card">
        <h2>${data.condition}</h2>
    </div>
    `;


    data.markets.forEach(market => {

        html += `
<div class="card">

<h2>${market.name}</h2>

<h3>📌 Market Structure</h3>
<p>${market.market_structure}</p>

<h3>💧 Liquidity</h3>
<p>${market.liquidity}</p>

<h3>📊 Order Flow</h3>
<p>${market.order_flow}</p>

<h3>🎯 Trading Plan</h3>
<p>${market.trading_plan}</p>

<button onclick="copyText(
\`${market.market_structure}

${market.liquidity}

${market.order_flow}

${market.trading_plan}\`
)">
複製分析
</button>

</div>
`;


    });


    document.getElementById("content").innerHTML = html;

})
.catch(error => {

    console.log(error);

    document.getElementById("content").innerHTML =
    "<h2>資料載入失敗</h2>";

});


function copyText(text){

navigator.clipboard.writeText(text);

alert("已複製");

}
