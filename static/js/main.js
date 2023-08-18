/* Send the "get" request to the "hello api" by passing language as an argument */
document.getElementById('get-message').addEventListener('click', async() => {
    const selectedLanguage = document.getElementById('language').value;
    const response = await fetch(`http://localhost:5000/hello?language=${selectedLanguage}`);
    const data = await response.json();

    /* Displaying the message on the web page */
    document.getElementById('message').innerText = data.msgText;
});