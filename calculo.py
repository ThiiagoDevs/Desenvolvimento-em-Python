print('Calculo de volume')
comprimento = float(
    input('Entre com comprimento em metros da caixa d\'água: '))
largura = float(input('Entre com a largura em metros da caixa d\'água: '))
profundidade = float(
    input('Entre com a profundidade em metros da caixa d\'água: '))
volume_em_mp3 = comprimento * largura * profundidade
volume_em_litros = volume_em_mp3 * 1000
print('A caixa d\'água comporta %.2f litros.' % volume_em_litros)
