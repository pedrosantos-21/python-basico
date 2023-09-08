import random
    
def jogar():

    boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto(True)
    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0  # posição
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Você errou, restam {} tentativas".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")

    else:
        print("Você perdeu!")
    print("Fim de jogo")

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def boas_vindas():
    print("==================================")
    print("===Bem-vindo ao jogo da forcar!===")
    print("==================================")

def carrega_palavra_secreta():
    arquivo = open("jogos\palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randint(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if (__name__ == "__main__"):
    jogar()