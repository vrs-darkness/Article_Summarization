function Main()
{
    var URL = document.getElementById('url');
    var xhttp  = new XMLHttpRequest();
    alert("http://localhost:3000/Extract/" + URL.value);
    localStorage.setItem("URL" , URL.value)
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            alert('ok');
            document.getElementsByClassName("output")[0].style.display = 'block';
            document.getElementsByClassName("output")[0].innerHTML = 'hi';
        }
    };
    xhttp.open("GET", "http://localhost:3000/Extract/" + URL.value, true);
    xhttp.send(); 
}