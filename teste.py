#!/usr/bin/env python3

text = 'CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAAATGATGATGATG'
index = 0

while index < len(text):
    index = text.find('ATG', index)
    if index == -1:
        break
    print('ATG found at', index)
    index += 3 # +2 because len('ll') == 2
