altura = float(input('Digite sua altura em metros: '))
peso = int(input('Digite seu peso em Kg: '))

def imc(p, a):
    imc_final = p / (a**2)
    return imc_final

resultado = imc(peso, altura)
print(f'Seu IMC é: {round(resultado, 2)}%')