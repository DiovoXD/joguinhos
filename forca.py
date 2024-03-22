import random



def desenhar_bonequinho(tentativas): 
    if tentativas == 0:
        print("  ____")
        print(" |    |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    elif tentativas == 1:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |")
        print(" |")
        print("_|__")
    elif tentativas == 2:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |")
        print("_|__")
    elif tentativas == 3:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|")
        print(" |")
        print("_|__")
    elif tentativas == 4:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |")
        print("_|__")
    elif tentativas == 5:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   /")
        print("_|__")
    else:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   / \\")
        print("_|__")

def forca():
    palavras = ["cachorro", "gatinho", "abacate", "python", "computador", "bomboclat", "musica"]

    palavra_escolhida = random.choice(palavras)
    letras_reveladas = ['_'] * len(palavra_escolhida) 

    print("palavra selecionada:", ''.join(letras_reveladas))
    
    tentativas = 0
    max_tentativas = 6

    while tentativas < max_tentativas:
        letra = input("digite uma letra: ")

        if letra in palavra_escolhida:
            print("letra encontrada na palavra! :D")
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    letras_reveladas[i] = letra
        else:
            print("Letra não encontrada na palavra :(")
            tentativas += 1
            desenhar_bonequinho(tentativas)
        
        print("Palavra:", ''.join(letras_reveladas))
        
        if '_' not in letras_reveladas:
            break
    
    if tentativas == max_tentativas:
        print("Voce perdeu :( a palavra era: ", palavra_escolhida)
    
    else:
        print("VOCE GANHOU!!! YYYIIIPEEE!!!! :D")

jogar_novamente = True
while jogar_novamente:
    forca()
    resposta = input("Deseja jogar novamente? (sim/nao): ").lower()
    if resposta != "sim":
        jogar_novamente = False