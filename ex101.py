'''Exercício 101 – Funções para votação'''


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: a VOTAÇÃO É OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# programa principal
nasc = int(input('Ano de nascimento:'))
print(voto(nasc))
