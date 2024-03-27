#!/bin/bash

#Set primer
PRIMER=IV

#Get current directory path
DIR=$(pwd)

#Make output directories
if [ ! -d "PIA_output" ]
then
    mkdir PIA_output
fi
mkdir PIA_output/${PRIMER}_primer

#Move to directory containing pia scripts
cd ${DIR}/bin/PIA

#For each clustered fasta file 
for FASTA in $(ls ${DIR}/Clustered_Files/${PRIMER}_primer/*_rep_seq.fasta)
do
    #Get file basename
    BASE=$(basename $FASTA | cut -d "." -f 1)

    #Run PIA
    perl PIA.pl -f $FASTA -b ${DIR}/blast_files/${BASE}.blast.txt

    #Move output files
    mv ${DIR}/Clustered_Files/${PRIMER}_primer/${BASE}.PIA_output/* ${DIR}/PIA_output/${PRIMER}_primer/
    rm -r ${DIR}/Clustered_Files/${PRIMER}_primer/${BASE}.PIA_output/
done
