// Script para mostrar detalles de una tarea usando una petición a la API

document.addEventListener('DOMContentLoaded', function() {
    const boton = document.getElementById('cargarDetallesBtn');
    const contenedor = document.getElementById('detallesApi');

    if (!boton || !contenedor) return; 

    boton.addEventListener('click', function() {
    if (!contenedor.classList.contains('oculto')) {
        contenedor.classList.add('oculto');
        contenedor.classList.remove('detallesApiVisible');
        return; // si está visible, ocultar y salir
    }

    const tareaId = boton.getAttribute('data-tarea-id');

        fetch(`/deustotil/api/tarea/${tareaId}/`)
            .then(response => {
                if (!response.ok) throw new Error('No se pudo cargar la tarea');
                return response.json();
            })
            .then(data => {
                contenedor.innerHTML = `
                    <p><strong>Descripción:</strong> ${data.descripcion}</p>
                    <p><strong>Fecha Inicio:</strong> ${data.fecha_inicio}</p>
                    <p><strong>Fecha Fin:</strong> ${data.fecha_fin}</p>
                    <p><strong>Prioridad:</strong> ${data.prioridad}</p>
                    <p><strong>Estado:</strong> ${data.estado}</p>
                `;
                contenedor.classList.remove('oculto');
                contenedor.classList.add('detallesApiVisible');
            })
            .catch(error => {
                contenedor.innerHTML = `<p class="error">Error al cargar datos: ${error.message}</p>`;
                contenedor.classList.remove('oculto');
                contenedor.classList.add('detallesApiVisible');
            });
    });
});





   