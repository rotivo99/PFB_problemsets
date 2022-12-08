#!/usr/bin/env python3

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'

dna_sub_1 = dna.find('ATG')
dna_sub_2 = dna.find('TTT')

if dna_sub_1 == -1:
    print('No ATG were found in your sequence.')
else:
    print(dna_sub_1, 'ATG were found in your sequence.')

if dna_sub_2 == -1:
    print('No TTT were found in your sequence.')
else:
    print(dna_sub_2, 'TTT were found in your sequence.')

print('')

print(dna.find('ATG'))
print(dna.find('TTT'))

print('')

import sys

t_test = float(sys.argv[1])

if t_test <= 0.05:
    print('Based on the t-test results with a significance of 5%, your means can\'t be considered similar.')
else:
    print('Based on the t-test results with a significance of 5%, your means can be considered similar.')

print('')

number = 7

if number > 0:
    print('Your number has a positive value.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')

print('')

if number > 0:
    if number > 50:
        print('Your number is positive and also bigger than 50.')
    else:
        print('Your number is positive and and also smaller than 50.')
elif number < 0:
    print('Your number has a negative value.')
else:
    print('Your number is zero.')
