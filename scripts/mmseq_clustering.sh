#!/bin/bash

#Activate conda environment
#conda create -n mmseq2 -c conda-forge -c bioconda mmseqs2
conda activate mmseq2

#Set primer
PRIMER=MZ

#Make output directory (if doesnt exist)
if [ ! -d "Clustered_Files" ]
then
    mkdir Clustered_Files
fi
mkdir Clustered_Files/${PRIMER}_primer

# Run clustering via mmseq2
for FASTA in $(ls FASTAs/${PRIMER}_primer/*.fa)
do
    BASE=$(basename $FASTA | cut -d "." -f 1)
    mmseqs easy-linclust \
    $FASTA Clustered_Files/${PRIMER}_primer/${BASE} tmp \
    --cov-mode 1 -c 0.9 --min-seq-id 0.97
done
