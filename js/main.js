//moedog-hitokoto-API
var xhr = new XMLHttpRequest();
xhr.open('get', 'https://api.moedog.org/hitokoto/?encode=json');
xhr.onreadystatechange = function () {
    var data = JSON.parse(xhr.responseText);
    var hitokoto = document.getElementById('hitokoto');
    hitokoto.innerText = data.hitokoto;
}
xhr.send();
