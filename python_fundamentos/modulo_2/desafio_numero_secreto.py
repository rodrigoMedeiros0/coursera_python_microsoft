# Intruções: Você criará um jogo de adivinhação de números em que o computador tentará adivinhar um número secreto que você definiu. O computador gerará suposições aleatórias dentro de um intervalo (1 a 10) e continuará adivinhando até encontrar o número correto.
import random 


secret_number = random.randint(1, 10) 
guess = 0
guessed = False

print("----------------------------------------------")
print("Bem-vindo ao jogo de adivinhação!")
while not guessed:
    guess = int(input("Tente adivinhar o número secreto entre 1 e 10: \n"))

    if guess == secret_number:
        print(f"Parabéns! Você adivinhou o número secreto! Era {secret_number}.")
        guessed = True