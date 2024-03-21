import random
import os
print()
print('Bem vindo ao Jokenpô!!!'.center(140))
print()
print('jokenpô é um jogo em que as pessoas jogam com as mãos, escolhendo entre pedra, papel e tesoura.'.center(140))
print('Funciona assim: a tesoura corta o papel, mas quebra com a pedra; o papel embrulha a pedra'.center(140))
print('mas é cortado pela tesoura e a pedra quebra a tesoura e é embrulhada pelo papel.'.center(140))
print('Porem aqui sera você contra o computador.'.center(140))
print('Boa sorte e se divirta.'.center(140))
print()
x = 0
meuponto = 0
pontocomp = 0
while x < 3:
    minhajogada = input('Escolha entre pedra, papel ou tesoura: ')
    os.system('cls')
    minhajogada = minhajogada.capitalize()
    jogo = ['Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura']
    computador = random.choice(jogo)
    if minhajogada == computador:
        print('Você colocou', minhajogada,'e o computador colocou',computador,'e o resultado foi empate.')
        x -= 1
    elif minhajogada == 'Pedra' and computador == 'Papel':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você foi derrotado.')
        pontocomp += 1 
    elif minhajogada == 'Pedra' and computador == 'Tesoura':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você venceu.')
        meuponto += 1 
    elif minhajogada == 'Papel' and computador == 'Pedra':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você venceu.')
        meuponto += 1 
    elif minhajogada == 'Papel' and computador == 'Tesoura':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você foi derrotado.')
        pontocomp += 1 
    elif minhajogada == 'Tesoura' and computador == 'Papel':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você venceu.')
        meuponto += 1 
    elif minhajogada == 'Tesoura' and computador == 'Pedra':
        print('Você colocou', minhajogada,'e o computador colocou',computador,', você foi derrotado.')
        pontocomp += 1 
    elif minhajogada not in jogo:
        print('Jogada invalida')
    x += 1
    if meuponto == 2:
        print()
        print('Parabens!!! Você venceu o computador!!!')
        break
    elif pontocomp == 2:
        print()
        print('Infelizmente você perdeu para o computador.')
        break