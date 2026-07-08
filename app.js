fetch("./market.json")
.then(response => response.json())
.then(data => {

console.log(data);

document.getElementById("content").innerHTML =
`
<div class="card">
<h2>${data.condition}</h2>
</div>
`;

});
