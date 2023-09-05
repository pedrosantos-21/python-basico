import random

print("=================================")
print("bem-vindo ao jogo da adivinhação!")
print("=================================")

total_de_tentativas = 3
numero_secreto = round(random.randint(1,30))

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero entre 1 a 30: "))
    print("Você digitou", chute)

    if(chute < 1 or chute > 30):
        print("Você deve digitar um numero entre 1 a 30!")
        continue 

    acertou = numero_secreto == chute
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    elif(maior):
        print("você errou! O seu chute foi  maior do que o numero secreto. ", end="\n")
    else:
        print("você errou! O seu chute foi menor do que o numero secreto. ")

print("Fim de jogo")
