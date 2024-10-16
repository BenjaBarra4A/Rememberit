function updateSubZona() {
    const zonaSelect = document.querySelector('select[name="zona"]');
    const subZonaContainer = document.getElementById('subZonaContainer');
    const subZonaSelect = document.querySelector('select[name="ciudad"]');

    subZonaSelect.selectedIndex = 0;

    if (zonaSelect.value) {
        subZonaContainer.style.display = 'block';

        const subZonaOptions = {
            'Norte': [
                ['Arica', 'Arica'],
                ['Iquique', 'Iquique'],
                ['Antofagasta', 'Antofagasta'],
                ['Calama', 'Calama'],
                ['Copiapó', 'Copiapó'],
                ['La Serena', 'La Serena'],
                ['Coquimbo', 'Coquimbo'],
            ],
            'Centro': [
                ['Valparaíso', 'Valparaíso'],
                ['Santiago', 'Santiago'],
                ['Rancagua', 'Rancagua'],
                ['Talca', 'Talca'],
                ['Curicó', 'Curicó'],
                ['San Fernando', 'San Fernando'],
                ['Los Andes', 'Los Andes'],
                ['Quillota', 'Quillota'],
                ['Limache', 'Limache'],
                ['Viña del Mar', 'Viña del Mar'],
            ],
            'Sur': [
                ['Concepción', 'Concepción'],
                ['Talcahuano', 'Talcahuano'],
                ['Los Ángeles', 'Los Ángeles'],
                ['Temuco', 'Temuco'],
                ['Valdivia', 'Valdivia'],
                ['Osorno', 'Osorno'],
                ['Puerto Montt', 'Puerto Montt'],
                ['Coyhaique', 'Coyhaique'],
                ['Punta Arenas', 'Punta Arenas'],
                ['Castro', 'Castro'],
                ['Chillán', 'Chillán'],
            ]
        };

        subZonaSelect.innerHTML = '';
        const options = subZonaOptions[zonaSelect.value] || [];
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option[0];
            opt.textContent = option[1];
            subZonaSelect.appendChild(opt);
        });
    } else {
        subZonaContainer.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const zonaSelect = document.querySelector('select[name="zona"]');
    if (zonaSelect) {
        zonaSelect.addEventListener('change', updateSubZona);
    }
});