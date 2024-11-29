let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Check if input is empty
    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = `<div class="alert alert-danger">Invalid input! Please provide text to be analyzed.</div>`;
        return; // Prevent further execution if input is empty
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            // Check if the response status is 200 (success)
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else {
                // If not 200, display the error message
                let errorResponse = JSON.parse(this.responseText); // Parse the JSON error response
                document.getElementById("system_response").innerHTML = `<div class="alert alert-danger">${errorResponse.error}</div>`;
            }
        }
    };

    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Send the text as JSON in the body of the request
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
};
