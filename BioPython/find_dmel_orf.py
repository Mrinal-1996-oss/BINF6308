#!/usr/bin/env python3
# read_print.py
# Create a file object named read_sample
from Bio.Seq import Seq
from Bio import SeqIO
import re
read_sample = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"
for record  in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
    if re.match("^\d{1}\D*$",record.id):
       rna = record.seq.transcribe()
       orf = re.search("AUG([AUGC]{3})+?(UAA|UAG|UGA)", str(rna)).group()
       print(Seq(orf).translate())
