import random

def moeda():
    while True:
        cara_coroa =["cara", "coroa"]

        jogar_moeda = random.choice(cara_coroa)
        resposta = input("Voce escolhe cara ou coroa? ")
        if resposta == jogar_moeda:
            print ("Voce ganhou! a moeda caiu em", jogar_moeda)

        else:
            print("voce errou! a moeda caiu em", jogar_moeda)
    
        jogar_dnv = input("jogar a moeda de novo? (sim/não): ")
        if jogar_dnv.lower() != ("sim"):
            break

moeda()
