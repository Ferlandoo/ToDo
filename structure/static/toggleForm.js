document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('sign-up-form').addEventListener('click', function () {
        var sign_in = document.getElementById('sign-in');
        var sign_up = document.getElementById('sign-up');

        sign_in.classList.add('hidden');
        sign_up.classList.remove('hidden');
    });

    document.getElementById('sign-in-form').addEventListener('click', function () {
        var sign_in = document.getElementById('sign-in');
        var sign_up = document.getElementById('sign-up');

        sign_in.classList.remove('hidden');
        sign_up.classList.add('hidden');
    });
});
