const urlForm = document.getElementById('urlForm');
const urlInput = document.getElementById('urlInput');

function sendUrl(e) {
    const url = urlInput.value;
    e.preventDefault();

    fetch('http://localhost:5000/shorten', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url: url})
    })
    .then(res => res.json())
    .then(data => {
        console.log('Deu certo:', data)
        urlInput.value = data.shortenedURL;
    })
    .catch(error => {
        console.error('Deu erro:', error)
    })
} 

urlForm.addEventListener('submit', sendUrl);