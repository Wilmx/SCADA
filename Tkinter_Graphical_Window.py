import tkinter as tk
from tkinter import ttk

# Factores de conversión
CONVERSION_FACTORS = {
    'psi_to_kg_cm2': 14.22,
    'barrel_to_liters': 158.99,
    'm3_to_barrels': 6.29,
    'liters_to_m3': 1000,
}


def psi_to_kg_cm2(psi):
    return psi / CONVERSION_FACTORS['psi_to_kg_cm2']


def kg_cm2_to_psi(kg_cm2):
    return kg_cm2 * CONVERSION_FACTORS['psi_to_kg_cm2']


def barrels_to_liters(barrels):
    return barrels * CONVERSION_FACTORS['barrel_to_liters']


def liters_to_barrels(liters):
    return liters / CONVERSION_FACTORS['barrel_to_liters']


def liters_to_m3(liters):
    return liters / CONVERSION_FACTORS['liters_to_m3']


def m3_to_liters(m3):
    return m3 * CONVERSION_FACTORS['liters_to_m3']


def m3_to_barrels(m3):
    return m3 / CONVERSION_FACTORS['m3_to_barrels']


def barrels_to_m3(barrels):
    return barrels * CONVERSION_FACTORS['m3_to_barrels']


# Diccionario de funciones de conversión
conversion_functions = {
    'PSI a Kg/cm²': psi_to_kg_cm2,
    'Kg/cm² a PSI': kg_cm2_to_psi,
    'Barriles a Litros': barrels_to_liters,
    'Litros a Barriles': liters_to_barrels,
    'Litros a M³': liters_to_m3,
    'M³ a Litros': m3_to_liters,
    'M³ a Barriles': m3_to_barrels,
    'Barriles a M³': barrels_to_m3,
}


def perform_conversion():
    input_value = float(entry_value.get())
    conversion_type = combo_conversion.get()

    if conversion_type in conversion_functions:
        result = conversion_functions[conversion_type](input_value)
        label_result.config(text=f"Resultado: {result:.2f}")
    else:
        label_result.config(text="Seleccione un tipo de conversión")


# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("400x200")

# Crear widgets
label_instruction = ttk.Label(root, text="Ingrese el valor y seleccione el tipo de conversión:")
label_instruction.pack(pady=10)

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

combo_conversion = ttk.Combobox(root, values=list(conversion_functions.keys()))
combo_conversion.pack(pady=5)

button_convert = ttk.Button(root, text="Convertir", command=perform_conversion)
button_convert.pack(pady=5)

label_result = ttk.Label(root, text="Resultado:")
label_result.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()
