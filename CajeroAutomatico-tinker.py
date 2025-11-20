
#     CLAVE DEL CAJERO = 1234

import tkinter as tk
from tkinter import messagebox

class CajeroAutomatico:
    def __init__(self, root):
        self.root = root
        self.root.title("Cajero Automático Mastercard")
        self.root.geometry("540x600")
        self.root.resizable(False, False)
        self.saldo = 1500000  # Saldo inicial 
        self.pin = "1234"
        self.intentos = 0
        self.max_intentos = 3
        self.estado = "bienvenida"
        self.historial = []
        self.recibo = ""
        self.sesion_iniciada = False  
        self.init_ui()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_saldo(self):
        if self.sesion_iniciada:
            saldo_frame = tk.Frame(self.root, bg="#232f34")
            saldo_frame.place(relx=0.5, rely=0.01, anchor="n", width=480, height=38)
            tk.Label(saldo_frame, text=f"💳 Saldo disponible: COP ${self.saldo:,.0f}",
                     font=("Segoe UI", 15, "bold"), fg="#f9aa33", bg="#232f34").pack(pady=4)

    def pantalla(self, titulo, mensaje):
        frame = tk.Frame(self.root, bg="#f5f6fa", bd=6, relief="ridge")
        frame.place(relx=0.5, rely=0.09, anchor="n", width=480, height=320)
        tk.Label(frame, text=titulo, font=("Segoe UI", 19, "bold"), fg="#d7263d", bg="#f5f6fa").pack(pady=16)
        tk.Label(frame, text=mensaje, font=("Segoe UI", 13), fg="#232f34", bg="#f5f6fa", wraplength=430, justify="center").pack(pady=8)
        return frame

    def botones(self, botones):
        btn_frame = tk.Frame(self.root, bg="#f5f6fa")
        btn_frame.place(relx=0.5, rely=0.74, anchor="n")
        columnas = 2  
        for i, (texto, comando) in enumerate(botones):
            row = i // columnas
            col = i % columnas
            tk.Button(btn_frame, text=texto, font=("Segoe UI", 13, "bold"), bg="#2e86ab", fg="white",
                      command=comando, width=20, height=2).grid(row=row, column=col, padx=10, pady=10)
        return btn_frame

    def init_ui(self):
        self.limpiar()
        self.mostrar_saldo()
        if self.estado == "bienvenida":
            self.pantalla_bienvenida()
        elif self.estado == "pin":
            self.pantalla_pin()
        elif self.estado == "menu":
            self.pantalla_menu()
        elif self.estado == "saldo":
            self.pantalla_saldo()
        elif self.estado == "retiro":
            self.pantalla_retiro()
        elif self.estado == "deposito":
            self.pantalla_deposito()
        elif self.estado == "cambiar_pin":
            self.pantalla_cambiar_pin()
        elif self.estado == "despedida":
            self.pantalla_despedida()
        elif self.estado == "bloqueado":
            self.pantalla_bloqueado()
        elif self.estado == "historial":
            self.pantalla_historial()
        elif self.estado == "recibo":
            self.pantalla_recibo()

    def pantalla_bienvenida(self):
        self.sesion_iniciada = False
        self.pantalla("Bienvenido al Cajero Mastercard",
                      "Inserte su tarjeta y presione INICIAR")
        self.botones([
            ("INICIAR", self.ir_pin),
            ("Salir", self.root.destroy)
        ])

    def ir_pin(self):
        self.estado = "pin"
        self.intentos = 0
        self.init_ui()

    def pantalla_pin(self):
        frame = self.pantalla("Ingrese su PIN",
                              "Digite su clave secreta (PIN) y pulse Entrar.\nIntentos permitidos: 3\n(PIN para el profe: 1234)")
        self.label_info = tk.Label(frame, text="", font=("Segoe UI", 11), fg="#d7263d", bg="#f5f6fa")
        self.label_info.pack(pady=6)
        self.entry_pin = tk.Entry(frame, show="*", font=("Segoe UI", 15), justify="center")
        self.entry_pin.pack(ipady=4, pady=10)
        self.entry_pin.focus_set()
        self.entry_pin.bind('<Return>', lambda e: self.validar_pin())
        self.botones([
            ("Entrar", self.validar_pin),
            ("Cancelar", self.ir_bienvenida)
        ])

    def validar_pin(self):
        valor = self.entry_pin.get()
        if valor == self.pin:
            self.estado = "menu"
            self.intentos = 0
            self.sesion_iniciada = True  # SESIÓN INICIADA
            self.init_ui()
        else:
            self.intentos += 1
            if self.intentos < self.max_intentos:
                self.label_info.config(
                    text=f"PIN incorrecto. Intentos restantes: {self.max_intentos - self.intentos}")
                self.entry_pin.delete(0, tk.END)
            else:
                self.estado = "bloqueado"
                self.init_ui()

    def ir_bienvenida(self):
        self.estado = "bienvenida"
        self.init_ui()

    def pantalla_menu(self):
        self.pantalla("Menú Principal",
                      "Seleccione la operación que desea realizar")
        self.botones([
            ("Consultar Saldo", self.ir_saldo),
            ("Retirar Dinero", self.ir_retiro),
            ("Depositar Dinero", self.ir_deposito),
            ("Cambiar PIN", self.ir_cambiar_pin),
            ("Historial", self.ir_historial),
            ("Recibo", self.ir_recibo),
            ("Finalizar", self.ir_despedida)
        ])

    def ir_saldo(self):
        self.estado = "saldo"
        self.init_ui()

    def pantalla_saldo(self):
        self.pantalla("Consulta de Saldo",
                      f"Su saldo disponible es:\nCOP ${self.saldo:,.0f}")
        self.recibo = f"Consulta de saldo: COP ${self.saldo:,.0f}"
        self.botones([
            ("Volver al menú", self.ir_menu),
            ("Recibo", self.ir_recibo)
        ])

    def ir_menu(self):
        self.estado = "menu"
        self.init_ui()

    def ir_retiro(self):
        self.estado = "retiro"
        self.init_ui()

    def pantalla_retiro(self):
        frame = self.pantalla("Retiro de Efectivo",
                          f"Digite el monto a retirar y presione Retirar\nSaldo actual: COP ${self.saldo:,.0f}")
        self.label_retiro = tk.Label(frame, text="", font=("Segoe UI", 11), fg="#d7263d", bg="#f5f6fa")
        self.label_retiro.pack(pady=5)
        self.entry_retiro = tk.Entry(frame, font=("Segoe UI", 15), justify="center")
        self.entry_retiro.pack(ipady=3, pady=8)
        self.entry_retiro.focus_set()

        def ejecutar_retiro(event=None):
            self.retirar_dinero()

        self.entry_retiro.bind('<Return>', ejecutar_retiro)
        self.botones([
            ("Retirar", ejecutar_retiro),  
            ("Cancelar", self.ir_menu)
        ])

    def retirar_dinero(self):
        try:
            entrada = self.entry_retiro.get().replace('.', '').replace(',', '')
            monto = int(entrada)
            if monto <= 0:
                self.label_retiro.config(text="Monto inválido. Ingrese un valor mayor a cero.")
            elif monto > self.saldo:
                self.label_retiro.config(text="Fondos insuficientes.")
            else:
                self.saldo -= monto
                self.historial.append(f"Retiro: COP ${monto:,.0f} | Saldo: COP ${self.saldo:,.0f}")
                self.recibo = f"Retiro: COP ${monto:,.0f}\nNuevo saldo: COP ${self.saldo:,.0f}"
                self.init_ui()
                messagebox.showinfo("Retiro exitoso", f"Retiró COP ${monto:,.0f}\nNuevo saldo: COP ${self.saldo:,.0f}")
        except:
            self.label_retiro.config(text="Ingrese un monto válido (puede usar punto o coma).")

    def ir_deposito(self):
        self.estado = "deposito"
        self.init_ui()

    def pantalla_deposito(self):
        frame = self.pantalla("Depósito de Efectivo",
                              f"Digite el monto a depositar y presione Depositar\nSaldo actual: COP ${self.saldo:,.0f}")
        self.label_deposito = tk.Label(frame, text="", font=("Segoe UI", 11), fg="#d7263d", bg="#f5f6fa")
        self.label_deposito.pack(pady=5)
        self.entry_deposito = tk.Entry(frame, font=("Segoe UI", 15), justify="center")
        self.entry_deposito.pack(ipady=3, pady=8)
        self.entry_deposito.focus_set()
        self.entry_deposito.bind('<Return>', lambda e: self.depositar_dinero())
        self.botones([
            ("Depositar", self.depositar_dinero),
            ("Cancelar", self.ir_menu)
        ])

    def depositar_dinero(self):
        try:
            entrada = self.entry_deposito.get().replace('.', '').replace(',', '')
            monto = int(entrada)
            if monto <= 0:
                self.label_deposito.config(text="Monto inválido. Ingrese un valor mayor a cero.")
            else:
                self.saldo += monto
                self.historial.append(f"Depósito: COP ${monto:,.0f} | Saldo: COP ${self.saldo:,.0f}")
                self.recibo = f"Depósito: COP ${monto:,.0f}\nNuevo saldo: COP ${self.saldo:,.0f}"
                self.init_ui()
                messagebox.showinfo("Depósito exitoso", f"Depositó COP ${monto:,.0f}\nNuevo saldo: COP ${self.saldo:,.0f}")
        except:
            self.label_deposito.config(text="Ingrese un monto válido (puede usar punto o coma).")

    def ir_cambiar_pin(self):
        self.estado = "cambiar_pin"
        self.init_ui()

    def pantalla_cambiar_pin(self):
        frame = self.pantalla("Cambio de PIN",
                              "Ingrese su PIN actual y el nuevo PIN (4 dígitos)")
        self.label_cpin = tk.Label(frame, text="", font=("Segoe UI", 11), fg="#d7263d", bg="#f5f6fa")
        self.label_cpin.pack(pady=5)
        self.entry_actual = tk.Entry(frame, show="*", font=("Segoe UI", 15), justify="center")
        self.entry_actual.pack(ipady=3, pady=5)
        self.entry_nuevo = tk.Entry(frame, show="*", font=("Segoe UI", 15), justify="center")
        self.entry_nuevo.pack(ipady=3, pady=5)
        self.entry_actual.focus_set()
        self.entry_nuevo.bind('<Return>', lambda e: self.cambiar_pin())
        self.botones([
            ("Cambiar PIN", self.cambiar_pin),
            ("Cancelar", self.ir_menu)
        ])

    def cambiar_pin(self):
        actual = self.entry_actual.get()
        nuevo = self.entry_nuevo.get()
        if actual != self.pin:
            self.label_cpin.config(text="PIN actual incorrecto.")
        elif not (nuevo.isdigit() and len(nuevo) == 4):
            self.label_cpin.config(text="El nuevo PIN debe tener 4 dígitos numéricos.")
        else:
            self.pin = nuevo
            self.recibo = f"Cambio de PIN exitoso.\nNuevo PIN: {nuevo}"
            messagebox.showinfo("PIN cambiado", "Su PIN fue cambiado exitosamente.")
            self.ir_menu()

    def ir_historial(self):
        self.estado = "historial"
        self.init_ui()

    def pantalla_historial(self):
        frame = self.pantalla("Historial de Operaciones", "")
        hist = self.historial[-10:] if self.historial else ["No hay movimientos aún."]
        for mov in reversed(hist):
            tk.Label(frame, text=mov, font=("Segoe UI", 11), fg="#232f34", bg="#f5f6fa").pack(anchor="w", padx=12)
        self.botones([
            ("Volver al menú", self.ir_menu)
        ])

    def ir_recibo(self):
        self.estado = "recibo"
        self.init_ui()

    def pantalla_recibo(self):
        frame = self.pantalla("Recibo Digital",
                              self.recibo if self.recibo else "No hay recibos disponibles.")
        self.botones([
            ("Volver al menú", self.ir_menu)
        ])

    def ir_despedida(self):
        self.sesion_iniciada = False  
        self.estado = "despedida"
        self.init_ui()

    def pantalla_despedida(self):
        self.pantalla("¡Gracias por usar Mastercard!",
                      "Retire su tarjeta y su dinero.\n¡Hasta pronto!")
        self.botones([
            ("Terminar", self.root.destroy)
        ])

    def pantalla_bloqueado(self):
        self.pantalla("Cajero bloqueado",
                      "Exceso de intentos de PIN\nPor favor, contacte a su banco.")
        self.botones([
            ("Salir", self.root.destroy)
        ])

if __name__ == "__main__":
    root = tk.Tk()
    app = CajeroAutomatico(root)
    root.mainloop()