// Message duration
window.onload = function () {
    setTimeout(function () {
        let elements = document.getElementsByClassName('message-duration');
        for (let element of elements) {
            element.style.opacity = '0';
            element.style.transition = 'opacity 1s';

            setTimeout(function () {
                element.style.display = 'none';
            }, 1000);
        }
    }, 2500);
};
