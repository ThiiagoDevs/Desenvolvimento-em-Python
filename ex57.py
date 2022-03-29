'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')
               ).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
