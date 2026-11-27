import time
import tkinter as tk

from PIL import Image, ImageTk


MAPA_CIDADE = "Felltharia.jpg"
MAPA_FLORESTA = "Floresta Sombria.jpg"
MAPA_FROSTHELL = "FrostHell.jpg"
IMAGEM_CASTELO_CONGELADO = "Castelo Congelado.jpg"


nome = input("Qual é o nome do personagem? ")


def mostrar_mapa(arquivo, titulo):
    janela = tk.Tk()
    janela.title(titulo)

    imagem = Image.open(arquivo)
    imagem = imagem.resize((854, 480))
    foto = ImageTk.PhotoImage(imagem)

    label = tk.Label(janela, image=foto)
    label.pack()
    janela.mainloop()


def explorar_frosthell():
    mostrar_mapa(MAPA_FROSTHELL, "Mapa de FrostHell")

    while True:
        print("\nFrostHell")
        print("[0] Voltar para a Floresta Sombria")
        print("[1] Castelo Congelado")
        print("[2] Taverna dos Esqueletos")
        print("[3] Esconderijo de Gelo")
        print("[4] Poço dos Mortos")
        print("[m] Ver mapa")
        print("[s] Sair")

        escolha = input("Escolha: ").lower()

        if escolha == "0":
            return False
        elif escolha == "1":
            texto = f"""
{nome}, você encaixa a Chave de Ossos Gelados e abre a porta. A grande porta vai para trás
e bate com força nas grandes paredes de gelo, e logo todo o seu interior é revelado.
Existem grandes colunas feitas de gelo com ossos entrelaçados e congelados.
Todo o castelo é feito desse gelo e de ossos juntos e mesclados, e tudo o que você
vê parece mentira. O corredor está cercado por muitos guardas esqueletos, e lá no centro
está o que você buscava desde o começo: o Rei Caveira Gelado, sentado em seu trono,
esperando por você.
"""
            print("\nPressione Enter para pular ou digite L para ver a descrição.")
            escolha = input("Escolha: ").lower()

            if escolha == "l":
                for letra in texto:
                    print(letra, end="", flush=True)
                    time.sleep(0.08)
                print()
                time.sleep(5)

            mostrar_mapa(IMAGEM_CASTELO_CONGELADO, "Castelo Congelado")
        elif escolha == "2":
            print("\nTaverna dos Esqueletos")
        elif escolha == "3":
            print("\nEsconderijo de Gelo")
        elif escolha == "4":
            print("\nPoço dos Mortos")
        elif escolha == "m":
            mostrar_mapa(MAPA_FROSTHELL, "Mapa de FrostHell")
        elif escolha == "s":
            return True
        else:
            print("Opção inválida.")


def explorar_floresta():
    mostrar_mapa(MAPA_FLORESTA, "Mapa da Floresta Sombria")

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
            return False
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
            if explorar_frosthell():
                return True
        elif escolha == "m":
            mostrar_mapa(MAPA_FLORESTA, "Mapa da Floresta Sombria")
        elif escolha == "s":
            return True
        else:
            print("Opção inválida.")


if input("Deseja ver o mapa de Felltharia? (s/n): ").lower() == "s":
    mostrar_mapa(MAPA_CIDADE, "Mapa de Felltharia")

while True:
    print("\nFelltharia")
    print("[0] Saída - ir para a Floresta")
    print("[1] Castelo")
    print("[2] Casa Comum")
    print("[3] Hotel")
    print("[4] Torre do Mago")
    print("[5] Loja")
    print("[6] Guilda")
    print("[m] Ver mapa")
    print("[s] Sair")

    escolha = input("Escolha um lugar: ").lower()

    if escolha == "0":
        if explorar_floresta():
            break
    elif escolha == "1":
        print("\nCastelo: A fortaleza principal, cercada pelo fosso de água.")
    elif escolha == "2":
        print("\nCasa Comum: A residência maior no bairro civil.")
    elif escolha == "3":
        print("\nHotel: O prédio grande de dois andares no centro da cidade.")
    elif escolha == "4":
        print("\nTorre do Mago: A torre alta com runas brilhantes.")
    elif escolha == "5":
        print("\nLoja: O comércio com toldos listrados.")
    elif escolha == "6":
        print("\nGuilda: O pátio fortificado com área de treino.")
    elif escolha == "m":
        mostrar_mapa(MAPA_CIDADE, "Mapa de Felltharia")
    elif escolha == "s":
        break
    else:
        print("Opção inválida.")