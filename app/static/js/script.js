const form = document.getElementById('form');
const url = document.getElementById('long_url'); 
const production = 'https://short-url-dp9s.onrender.com/';
const development = 'http://127.0.0.1:8000/';
const apiUrl = window.location.hostname === "127.0.0.1" ? development : production;

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const longUrl = url.value;

    try {
        const res = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ long_url: longUrl })
        });

        const data = await res.json();

        if (res.ok) {
            console.log('URL Encurtada:', data.short_url);
            url.value =  data.short_url;
        } else {
            console.error('Erro:', data.message);
        }
    } catch (error) {
        console.error('Erro ao comunicar com o servidor:', error);
    }
});
