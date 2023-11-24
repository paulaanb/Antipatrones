function guardarOperador(operador) {
    // Lógica para guardar el operador
    var inputNumbers = document.getElementById("inputNumbers");
    inputNumbers.value += operador;
}


function calcularResultado(resultado) {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;
    var resultadoFinal = eval(operacion);
    inputNumbers.value = resultadoFinal;
}

function calcularCuadrado() {
    var inputNumbers = document.getElementById("inputNumbers");
    var numero = parseFloat(inputNumbers.value);
    var resultado = numero * numero;
    inputNumbers.value = resultado;
}
function calcularCubo() {
    var inputNumbers = document.getElementById("inputNumbers");
    var numero = parseFloat(inputNumbers.value);
    var resultado = numero * numero * numero;
    inputNumbers.value = resultado;
}

function sumatorio() {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;
    var numeros = operacion.split(",");
    var suma = 0;
    for (var i = 0; i < numeros.length; i++) {
        suma += parseFloat(numeros[i]);
    }
    inputNumbers.value = suma;
}

function ordenar() {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;
    var numeros = operacion.split(",");
    var numerosOrdenados = numeros.sort(function (a, b) {
        return a - b;
    });
    var nuevaOperacion = numerosOrdenados.join(",");
    inputNumbers.value = nuevaOperacion;
}

function revertir() {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;
    var nuevaOperacion = operacion.split("").reverse().join("");
    inputNumbers.value = nuevaOperacion;
}

function quitar() {
    var inputNumbers = document.getElementById("inputNumbers");
    var operacion = inputNumbers.value;
    var nuevaOperacion = operacion.slice(0, -1);
    inputNumbers.value = nuevaOperacion;
}

function mod() {
    var inputNumbers = document.getElementById("inputNumbers");
    var numero = parseFloat(inputNumbers.value);
    var resultado = Math.abs(numero);
    inputNumbers.value = resultado;
}

function fact() {
    var inputNumbers = document.getElementById("inputNumbers");
    var numero = parseInt(inputNumbers.value);
    var resultado = 1;

    for (var i = 1; i <= numero; i++) {
        resultado *= i;
    }

    inputNumbers.value = resultado;
}