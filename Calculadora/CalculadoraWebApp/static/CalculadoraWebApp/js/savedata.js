function guardarOperacionEnDB() {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;

    // Enviar la operación al backend
    fetch('/guardar_operacion/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ operacion: operacion })
    })
    .then(response => {
        if (response.ok) {
            console.log('Operación guardada correctamente');
        } else {
            console.error('Error al guardar la operación');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}