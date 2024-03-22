import random

def Jogo_de_Adivinhação():
    while True:  
        numero_secreto = random.randint(1, 100)
        tentativas = 0
        max_tentativas = 10

        print("Bem-vindo ao Jogo de Adivinhação :D")
        print("Tente adivinhar o número entre 1 e 100 :)")

        while tentativas < max_tentativas:
            tentativa = int(input("Digite sua tentativa: "))
            tentativas += 1

            if tentativa == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas! O número secreto era {numero_secreto} :D")
                break
            elif tentativa < numero_secreto:
                print("O número é maior. Tente Novamente :)")
            else:
                print("O número é menor. Tente Novamente :)")

        if tentativas == max_tentativas:
            print(f"Suas {max_tentativas} tentativas acabaram. O número secreto era {numero_secreto} :(")

        jogar_novamente = input("Deseja jogar novamente? (sim/não): ")
        if jogar_novamente.lower() != "sim":
            break  


Jogo_de_Adivinhação()
