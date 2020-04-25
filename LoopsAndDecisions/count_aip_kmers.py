#!/usr/bin/env python
import re
import os
read_sample = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')

kmer_length = 6
kmer_dictionary = {}
line = ' '
while line:
    # Read one line from the file
    line = read_sample.readline()
    # Remove end-of-line character
    line = line.rstrip(os.linesep)
    if re.match('^[ATGCN]+$', line):
        stop = len(line) - kmer_length + 1
        # Iterate over the positions
        for start in range(0, stop):
            # Get the substring at a specific start and end position
            kmer = line[start:start + kmer_length]
            if kmer in kmer_dictionary:
                #Add one to count
                kmer_dictionary[kmer]+= 1
            else:
                #It's not in the dictionary so add with a count of 1
                kmer_dictionary[kmer] =1

t= "\t"
aip_kmers = open("aip_kmers.txt",'w')

#Iterate over the k-mers in the dictionary
for kmer in kmer_dictionary:
    #Get the count of how many times observed
    count=kmer_dictionary[kmer]
    #Convert the count to a string and make a tuple of the kmer and count
    out =(kmer,str(count))
    #Join the elements of the out tuple
    out =t.join(out) + "\n"
    aip_kmers.write(out)
