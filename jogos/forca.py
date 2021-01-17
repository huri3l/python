from random import randrange

def jogar():

    mostrar_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas_restantes = 7

    while(not enforcou and not acertou):

        letra_informada = input("Informe uma letra: ").strip().upper()

        if(letra_informada in palavra_secreta):
            marca_letra_correta(letra_informada, letras_acertadas, palavra_secreta)
        else:
            tentativas_restantes -= 1
            desenha_forca(tentativas_restantes)

        enforcou = tentativas_restantes == 0
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print(f"Tentativas restantes: {tentativas_restantes}")

    imprime_mensagem_final(acertou, palavra_secreta)

def mostrar_mensagem_abertura():
    print("*" * 33)
    print("Bem vindo ao jogo de Forca!")
    print("*" * 33)

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    indice = randrange(0, len(palavras))
    palavra_secreta = palavras[indice].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def marca_letra_correta(letra_informada, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra_informada == letra):
            letras_acertadas[index] = letra

        index += 1

def imprime_mensagem_final(acertou, palavra_secreta):
    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(tentativas_restantes):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas_restantes == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas_restantes == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas_restantes == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()