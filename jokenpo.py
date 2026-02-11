import random

def jokenpo():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha = random.choice(opcoes)
    print(f"Jo Ken Po! O computador escolheu: {escolha}")
    return escolha

if __name__ == "__main__":
    jokenpo()