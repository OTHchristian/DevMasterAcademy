document.getElementById('btn').onclick = function(){
    var formove = document.getElementById('forMove');
    var prp = document.getElementById('prpGood');
    if(formove.style.paddingLeft=='131px'){
        formove.style.paddingLeft='0';
        prp.style.backgroundColor='black';
        document.getElementById('btn').style.backgroundColor='white';
    }else{
        formove.style.paddingLeft='131px';
        prp.style.backgroundColor='white';
        document.getElementById('btn').style.backgroundColor='black';
    }
}