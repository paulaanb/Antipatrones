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

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(master=root)
    app.mainloop()