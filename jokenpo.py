


from random import randint

print('#'*9,"'BEM VINDO AO JOKENPO PYTHON VERSION'",'#'*9)
playername = input('Digite Seu Nome: ')
vitoria = ('Parabens %s vc venceu'%playername)
derrota = 'Computador venceu'
userchance = int(input('Para jogar escolha entre:\n(1 para Pedra)-(2 para Papel)-(3 para Tesoura)\nDigite o valor aqui: '))
nomes = ['nada','Pedra','Papel','Tesoura']
com = randint(1,3)
comchoice = nomes[com]
#regras jokenpo
pd_x_ts = 'Pedra quebra Tesoura, '
ts_x_pp = 'Tesoura corta Papel, '
pp_x_pd = 'Papel enrola Pedra, '
r = 'resultado'

while userchance not in [1,2,3]:
    userchance = int(input('Escolha Invalida, escolha novamente, conforme a lista acima!\nDigite o valor aqui:  '))

if userchance == com:
    r = ('Empate: Ambos escolheram '+comchoice)
else:
    if userchance == 1:
        if com == 2:
            r = (pp_x_pd+derrota)
        else:
            r = (pd_x_ts+vitoria)
    elif userchance == 2:
        if com == 1:
            r = (pp_x_pd+vitoria)
        else:
            r = (ts_x_pp+derrota)
    else:
        if com == 1:
            r = (pd_x_ts+derrota)
        else:
            r = (ts_x_pp+vitoria)

userchance = nomes[userchance]
print('vc escolheu %s, o computador %s! \n        %s!' %(userchance,comchoice,r)) # mostra o resultado da partida!!
print('# '*7,'Obrigado por Jogar: '+playername,'# '*7)

