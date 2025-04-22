import random 


#Desafio For
alunos = ['Andre', 'Bruno', 'Ana', 'Jessica']

for aluno in alunos:
    print('Bem vindos ao curso de Python,', aluno)

# Desafio While

numero_sorteado = random.randint(1, 10)
resposta = 0 

print('Tente adivinha o número de 1 a 10')
while resposta != numero_sorteado:
    resposta = int(input('Digite o número: '))
    if resposta == numero_sorteado:
        print('Parabéns, você ecertou o número! ', numero_sorteado)
    else:
        if resposta < numero_sorteado:
            print('Tente um número maior!')
        else:
            print('Tente um número menor!')