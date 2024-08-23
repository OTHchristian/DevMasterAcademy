function darkmode(){
    document.getElementById('Body').style.backgroundImage = 'url(darkbg.jpg)';
    document.getElementById('show').style.backgroundImage = 'url(darkbg.jpg)';
    document.getElementById('sun').style.fill = 'black';
    document.getElementById('a').style.fill = 'black';
    document.getElementById('b').style.fill = 'black';
    document.getElementById('c').style.fill = 'black';
    document.getElementById('d').style.fill = 'black';
}
 function lightmode(){
    document.getElementById('Body').style.backgroundImage = 'url(bg1.webp)';
    document.getElementById('show').style.backgroundImage = 'url(bg2.avif)';
    document.getElementById('sun').style.fill = 'blue';
    document.getElementById('a').style.fill = 'blue';
    document.getElementById('b').style.fill = 'blue';
    document.getElementById('c').style.fill = 'blue';
    document.getElementById('d').style.fill = 'blue';
 }
var toggle = document.getElementById('ToggleButton')
toggle.style.paddingLeft = '0px'
toggle.onclick = function(){
    if(toggle.style.paddingLeft == '0px'){
        toggle.style.paddingLeft = '37px';
        setTimeout(() => {
            darkmode();
        }, 800);
    }else{
        toggle.style.paddingLeft = '0'
        setTimeout(() => {
            lightmode();
        }, 800);
    }
}