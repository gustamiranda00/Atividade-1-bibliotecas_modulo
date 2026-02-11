import random

def megasena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    print("Números da Mega-Sena:")
    print(f"{numeros[0]} - {numeros[1]} - {numeros[2]} - {numeros[3]} - {numeros[4]} - {numeros[5]}")
    return numeros

if __name__ == "__main__":
    megasena()