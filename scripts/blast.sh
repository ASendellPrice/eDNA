#!/bin/bash

#File:           merge_pia.py
#Author:         Ashley T. Sendell-Price
#Date:           27.03.2024
#Description:    ADD
#Usage:          source run_blast.sh VERT

#Set primer
PRIMER=$1

#Make output directory (if doesnt exist)
if [ ! -d "blast_files" ]
then
    mkdir blast_files
fi

# mamba create -n blast_eDNA blast -c bioconda
conda activate blast_eDNA
for FASTA in $(ls Clustered_Files/${PRIMER}_primer/*_rep_seq.fasta)
do
    BASE=$(basename $FASTA | cut -d "." -f 1)
    blastn -db bin/blast_db/nt \
    -query $FASTA -out blast_files/${BASE}.blast.txt \
    -max_target_seqs 500 -outfmt "6 std staxids" -num_threads 4 
done

