def jogar():
    print("==================================")
    print("===Bem-vindo ao jogo da forcar!===")
    print("==================================")

    palavra_secreta = "moreno".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

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

    if(acertou):
        print("Você ganhou!")

    else:
        print("Você perdeu!")
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
