'''
digitar no terminal: pip install pillow
'''

import tkinter as tk
from PIL import Image, ImageTk

def mostrar_mapa(caminho_imagem):
    # Cria a janela do mapa
    janela = tk.Tk()
    janela.title("Mapa da Cidade - Seu RPG")
    
    # Carrega a imagem
    img = Image.open(caminho_imagem)
    
    # (Opcional) Redimensiona a imagem se ela for gigante (ex: 800x600)
    img = img.resize((800, 600)) 
    
    foto = ImageTk.PhotoImage(img)
    
    # Coloca a imagem dentro da janela
    label = tk.Label(janela, image=foto)
    label.pack()
    
    # Mantém a janela aberta até o jogador fechar no "X"
    janela.mainloop()

# --- EXEMPLO DE USO NO SEU JOGO ---
print("Você chegou aos portões da cidade de Eldoria!")
input("Pressione ENTER para abrir o mapa...")

# Troque pelo nome exato do seu arquivo de imagem
mostrar_mapa("mapa_cidade.jpg")

print("Você guardou o mapa na mochila. Para onde deseja ir agora?")
