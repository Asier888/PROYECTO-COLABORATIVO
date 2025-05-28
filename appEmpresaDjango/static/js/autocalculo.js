// Script que calcula la fecha de finalización automáticamente 
// basado en la fecha de inicio y una duración en días.

window.onload = function () {
    var fechaInicioInput = document.getElementsByName('fecha_inicio')[0];
    var duracionInput = document.getElementsByName('duracion')[0];
    var fechaFinInput = document.getElementsByName('fecha_fin')[0];

    function calcularFechaFin() {
        var fechaInicio = fechaInicioInput.value; 
        var duracion = duracionInput.value;

        if (fechaInicio !== '' && duracion !== '') {
            var partes = fechaInicio.split('-');
            var año = parseInt(partes[0]);
            var mes = parseInt(partes[1]);
            var dia = parseInt(partes[2]);

            var diasDuracion = parseInt(duracion);
            if (isNaN(diasDuracion)) return;

            dia = dia + diasDuracion;
            while (dia > 30) {
                dia = dia - 30;
                mes = mes + 1;
                if (mes > 12) {
                    mes = 1;
                    año = año + 1;
                }
            }
            if (mes < 10) {
                mes = '0' + mes;
            }
            if (dia < 10) {
                dia = '0' + dia;
            }

            fechaFinInput.value = año + '-' + mes + '-' + dia;
        }
    }

    fechaInicioInput.onchange = calcularFechaFin;
    duracionInput.oninput = calcularFechaFin;
};
