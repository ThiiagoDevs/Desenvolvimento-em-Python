resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    n = int(input(' Digite im número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer cintinuar? S/N: ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {n} número e a média foi {média}')
print(f'O maior valor foi {n} e o menor foi {n}')
