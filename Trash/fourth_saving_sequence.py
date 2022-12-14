#!/usr/bin/env python3

import os, sys, re
from Bio.Seq import Seq

multifasta_file = sys.argv[1]

if os.path.exists(multifasta_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...')
    with open(multifasta_file, 'r') as sys_read, open('ORF.fna', 'w') as nucleotide_write, open('ORF.faa', 'w') as peptide_write:
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
                    nucleotide_dictionary[new_line]['ORF1_rc'] = ORF1_reverse_complement
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
                    nucleotide_dictionary[new_line]['ORF2_rc'] = ORF2_reverse_complement
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
                    nucleotide_dictionary[new_line]['ORF3_rc'] = ORF3_reverse_complement
        protein_dictionary = {}
        peptide_exception_dictionary = {}
        nucleotide_exception_dictionary = {}
        for gene_tag, ORF_dict in nucleotide_dictionary.items():
            protein_dictionary[gene_tag] = {}
            for ORF_key, ORF_seq in ORF_dict.items():
                ORF_coding_region = Seq(ORF_seq)
                ORF_protein = str(ORF_coding_region.translate())
                #ORF_protein = str(ORF_protein)
                try:
                    CDS_regex = re.search(r'M.+\*', ORF_protein)
                    coding_sequence = ORF_protein[CDS_regex.start():CDS_regex.end()]
                    protein_dictionary[gene_tag][ORF_key] = coding_sequence
                    peptide_write.write(f'>{gene_tag}_frame{ORF_key[3:7]}_{CDS_regex.start()}_{CDS_regex.end()}\n')
                    peptide_write.write(f'{coding_sequence}\n')
               #     if nucleotide_dictionary[gene_tag].has_key(protein_dictionary[gene_tag][ORF_key]):
                    nucleotide_write.write(f'>{gene_tag}_frame{ORF_key[3:7]}_{CDS_regex.start()*4-2}_{CDS_regex.end()*3}\n')
                    nucleotide_write.write(f'{nucleotide_dictionary[gene_tag][ORF_key]}\n')
               #     peptide_write.write(f'{gene_tag}_frame{ORF_key[3:7]}_{CDS_regex.start()}_{CDS_regex.end()}\n')
               #     peptide_write.write(f'{coding_sequence}\n')
               #     print(protein_dictionary)
                except AttributeError:
                    peptide_exception_dictionary[f'{gene_tag}_frame{ORF_key[3:7]}'] = ORF_protein
                    nucleotide_exception_dictionary[f'{gene_tag}_frame{ORF_key[3:7]}'] = ORF_seq
        peptide_write.write('\nThe following invalid aminoacid sequences were found in your file:\n')
        nucleotide_write.write('\nThe following invalid nucleotide sequences were found in your file:\n')
        for exception_tag, exception_value in peptide_exception_dictionary.items():
            #print(exception_tag, exception_value)
            #continue
            peptide_write.write(f'>{exception_tag}\n')
            peptide_write.write(f'{exception_value}\n')
        for nucleotide_exception_tag, nucleotide_exception_value in nucleotide_exception_dictionary.items():
            nucleotide_write.write(f'>{nucleotide_exception_tag}\n')
            nucleotide_write.write(f'{nucleotide_exception_value}\n')


#        print(exception_dictionary)
       #             continue
       #             peptide_write.write(f'>{gene_tag}_frame{ORF_key[3:7]}_No_coding_region_found\n')
       #             peptide_write.write(f'{ORF_protein}\n')
       #             continue
       #             print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq', gene_tag, ORF_key, ORF_protein)
                #cds_regex = re.search(r'M.+\*', sequence) #Achando sequ??ncia que comece com M e termine com *
                #cds = sequence[cds_regex.start():cds_regex.end()] #Separando a sequ??ncia numa vari??vel                                                                                  dictionary[split_2[0]]['Protein CDS'] = cds #E acrescenta ela como valor no dicion??rio

               # protein_dictionary[gene_tag][ORF_key] = str(ORF_protein)
