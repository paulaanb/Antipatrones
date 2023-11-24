 ## Antipatrones
El link de mi repositorio es el siguiente
https://github.com/paulaanb/Antipatrones

### Descripción del Ejercicio

Este ejercicio se centra en la identificación y corrección de un antipatrón de programación conocido como "Spaghetti Code".

#### Enunciado

Se parte del siguiente fragmento de código:

```python
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```

El propósito es reconocer las particularidades del antipatrón "Spaghetti Code" que están presentes en el código y llevar a cabo una refactorización con el fin de mejorar su claridad y facilidad de mantenimiento. Se busca eliminar la complejidad en las estructuras de control, modularizar el código y perfeccionar la gestión de posibles errores.

Rubrica:

## Identificación de Características de "Spaghetti Code" (20%)

### Función `calcular`

La función `calcular` presenta ciertas características que indican la presencia de "Spaghetti Code":

- **Control basado en cadenas**: El uso de cadenas (`'suma'`, `'resta'`, `'multiplicacion'`, `'division'`) para controlar el flujo del programa puede llevar a una lógica compleja y poco clara.

- **Lógica anidada y falta de modularización**: El manejo de diferentes operaciones se realiza a través de múltiples condicionales anidados (`if-else`), lo que dificulta la lectura y mantenimiento del código.

- **Manejo de errores sin excepciones**: La función maneja un caso de error (división por cero) mediante una impresión directa, lo cual puede no ser adecuado para un manejo robusto de errores. La falta de excepciones podría llevar a un control poco estructurado de casos excepcionales.

## Refactorización del Código (60%)

La refactorización tiene como objetivo mejorar la legibilidad y la estructura del código original.
Se busca una modularización adecuada, eliminando el control basado en cadenas y mejorando el manejo de errores.

```python
import tkinter as tk


class Sumar:
    @staticmethod
    def sumar(valor_anterior, valor_actual):
        return valor_anterior + valor_actual


class Restar:
    @staticmethod
    def restar(valor_anterior, valor_actual):
        return valor_anterior - valor_actual


class Multiplicar:
    @staticmethod
    def multiplicar(valor_anterior, valor_actual):
        return valor_anterior * valor_actual


class Dividir:
    @staticmethod
    def dividir(valor_anterior, valor_actual):
        if valor_actual != 0:
            return valor_anterior / valor_actual
        else:
            return "No se puede dividir entre cero"


class Calculadora(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculadora")
        self.pack()
        self.crear_widgets()
        self.operacion_actual = None
        self.valor_anterior = None
        self.limpiar_pantalla = False
        self.sumar = Sumar()
        self.restar = Restar()
        self.multiplicar = Multiplicar()
        self.dividir = Dividir()

    def agregar_numero(self, numero):
        entry_text = self.num_display.get()
        if self.limpiar_pantalla:
            self.num_display.set(numero)
            self.limpiar_pantalla = False
        else:
            if entry_text == "0" or entry_text.startswith("No se puede"):
                self.num_display.set(numero)
            else:
                self.num_display.set(entry_text + numero)

    def limpiar_display(self):
        self.num_display.set("0")

    def realizar_operacion(self, operacion):
        valor_actual = float(self.num_display.get())
        if self.valor_anterior is not None:
            if self.operacion_actual == '+':
                self.valor_anterior = self.sumar.sumar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '-':
                self.valor_anterior = self.restar.restar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '*':
                self.valor_anterior = self.multiplicar.multiplicar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '/':
                result = self.dividir.dividir(
                    self.valor_anterior, valor_actual)
                if isinstance(result, float):
                    self.valor_anterior = result
                else:
                    self.num_display.set(result)
                    return

        self.operacion_actual = operacion
        self.valor_anterior = float(self.num_display.get())
        self.limpiar_pantalla = True

    def calcular_resultado(self):
        if self.operacion_actual and self.valor_anterior is not None:
            valor_actual = float(self.num_display.get())
            if self.operacion_actual == '+':
                valor_actual = self.sumar.sumar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '-':
                valor_actual = self.restar.restar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '*':
                valor_actual = self.multiplicar.multiplicar(
                    self.valor_anterior, valor_actual)
            elif self.operacion_actual == '/':
                result = self.dividir.dividir(
                    self.valor_anterior, valor_actual)
                if isinstance(result, float):
                    valor_actual = result
                else:
                    self.num_display.set(result)
                    return

            self.num_display.set(str(valor_actual))
            self.valor_anterior = None
            self.operacion_actual = None
            self.limpiar_pantalla = True

    def crear_widgets(self):
        self.num_display = tk.StringVar()
        self.num_display.set("0")

        display_frame = tk.Frame(self)
        display_frame.pack()

        display_entry = tk.Entry(display_frame, textvariable=self.num_display, font=(
            "Arial", 12), state='disabled')
        display_entry.pack(side="left", padx=5, pady=5)

        num_buttons_frame = tk.Frame(self)
        num_buttons_frame.pack()

        buttons_layout = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '.', '0', 'C'
        ]

        for i, num in enumerate(buttons_layout):
            if num != 'C':
                button = tk.Button(num_buttons_frame, text=num, width=5, height=2, font=("Arial", 12),
                                   command=lambda n=num: self.agregar_numero(n))
            else:
                button = tk.Button(num_buttons_frame, text=num, width=5, height=2, font=("Arial", 12),
                                   command=self.limpiar_display)

            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

        operation_frame = tk.Frame(self)
        operation_frame.pack()

        operations = ['+', '-', '/', '=', '*']  # Reordenados
        for i, op in enumerate(operations):
            button = tk.Button(operation_frame, text=op, width=5, height=2, font=("Arial", 12),
                               command=lambda symbol=op: self.realizar_operacion(symbol) if symbol != '=' else self.calcular_resultado())
            button.grid(row=0, column=i, padx=5, pady=5)

        quit_frame = tk.Frame(self)
        quit_frame.pack()

        self.quit = tk.Button(quit_frame, text="QUIT", fg="red", font=("Arial", 12),
                              command=self.master.destroy)
        self.quit.pack(padx=5, pady=5)


root = tk.Tk()
app = Calculadora(master=root)
app.mainloop()
```

### Justificación de Cambios:

1. **Modularización y estructura clara:**
   - El código inicial se basaba en una función grande con múltiples sentencias condicionales, lo que dificultaba su mantenimiento y comprensión.
   - La refactorización separó las operaciones matemáticas en clases separadas (Sumar, Restar, Multiplicar, Dividir), lo que proporciona una estructura más modular y organizada.
   - La nueva versión implementa métodos estáticos para cada operación, facilitando su uso y comprensión.

2. **Eliminación del "Spaghetti Code":**
   - El código original presentaba características de "Spaghetti Code" al depender en gran medida de estructuras condicionales anidadas, lo que lo hacía difícil de entender y mantener.
   - La refactorización elimina este problema al dividir las operaciones en clases separadas, brindando una estructura más clara y manejable.

3. **Mejor manejo de errores:**
   - El código refactorizado maneja mejor los errores al dividir, evitando la división por cero y proporcionando mensajes claros en lugar de simplemente imprimir en la consola.

### Observaciones Finales:

La versión mejorada del código muestra una clara separación de responsabilidades, con operaciones matemáticas encapsuladas en clases individuales. Esto mejora significativamente la legibilidad, la mantenibilidad y la escalabilidad del código, reduciendo la complejidad y facilitando futuras extensiones o modificaciones.

Las clases separadas para cada operación permiten un enfoque más modular y organizado, facilitando la reutilización de código y promoviendo buenas prácticas de desarrollo.

El uso de una interfaz gráfica (GUI) para la calculadora mejora la experiencia del usuario al proporcionar una forma interactiva y visual de realizar cálculos, lo que hace que la aplicación sea más intuitiva y accesible.

### UMLS:

Convertimos el codigo proporcionado:


<img src="https://github.com/paulaanb/Antipatrones/blob/main/UML/UML_Inicial.png">

A un código mucho más optimizado y aplicando los principios SOLID:

<img src="https://github.com/paulaanb/Antipatrones/blob/main/UML/UML_Final.png">
