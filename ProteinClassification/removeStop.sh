#!/usr/bin/env bash
#removeStop.sh
input=~/BINF6308/BLAST/Trinity.fasta.transdecoder.pep
sed  's/\*//' $input > temporary.fasta
head  -n500 temporary.fasta > proteins.fasta
rm -rf temporary.fasta

