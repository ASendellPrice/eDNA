#!/bin/bash
#pip install bioinfokit

taxaID = "10053"
primer = "V"
site = "17"




step 1 find sequence IDs allocated to focal taxa ID
grep "10053" eDNA/PIA_output/V_primer/V17-211123_S95_L001_rep_seq.Summary_Reads.txt

step 2 extract these sequences from fasta
grep "M02610:119:000000000-L677M:1:2102:14295:22763" ../../Clustered_Files/V_primer/V17-211123_S95_L001_all_seqs.fasta

