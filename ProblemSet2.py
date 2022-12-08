#!/usr/bin/env python3

import sys

dna = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
sequencia = sys.argv[1].upper()

if sequencia in dna:
    print(sequencia, "foi encontrado na sua sequência")
else:
    print(sequencia, "NÃO foi encontrado na sua sequência")

syscount = dna.count(sequencia)
print(syscount)
