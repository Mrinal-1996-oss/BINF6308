#!/usr/bin/env python
#interleaved.py
import os
try:
    os.remove("Interleaved.fasta")
except Exception as e:
     print(e)
from Bio import SeqIO 
read_left = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
read_right = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")
allreader= []
for left,right in zip(read_left,read_right):
    allreader.append(left)
    allreader.append(right)
with open("Interleaved.fasta", "w") as output:
      SeqIO.write(allreader, output, "fasta")

      
