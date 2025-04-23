frutas = ["Maçã", "Banana", "Pera", "Laranja"]

print(frutas[0:2])

#list compreension 
valor_inicial = [10, 20, 30, 40, 50]
desconto = 5
valor_final = [valor - desconto for valor in valor_inicial]
print(valor_final)