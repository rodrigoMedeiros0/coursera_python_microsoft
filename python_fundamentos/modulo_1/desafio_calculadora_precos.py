preco = 75
desconto = 15

desconto_aplicado = preco * (desconto / 100)

preco_final = preco - desconto_aplicado

print(f"O preço final do produto, após aplicar o desconto de {desconto}%, é R$ {preco_final:.2f}")