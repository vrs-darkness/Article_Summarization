document.addEventListener('DOMContentLoaded', function () {
    const dataContent = document.getElementById('dataContent').value;
    const lines = dataContent.split('\\n'); // Split data by "\n"
    const typingContentElement = document.getElementById('typing-content');
    const actionButtons = document.getElementById('actionButtons');
    
    let lineIndex = 0;
    let charIndex = 0;

    function typeLine() {
        if (lineIndex < lines.length) {
            const line = lines[lineIndex];
            if (charIndex < line.length) {
                typingContentElement.textContent += line.charAt(charIndex);
                charIndex++;
                setTimeout(typeLine, 5); // Delay between each character
            } else {
                typingContentElement.textContent += '\n'; // Add new line after the line is typed
                charIndex = 0;
                lineIndex++;
                setTimeout(typeLine, 300); // Delay between each line
            }
        } else {
            // Show the buttons after typing is complete
            actionButtons.style.display = 'block';
        }
    }

    typeLine(); // Start the typing effect

    // Copy to clipboard functionality
    const copyButton = document.getElementById('copyButton');
    copyButton.addEventListener('click', function () {
        const textToCopy = typingContentElement.textContent;
        navigator.clipboard.writeText(textToCopy).then(function () {
            alert('Summary copied to clipboard!');
        }).catch(function (error) {
            console.error('Failed to copy text: ', error);
        });
    });
});
