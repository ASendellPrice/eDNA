"""
File:           extract_sequences.py
Author:         Ashley T. Sendell-Price
Date:           28.04.2024
Description:    Outputs sequences assigned to specified taxa ID into a fasta file (output.fasta)
                Requires bioinfokit
Usage:          python extract_sequences pia_output fasta taxaID:
"""

import sys
import os

sequenceIDs = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if not "#" in line:
            if line.split(sep = '\t')[1] == sys.argv[3]:            
                sequenceID = line.split(sep = '\t')[0]
                with open(sys.argv[2], 'r') as fasta:
                    for fasta_entry in fasta.readlines():
                        if ">" in fasta_entry and sequenceID in fasta_entry:
                                sequenceIDs.append(fasta_entry.strip().replace(">", "")) 

with open('sequenceIDs.txt', 'w') as outfile:
    outfile.write("\n".join(sequenceIDs))

os.system('seqtk subseq ' + sys.argv[2] + ' sequenceIDs.txt | grep -v "[subseq]" > output.fasta')
