const form = document.getElementById('form');
const url = document.getElementById('long_url');
form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const longUrl = url.value;

    try {
        const res = await fetch("http://localhost:5000/", {
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
