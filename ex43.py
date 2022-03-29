'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status'''
peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal ')
elif 18.5 <= imc < 25:
    print('Parabens você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBSIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓBIDA, cuidado!')
