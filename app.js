fetch('./market.json')
.then(response => response.json())
.then(data => {

    document.getElementById("date").innerText = data.date;

    let html = `
    <div class="card">
        <h2>${data.condition}</h2>
    </div>
    `;

    data.markets.forEach(market => {

        html += `
        <div class="card">
            <h2>${market.name}</h2>
            <pre>${market.structure}</pre>
            <button onclick="copyText('${market.name}')">
            複製
            </button>
        </div>
        `;

    });

    document.getElementById("content").innerHTML = html;

})
.catch(error=>{
    document.getElementById("content").innerHTML =
    "<h2>資料載入失敗</h2>";
    console.log(error);
});


function copyText(text){
    navigator.clipboard.writeText(text);
    alert("已複製");
}
