document.body.style.padding = "0 100px";
document.body.style.marign = 0;

const navItemNames = ["첫 화면", "글 모음", "설명", "글 쓰기"]
const header = document.getElementById("header");

let ul = document.createElement("ul");
ul.id = "header-nav";
ul.style.display = "flex";
ul.style.justifyContent = "space-between";
ul.style.alignItems = "center";
ul.style.paddingLeft = 0;
ul.style.width = "50%";

for (let s of navItemNames){
let li = document.createElement("li");
li.innerText = s;
li.style.listStyle = "none";

li.addEventListener("mouseover", function(e){
  e.target.style.backgroundColor = "lightgray";
});

li.addEventListener("mouseleave", function(e){
  e.target.style.backgroundColor = "unset";
})

ul.appendChild(li);
}

header.appendChild(ul);

header.style.display = "flex";
header.style.justifyContent = "space-between";
header.style.padding = "0 20px";
