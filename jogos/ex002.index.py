print("=================================")
print("bem-vindo ao jogo da adivinhação!")
print("=================================")

total_de_tentativas = 3
numero_secreto = 7

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero: "))
    print("Você digitou", chute)

    acertou = numero_secreto == chute
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print(
                "você errou! O seu chute foi  maior do que o numero secreto. ", end="\n")
        elif (menor):
            print("você errou! O seu chute foi menor do que o numero secreto. ")

print("Fim de jogo")
