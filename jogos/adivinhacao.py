from random import randrange

def jogar():
    print("*" * 33)
    print("Bem vindo ao jogo de Adivinhação!")
    print("*" * 33)

    numero_secreto = randrange(0, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        numero_informado = int(input("Informe um número entre 1 e 100: "))
        print("O valor digitado foi: {}".format(numero_informado))

        if (numero_informado < 1 or numero_informado > 100):
            print("Você deve digitar um número entre 1 e 100!")
            print("-=" * 25)
            continue

        acertou = numero_informado == numero_secreto
        maior = numero_informado > numero_secreto
        menor = numero_informado < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos}!")
            break
        else:
            print("Você errou.")

            if (maior):
                print("O número informado é maior do que o número secreto.")
            elif (menor):
                print("O número informado é menor do que o número secreto.")

            pontos_perdidos = abs(numero_secreto - numero_informado)
            pontos = pontos - pontos_perdidos

        print("-=" * 25)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()