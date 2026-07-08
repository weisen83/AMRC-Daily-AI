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


    data【"市場"】.forEach(market => {

        html += `
<div class="card">

<h2>${market.【"商品名"】}</h2>

<h3>📌 Market Structure</h3>
<p>${market【"市場結構"】}</p>

<h3>💧 Liquidity</h3>
<p>${market【"流動性"】}</p>

<h3>📊 Order Flow</h3>
<p>${market【"訂單流"】}</p>

<h3>🎯 Trading Plan</h3>
<p>${market【"交易計畫"】}</p>

<button onclick="copyText(
\`${market【"市場結構"】}

${market【"流動性"】}

${market【"訂單流"】}

${market【"交易計畫"】}\`
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
