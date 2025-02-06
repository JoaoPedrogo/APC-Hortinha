import customtkinter as ctk
from tkinter import messagebox

base_producao = {
    "Alface": 2.5,
    "Tomate": 6.0,
    "Manjericão": 1.5,
    "Cebolinha": 0.5,
    "Pimenta": 1.75
}

sol_ideal = {
    "Alface": 8,
    "Tomate": 7,
    "Manjericão": 8,
    "Cebolinha": 6,
    "Pimenta": 8
}

pancs = {
    "Ora-pro-nóbis": 1.2,
    "Taioba": 1.8,
    "Caruru": 0.7,
    "Beldroega": 0.9
}

pancsSol = {
    "Ora-pro-nóbis": 6,
    "Taioba": 5,
    "Caruru": 6,
    "Beldroega": 5
}

base_producao.update(pancs)
sol_ideal.update(pancsSol)

orientacoes = {
    "Horizontal": 1.0,
    "Vertical": 1.2
}

climas = {
    "Quente": 1.1,
    "Temperado": 1.0,
    "Frio": 0.9
}

def calcular_producao():
    try:
        planta = var_planta.get()
        horas_sol = float(entry_horas.get())
    
        if horas_sol > 12:
            messagebox.showerror("Erro", "O valor máximo permitido para horas de sol é 12h.")
            return

        area = float(entry_area.get())
        clima = var_clima.get()
        orient = var_orient.get()
        
        base = base_producao[planta]
        ideal = sol_ideal[planta]
        sol_mult = horas_sol / ideal
        
        clima_factor = climas[clima]
        orient_factor = orientacoes[orient]
        
        producao = base * area * sol_mult * clima_factor * orient_factor
        
        resultado = (
            f"PREVISÃO DE COLHEITA PARA {planta.upper()}\n\n"
            f"• Planta: {planta}\n"
            f"• Horas de sol/dia: {horas_sol}h (ideal: {ideal}h)\n"
            f"• Área cultivada: {area} m²\n"
            f"• Clima: {clima}\n"
            f"• Orientação: {orient}\n\n"
            f"Produção total estimada: {producao:.1f} kg"
        )
        label_resultado.configure(text=resultado)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos para horas de sol e área.")

def mostrar_dados():
    dados_formatados = "Planta\tProdução Base (kg/m²)\tHoras Ideais (h)\n"
    for planta in base_producao.keys():
        producao_base = base_producao[planta]
        horas_ideais = sol_ideal[planta]
        dados_formatados += f"{planta}\t{producao_base}\t{horas_ideais}\n"
    label_dados.config(text=dados_formatados)


janela = ctk.CTk()
janela.title("Hortinha")
janela.geometry("500x500")
janela.resizable(False, False)

label_titulo = ctk.CTkLabel(janela, text="Hortinha", font=("Arial", 16))
label_titulo.pack(pady=10)

frame_inputs = ctk.CTkFrame(janela)
frame_inputs.pack(pady=5)

frame_planta = ctk.CTkFrame(frame_inputs)
frame_planta.pack(pady=5)
ctk.CTkLabel(frame_planta, text="Escolha sua planta:", font=("Arial", 12)).pack(side=ctk.LEFT, padx=5)
var_planta = ctk.StringVar(value="Alface")
menu_planta = ctk.CTkOptionMenu(frame_planta, variable=var_planta, values=list(base_producao.keys()))
menu_planta.pack(side=ctk.LEFT)

frame_horas = ctk.CTkFrame(frame_inputs)
frame_horas.pack(pady=5)
ctk.CTkLabel(frame_horas, text="Horas de sol/dia:", font=("Arial", 12)).pack(side=ctk.LEFT, padx=5)
entry_horas = ctk.CTkEntry(frame_horas, width=100)
entry_horas.pack(side=ctk.LEFT)

frame_area = ctk.CTkFrame(frame_inputs)
frame_area.pack(pady=5)
ctk.CTkLabel(frame_area, text="Área (m²):", font=("Arial", 12)).pack(side=ctk.LEFT, padx=5)
entry_area = ctk.CTkEntry(frame_area, width=100)
entry_area.pack(side=ctk.LEFT)

frame_clima = ctk.CTkFrame(frame_inputs)
frame_clima.pack(pady=5)
ctk.CTkLabel(frame_clima, text="Clima da região:", font=("Arial", 12)).pack(side=ctk.LEFT, padx=5)
var_clima = ctk.StringVar(value="Temperado")
menu_clima = ctk.CTkOptionMenu(frame_clima, variable=var_clima, values=list(climas.keys()))
menu_clima.pack(side=ctk.LEFT)

frame_orient = ctk.CTkFrame(frame_inputs)
frame_orient.pack(pady=5)
ctk.CTkLabel(frame_orient, text="Orientação da horta:", font=("Arial", 12)).pack(side=ctk.LEFT, padx=5)
var_orient = ctk.StringVar(value="Horizontal")
menu_orient = ctk.CTkOptionMenu(frame_orient, variable=var_orient, values=list(orientacoes.keys()))
menu_orient.pack(side=ctk.LEFT)

botao_calcular = ctk.CTkButton(janela, text="Calcular Produção", font=("Arial", 12), command=calcular_producao)
botao_calcular.pack(pady=20)

label_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 12), justify=ctk.LEFT)
label_resultado.pack(pady=10)


label_dados = ctk.CTkLabel(janela, text="", font=("Arial", 10), justify=ctk.LEFT)
label_dados.pack(pady=10)

janela.mainloop()