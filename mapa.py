from pathlib import Path
import tkinter as tk

from PIL import Image, ImageTk


MAPA_CIDADE = Path(__file__).with_name("Felltharia.jpg")
MAPA_FLORESTA = Path(__file__).with_name("Floresta_sombria.jpg")

LOCAIS = {
    "1": ("Castelo", "A fortaleza principal, cercada pelo fosso de água."),
    "2": ("Casa Comum", "A residência maior no bairro civil."),
    "3": ("Hotel", "O prédio grande de dois andares no centro da cidade."),
    "4": ("Torre do Mago", "A torre alta com runas brilhantes."),
    "5": ("Loja", "O comércio com toldos listrados."),
    "6": ("Guilda", "O pátio fortificado com área de treino."),
}


def mostrar_mapa(caminho_imagem):
    janela = tk.Tk()
    janela.title("Mapa de Felltharia")

    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((854, 480))
    foto = ImageTk.PhotoImage(imagem)

    label = tk.Label(janela, image=foto)
    label.pack()
    janela.mainloop()


def explorar_floresta():
    mostrar_mapa(MAPA_FLORESTA)

    while True:
        print("\nFloresta")
        print("[0] Voltar para Felltharia")
        print("[1] Torre de Vigia")
        print("[2] Casa da Bruxa")
        print("[3] Caverna dos Goblins")
        print("[4] Trilha Congelada")
        print("[m] Ver mapa")
        print("[s] Sair")
        escolha = input("Escolha: ").lower()

        if escolha == "0":
            return
        elif escolha == "m":
            mostrar_mapa(MAPA_FLORESTA)
        elif escolha == "s":
            return "exit"
        elif escolha == "1":
            print("\nTorre de Vigia:")
            print("Uma torre abandonada vigia os caminhos da floresta.")
        elif escolha == "2":
            print("\nCasa da Bruxa:")
            print("Uma casa antiga esconde mistérios entre as árvores.")
        elif escolha == "3":
            print("\nCaverna dos Goblins:")
            print("Ruídos ecoam pelas profundezas da caverna.")
        elif escolha == "4":
            print("\nTrilha Congelada:")
            print("Uma trilha coberta de gelo leva ainda mais fundo na floresta.")
        else:
            print("Opção inválida.")


def iniciar_jogo():
    if input("Deseja ver o mapa de Felltharia? (s/n): ").lower() == "s":
        mostrar_mapa(MAPA_CIDADE)

    while True:
        print("\nFelltharia")
        print("[0] Saída - ir para a Floresta")
        for numero, (nome, _) in LOCAIS.items():
            print(f"[{numero}] {nome}")
        print("[m] Ver mapa")
        print("[s] Sair")

        escolha = input("Escolha um lugar: ").lower()

        if escolha == "0":
            if explorar_floresta() == "exit":
                break
        elif escolha == "m":
            mostrar_mapa(MAPA_CIDADE)
        elif escolha == "s":
            break
        elif escolha in LOCAIS:
            nome, descricao = LOCAIS[escolha]
            print(f"\n{nome}: {descricao}")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    iniciar_jogo()
