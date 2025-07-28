# Conversor de Moeda

# Dados fornecidos
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibição dos resultados com duas casas decimais
print("Valor em Reais: R$ {:.2f}".format(valor_reais))
print("Convertido em Dólares: US$ {:.2f}".format(valor_dolar))
print("Convertido em Euros: € {:.2f}".format(valor_euro))
