"""
File:           merge_pia.py
Author:         Ashley T. Sendell-Price
Date:           27.03.2024
Description:    ADD
                Requires bioinfokit
Usage:          python extract_sequences taxaID
"""

#Import required modules
import sys
from bioinfokit.analys import Fasta

#Create sequence ID list
IDfile = open('sequenceIDs.txt', 'w')
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        #check not a header line
        if not "#" in line:
            #
            if line.split(sep = '\t')[1] == sys.argv[2]:
                sequenceID = line.split(sep = '\t')[0]
                IDfile.writelines(sequenceID + '\n')

# extract sequences based on sequence ID and region coordinates
Fasta.extract_seq(file = FASTA, id="sequenceIDs.txt")
