#!/usr/bin/env python3

import os, sys, re
from Bio.Seq import Seq

multifasta_file = sys.argv[1]

if os.path.exists(multifasta_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...')
    with open(multifasta_file, 'r') as sys_read:
        nucleotide_dictionary = {}
        for line in sys_read:
            if line.startswith('>'):
                new_line = line.rstrip().split(' ').pop(0).replace('>', '')
                nucleotide_dictionary[new_line] = {}
                full_sequence_line = ''
            else:
                full_sequence_line += ''.join(line.rstrip())
                for ORF1_search in re.finditer(r'(([ATGC]{3})+)', full_sequence_line):
                    ORF1_sequence = full_sequence_line[ORF1_search.start(1):ORF1_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF1'] = ORF1_sequence
                #    ORF1_coding_region = Seq(ORF1_sequence)
                #    ORF1_protein = ORF1_coding_region.translate()
                #    ORF1_aminoacid_sequence = ''
                #    for aminoacid in ORF1_protein:
                #        ORF1_aminoacid_sequence += aminoacid
                #        protein_dictionary[new_line]['ORF1 Protein'] = ORF1_aminoacid_sequence
                    ORF1_reverse_complement = ORF1_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF1 rc'] = ORF1_reverse_complement
                for ORF2_search in re.finditer(r'\w(([ATGC]{3})+)', full_sequence_line):
                    ORF2_sequence = full_sequence_line[ORF2_search.start(1):ORF2_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF2'] = ORF2_sequence
                #    ORF2_coding_region = Seq(ORF2_sequence)
                #    ORF2_protein = ORF2_coding_region.translate()
                #    ORF2_aminoacid_sequence = ''
                #    for aminoacid in ORF2_protein:
                #        ORF2_aminoacid_sequence += aminoacid
                #        protein_dictionary[new_line]['ORF2 Protein'] = ORF2_aminoacid_sequence
                    ORF2_reverse_complement = ORF2_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF2 rc'] = ORF2_reverse_complement
                for ORF3_search in re.finditer(r'\w{2}(([ATGC]{3})+)', full_sequence_line):
                    ORF3_sequence = full_sequence_line[ORF3_search.start(1):ORF3_search.end(1)]
                    nucleotide_dictionary[new_line]['ORF3'] = ORF3_sequence
                #    ORF3_coding_region = Seq(ORF3_sequence)
                #    ORF3_protein = ORF3_coding_region.translate()
                #    ORF3_aminoacid_sequence = ''
                #    for aminoacid in ORF3_protein:
                #        ORF3_aminoacid_sequence += aminoacid
                #        protein_dictionary[new_line]['ORF3 Protein'] = ORF3_aminoacid_sequence
                    ORF3_reverse_complement = ORF3_sequence.replace('A', 't').replace('T', 'a').replace('C',  'g').replace('G', 'c').upper()
                    nucleotide_dictionary[new_line]['ORF3 rc'] = ORF3_reverse_complement
        protein_dictionary = {}
        for gene_tag, ORF_dict in nucleotide_dictionary.items():
            protein_dictionary[gene_tag] = {}
            for ORF_key, ORF_seq in ORF_dict.items():
                ORF_coding_region = Seq(ORF_seq)
                ORF_protein = ORF_coding_region.translate()
                protein_dictionary[gene_tag][ORF_key] = str(ORF_protein)

   #     print(protein_dictionary)
                

            #ORF_coding_region = Seq(value['ORF 1'])
            #ORF_protein = ORF_coding_region.translate()
            #ORF_aminoacid_sequence = ''
            #for aminoacid in ORF_protein:

#        coding_DNA = Seq(new_sequence) #Tem que colocar esse Seq para o biopython funcionar (aparecia assim na documenta????o)
#        protein = coding_DNA.translate()



#        print(protein_dictionary)




        #9sep_list_by_tag = (''.join(sys_read.read().splitlines())).split('>')
#        print(sep_list_by_tag)       
#        def ORF(sys_read):
        #for item in sep_list_by_tag:
#            print(line)
        #    for match in re.finditer(r'\w+', item):
#                teste = match.group(1)
         #       print([match])





#                #PRIMEIRO OPEN READING FRAME:
#                for line in splitting_greater_than: #Para cada linha cont??nua...f
#                    for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line): #...quero o identificador da sequ??ncia. Eu reparei que o n??mero que acompanhava o c variava, ent??o eu coloquei o + ao lado do d, mas eu tamb??m coloquei junto de todo o resto, porque eu n??o sabia se eles SEMPRE eram fixos.
#                        dictionary[match] = {} #Acrescentando o identificador como chave do dicion??rio.                                                                                     for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I): #Quero achar c??dons quantas vezes aparecerem... (Aqui t?? tudo juntoe e t?? separando eles de tr??s em tr??s)
#                        sequence = line[codon.start():codon.end()] #Separando os c??dons e atribuindo eles a uma vari??vel.                                                                       codon_list = [] #Criando uma lista vazia de c??dons.
#                        for nt in range(0, len(sequence), 3): #Para nucleot??deos nesse intervalo...
#                            codon_list += [sequence[nt:nt+3]] #...adicionar eles na nossa lista de c??dons...
#                            joining = ' '.join(codon_list) #Juntando os c??dons por espa??os.  
#                            for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I): #Procurando c??dons completos.
#                                new_sequence = joining[codon_search.start():codon_search.end()] #Salvando a sequ??ncia aqui.
#                                dictionary[match]['ORF1'] = new_sequence #...e no dicion??rio depois.
#                                #COMPLEMENTO REVERSO PRIMEIRO OPEN READING FRAME:
##                                reverse_complement = new_sequence.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper() #Substituindo.
#                                dictionary[match]['ORF1_rc'] = reverse_complement #Salvando no dicion??rio.
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
