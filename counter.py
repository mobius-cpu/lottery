#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : counter.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 16.01.2020
# Last Modified Date: 16.01.2020
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>

bet = []
drawn = []
amount_bet = 0
amount_drawn = 0


def collector():
    global amount_bet, amount_drawn
    amount_bet = int(input('How many numbers you bet '))
    for i in range(0, amount_bet):
        bet.append(int(input('Enter with ' + str(i+1) + 'º number ')))

    amount_drawn = int(input('\n' + 'How many numbers was drawn '))
    for i in range(0, amount_drawn):
        drawn.append(int(input('Enter with ' + str(i+1) + 'º number ')))


def counter():
    count = 0
    for i in range(0, amount_drawn):
        count = count + bet.count(drawn[i])
    return count


collector()
successes = counter()
percentage = round(counter()*100.0/amount_drawn, 1)

print('\n' + "Your successes are " + str(successes))
print('\n' + "Your percentage of success is " + str(percentage) + '%')
