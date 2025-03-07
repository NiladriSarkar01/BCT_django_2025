const x=document.getElementById("para")


window.addEventListener("scroll", ()=>{
    let ofset=window.scrollY;
    x.style.backgroundPositionY=ofset*0.7+"px";
})