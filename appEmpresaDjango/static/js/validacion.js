document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
    let errores = [];

    if (!form.querySelector('input[name="nombre"]')) return;
    
    const nombre = form.querySelector('input[name="nombre"]');
    if (nombre && nombre.value.trim() === '') {
      errores.push('El campo "Nombre" es obligatorio.');
    }

    const fechaInicio = form.querySelector('input[name="fecha_inicio"]');
    const fechaFin = form.querySelector('input[name="fecha_fin"]');

    if (fechaInicio && fechaFin && fechaInicio.value && fechaFin.value) {
      if (new Date(fechaFin.value) < new Date(fechaInicio.value)) {
        errores.push('La fecha fin no puede ser anterior a la fecha inicio.');
      }
    }

    if (errores.length > 0) {
      event.preventDefault();
      alert(errores.join('\n'));
    }
  });
});