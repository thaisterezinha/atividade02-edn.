# Calculadora de Desconto

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do valor do desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("Produto:", nome_produto)
print("Preço Original: R$ {:.2f}".format(preco_original))
print("Desconto: {}% (R$ {:.2f})".format(porcentagem_desconto, valor_desconto))
print("Preço Final com Desconto: R$ {:.2f}".format(preco_final))
