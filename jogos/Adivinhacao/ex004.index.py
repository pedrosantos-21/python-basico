import random

print("=================================")
print("bem-vindo ao jogo da adivinhação!")
print("=================================")

#inicialização das variáveis
total_de_tentativas = 0
numero_secreto = round(random.randint(1, 100))
pontos = 1000

print("Qual nível de dificuldade?",numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nivel para seu jogo: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#Laço de repetição
for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))

    #Definindo o chute
    chute = int(input("Digite um numero entre 1 a 30: "))
    print("Você digitou", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 a 30!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto

    if (acertou):
        print("Parabéns você acertou! sua pontuação final foi {} ".format(pontos))
        print("Fim de jogo")
        break
    elif (maior):
        print("você errou! O seu chute foi  maior do que o numero secreto. ", end="\n")
    else:
        print("você errou! O seu chute foi menor do que o numero secreto. ")
        
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

if not acertou:
    print("Fim de jogo. você não acertou! Sua pontuação final foi {}".format(pontos))
