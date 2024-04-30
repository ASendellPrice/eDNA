"""
File:           extract_sequences.py
Author:         Ashley T. Sendell-Price
Date:           28.04.2024
Description:    Outputs sequences assigned to specified taxa ID into a fasta file (output.fasta)
                Requires bioinfokit
Usage:          python extract_sequences pia_output fasta taxaID:
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
            #If line 
            if line.split(sep = '\t')[1] == sys.argv[3]:
                sequenceID = line.split(sep = '\t')[0]
                IDfile.writelines(sequenceID + '\n')

# extract sequences based on sequence ID and region coordinates
Fasta.extract_seq(file = sys.argv[2], id="sequenceIDs.txt")
