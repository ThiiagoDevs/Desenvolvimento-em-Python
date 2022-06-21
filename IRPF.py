# Cálculo do IRPF
rendimento_anual = float(input('Qual valor do seu rendimento bruto anual? '))
if rendimento_anual < 22847.77:
    aliquota = 0
elif (rendimento_anual >= 22847.77):
    if (rendimento_anual < 33919.81):
        aliquota = 7.5
    elif (rendimento_anual >= 33919.81):
        if (rendimento_anual < 45012.61):
            aliquota = 15.0
        elif (rendimento_anual >= 45012.61):
            if (rendimento_anual < 55976.16):
                aliquota = 22.5
            elif (rendimento_anual >= 55976.16):
                aliquota = 27.5
imposto_a_pagar = rendimento_anual * (aliquota / 100)
print('Sua aliquota é de %.2f%% e seu imposto a pagar, R$ %.2f' %
      (aliquota, imposto_a_pagar))
