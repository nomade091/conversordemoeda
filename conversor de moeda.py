# Taxas de câmbio atuais em relação ao Real
taxa_dolar = 4.93
taxa_euro = 5.36
taxa_iene = 0.033

try:
    # Obter o valor em reais da carteira
    real = float(input('Quanto dinheiro você tem na carteira? R$'))

    # Calcular as conversões
    dolar = real / taxa_dolar
    euro = real / taxa_euro
    iene = real / taxa_iene

    # Exibir os resultados
    print(f'Com R${real:.2f}, você pode comprar US${dolar:.2f}, €${euro:.2f} e JPY${iene:.2f} (iene).')

except ValueError:
    print('Por favor, insira um valor numérico válido.')
