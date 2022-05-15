'''Funções'''


'''def mensg(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensg('      SISTEMA DE ALUNOS   ')
mensg('   CADASTRO DE FUNCIONÁRIO   ')
mensg('       ERRO NO SISTEMA  ')'''


'''def mult(a, b):
    print(f'A = {a} e B = {b}')
    m = a * b
    print(f' A multiplicação de A * B = {m}')


# Programa principal
mult(b=4, a=6)
mult(2, 5)
mult(7, 3)'''


'''def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 2, 4)
contador(5, 8, 6, 4, 4)'''


'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for núm in valores:
        s += núm
    print(f'Somando os valores {valores} temos {s} ')


soma(2, 5)
soma(8, 8, 4, 5)
soma(9, 3, 6)
