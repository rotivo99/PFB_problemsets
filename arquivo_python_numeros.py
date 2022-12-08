#!/usr/bin/env python3

import sys

print('#1') #Checa se o número é positivo ou negativo.

number = float(sys.argv[1])

if number > 0:
    print('Your number has a positive value.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')

print('')
print('#2') #Checa se o número, quando positivo, é maior, menor ou igual a 50.

if number > 0:
    if number > 50:
        print('Your number is positive and also bigger than 50.')
    elif number < 50:
        print('Your number is positive and and also smaller than 50.')
    else:
        print('Your number is fifty.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')

print('')
print('#3') #Checa se o número, quando menor que 50, é par.

if number > 0:
    if number > 50:
        print('Your number is positive and also bigger than 50.')
    elif number < 50:
        if number % 2 == 0:
            print('Your number is positive, smaller than 50, but even.')
        else:
            print('Your number is positive, smaller than 50, but definetly not even.')
    else:
        print('Your number is fifty.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')

print('')
print('#4') #Checa se o número, quando maior que 50, é divisível por 3.

if number > 0:
    if number > 50:
        if number % 3 == 0:
            print('Your number is positive, bigger than 50 and divisible by 3.')
        else:
            print('Your number is positive, bigger than 50, but indivisible by 3.')
    elif number < 50:
        if number % 2 == 0:
            print('Your number is positive, smaller than 50, but even.')
        else:
            print('Your number is positive, smaller than 50, but definetly not even.')
    else:
        print('Your number is fifty.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')
