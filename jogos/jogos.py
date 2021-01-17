import forca
import adivinhacao

print("*" * 33)
print("Escolha o seu jogo")
print("*" * 33)

print("(1) Forca (2) Adivinhação")

jogo = int(input("Informe o jogo: "))

if (jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()
else:
    print("Jogo desconhecido.")