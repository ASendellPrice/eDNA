"""
File:           merge_pia.py
Author:         Ashley T. Sendell-Price
Date:           27.03.2024
Description:    Takes output from multiple runs of PIA (https://github.com/Allaby-lab/PIA) 
                and merges into a single tab delimited file with taxonomic information added
                e.g. kingdom, superphylum, phylum etc. Taxonomic info sourced using taxaranks
                tool from https://github.com/linzhi2013/taxonomy_ranks
Usage:          python merge_pia.py PATH/TO/PIA/OUTPUT/DIRECTORY (requires blast_edna env)
"""

#Import required modules
import sys

with open((sys.argv[1]), 'r') as f:
    for line in f.readlines():
        if not "#" in line:
            if sys.argv[2] in line:
                print(line.split(sep = '\t')[0])
