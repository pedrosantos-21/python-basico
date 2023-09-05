def jogar():
    print("==================================")
    print("===Bem-vindo ao jogo da forcar!===")
    print("==================================")

    palavra_secreta = "moreno"
    
    enforcou = False
    acertou = False

    #enquanto(True) 
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0 #posição
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("encontrei a letra {} na posição {} " .format(chute, index))
            index += 1
        
        print("Jogando...")
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
