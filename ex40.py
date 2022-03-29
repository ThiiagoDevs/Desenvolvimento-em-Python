''' Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {média}')
if média >= 5 and média < 7:
    print('O aluno esta em RECUPERAÇÂO.')
elif média < 5:
    print('O aluno esta REPROVADO')
elif média >= 7:
    print('O aluno esta APROVADO.')
