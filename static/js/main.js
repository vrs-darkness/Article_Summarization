function toggleSwitchChange() {
    let toggleSwitch = document.getElementById('toggleSwitch');
    let formUrl = document.getElementsByClassName('forms-url')[0];
    let formPara = document.getElementsByClassName('forms-para')[0];

    if (toggleSwitch.checked) {
        formUrl.style.display = 'none';
        formPara.style.display = 'block';
    } else {
        formPara.style.display = 'none';
        formUrl.style.display = 'block';
    }
}

function resizeInput(input) {
    input.style.height = 'auto'; // Reset height to auto to enable shrinking effect
    input.style.height = (input.scrollHeight) + 'px'; // Set height based on scrollHeight for vertical scaling
    input.style.width = 'auto'; // Reset width to auto to enable horizontal scaling
    input.style.width = (input.scrollWidth) + 'px'; // Set width based on scrollWidth for horizontal scaling
}

function showLoader() {
    document.getElementById('loader').style.display = 'block';
}