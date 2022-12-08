#!/usr/bin/env python3

import os, sys, re
from Bio.Seq import Seq

multifasta_file = sys.argv[1]

if os.path.exists(multifasta_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...')
    with open(multifasta_file, 'r') as sys_read:
        nucleotide_dictionary = {}
        protein_dictionary = {}
        for line in sys_read:
            if line.startswith('>'):
                new_line = line.rstrip().split(' ').pop(0).replace('>', '')
                nucleotide_dictionary[new_line] = {}
                protein_dictionary[new_line] = {}
                full_sequence_line = ''

            else:
                full_sequence_line += ''.join(line.rstrip())
                for ORF1_search in re.finditer(r'(([ATGC]{3})+)', full_sequence_line):
                    ORF1_sequence = full_sequence_line[ORF1_search.start(1):ORF1_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF1'] = ORF1_sequence
                    ORF1_coding_region = Seq(ORF1_sequence)
                    ORF1_protein = ORF1_coding_region.translate()
                    

                    amino_list = ''


                    for aminoacid in ORF1_protein:
                        amino_list += aminoacid
                    #    protein_dictionary[new_line]['ORF1 Protein'] = ORF1_protein
                        protein_dictionary[new_line]['ORF1 Protein'] = amino_list


                    ORF1_reverse_complement = ORF1_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF1 rc'] = ORF1_reverse_complement
                for ORF2_search in re.finditer(r'\w(([ATGC]{3})+)', full_sequence_line):
                    ORF2_sequence = full_sequence_line[ORF2_search.start(1):ORF2_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF2'] = ORF2_sequence
                    ORF2_reverse_complement = ORF2_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF2 rc'] = ORF2_reverse_complement
                for ORF3_search in re.finditer(r'\w{2}(([ATGC]{3})+)', full_sequence_line):
                    ORF3_sequence = full_sequence_line[ORF3_search.start(1):ORF3_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF3'] = ORF3_sequence
                    ORF3_reverse_complement = ORF3_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF3 rc'] = ORF3_reverse_complement
        

#        coding_DNA = Seq(new_sequence) #Tem que colocar esse Seq para o biopython funcionar (aparecia assim na documentação)
#        protein = coding_DNA.translate()



        print(protein_dictionary)




        #9sep_list_by_tag = (''.join(sys_read.read().splitlines())).split('>')
#        print(sep_list_by_tag)       
#        def ORF(sys_read):
        #for item in sep_list_by_tag:
#            print(line)
        #    for match in re.finditer(r'\w+', item):
#                teste = match.group(1)
         #       print([match])





#                #PRIMEIRO OPEN READING FRAME:
#                for line in splitting_greater_than: #Para cada linha contínua...f
#                    for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line): #...quero o identificador da sequência. Eu reparei que o número que acompanhava o c variava, então eu coloquei o + ao lado do d, mas eu também coloquei junto de todo o resto, porque eu não sabia se eles SEMPRE eram fixos.
#                        dictionary[match] = {} #Acrescentando o identificador como chave do dicionário.                                                                                     for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I): #Quero achar códons quantas vezes aparecerem... (Aqui tá tudo juntoe e tá separando eles de três em três)
#                        sequence = line[codon.start():codon.end()] #Separando os códons e atribuindo eles a uma variável.                                                                       codon_list = [] #Criando uma lista vazia de códons.
#                        for nt in range(0, len(sequence), 3): #Para nucleotídeos nesse intervalo...
#                            codon_list += [sequence[nt:nt+3]] #...adicionar eles na nossa lista de códons...
#                            joining = ' '.join(codon_list) #Juntando os códons por espaços.  
#                            for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I): #Procurando códons completos.
#                                new_sequence = joining[codon_search.start():codon_search.end()] #Salvando a sequência aqui.
#                                dictionary[match]['ORF1'] = new_sequence #...e no dicionário depois.
#                                #COMPLEMENTO REVERSO PRIMEIRO OPEN READING FRAME:
##                                reverse_complement = new_sequence.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper() #Substituindo.
#                                dictionary[match]['ORF1_rc'] = reverse_complement #Salvando no dicionário.
#                #SEGUNDO OPEN READING FRAME:
#                for line in splitting_greater_than:
#                    for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line):
#                        for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I):
#                            sequence = line[codon.start():codon.end()]
#                            corrected_sequence = re.sub(r'\w', '', sequence, 1)
#                            codon_list = []
#                            for nt in range(0, len(corrected_sequence), 3):
#                                codon_list += [corrected_sequence[nt:nt+3]]
#                                joining = ' '.join(codon_list)
#                            for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I):
#                                new_sequence = joining[codon_search.start():codon_search.end()]
#                                dictionary[match]['ORF2'] = new_sequence
                                #COMPLEMENTO REVERSO SEGUNDO OPEN READING FRAME:
#                                reverse_complement = new_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
#                                dictionary[match]['ORF2_rc'] = reverse_complement
#                #TERCEIRO OPEN READING FRAME:
#                for line in splitting_greater_than:
#                    for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line):
#                        for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I):
#                            sequence = line[codon.start():codon.end()]
#                            corrected_sequence = re.sub(r'\w', '', sequence, 2)
#                            codon_list = []
#                            for nt in range(0, len(corrected_sequence), 3):
#                                codon_list += [corrected_sequence[nt:nt+3]]
#                                joining = ' '.join(codon_list)
#                            for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I):
#                                new_sequence = joining[codon_search.start():codon_search.end()]
#                                dictionary[match]['ORF3'] = new_sequence
#                                #COMPLEMENTO REVERSO TERCEIRO OPEN READING FRAME:
#                                reverse_complement = new_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
#                                dictionary[match]['ORF3_rc'] = reverse_complement
