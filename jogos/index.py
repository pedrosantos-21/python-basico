print("=================================")
print("bem-vindo ao jogo da adivinhação!")
print("=================================")

total_de_tentativas = 3
numero_secreto = 7
rodada = 1

while (rodada <= total_de_tentativas):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero: "))
    print("Você digitou", chute)

    acertou = numero_secreto == chute
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print(
                "você errou! O seu chute foi  maior do que o numero secreto. ", end="\n")
        elif (menor):
            print("você errou! O seu chute foi menor do que o numero secreto. ")

    rodada = rodada + 1

print("Fim de jogo")
