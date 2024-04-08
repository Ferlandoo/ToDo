window.onload = function () {
    setTimeout(function () {
        let element = document.getElementById('message-duration');
        element.style.opacity = '0';
        element.style.transition = 'opacity 1s';

        setTimeout(function () {
            element.style.display = 'none';
        }, 1000);
    }, 2500);
};
