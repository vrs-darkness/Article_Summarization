async function summarize() {
    let url = document.getElementById('url').value;

    url = encodeURIComponent(url);
    try {
        let response = await fetch("http://127.0.0.1:5000/get", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "data": url
            })
        });

        if (response.ok) {
            let data = await response.json();
            console.log(data);
        } else {
            console.error('Request failed with status:', response.status);
        }
    } catch (error) {
        console.error('Network error occurred:', error);
    }
}
