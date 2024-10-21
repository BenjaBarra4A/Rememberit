document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('theme-toggle');

    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('dark-mode');
        if (toggle) {
            toggle.checked = true;
        }
    }

    if (toggle) {
        toggle.addEventListener('change', () => {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('dark-mode', 'enabled');
            } else {
                localStorage.setItem('dark-mode', 'disabled');
            }
        });
    }
});
