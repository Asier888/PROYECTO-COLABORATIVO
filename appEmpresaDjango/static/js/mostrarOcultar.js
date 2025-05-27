document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('toggleNotasBtn');
    const notas = document.getElementById('notas');

    btn.addEventListener('click', function() {
        if (notas.style.display === 'none') {
            notas.style.display = 'block';
            btn.textContent = 'Ocultar notas';
        } else {
            notas.style.display = 'none';
            btn.textContent = 'Mostrar notas';
        }
    });
});