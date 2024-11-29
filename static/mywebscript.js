let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create the data object for the POST request
    let data = {
        text: textToAnalyze
    };

    // Create an XMLHttpRequest for the POST request
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Display the response text in the system_response div
            document.getElementById("system_response").innerHTML = JSON.parse(this.responseText).response;
        } else if (this.readyState == 4 && this.status == 400) {
            // Display error message if no text is provided
            document.getElementById("system_response").innerHTML = "Error: No text provided!";
        }
    };

    // Open the POST request and set the correct headers
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Send the request with the JSON data
    xhttp.send(JSON.stringify(data));
}
