#!/usr/bin/env python
import re
#import os
read_sample = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')

# Initialize a variable to contain the lines
line = ' '
seq = ' '
kmer_dictionary = {}

# While line is not empty
while line:
     # Read one line from the file
      line = read_sample.readline()
        #Remove end-of-line character
       # line = line.rstrip(os.linesep)
      if re.match('^[ATGCN]+$', line):
     # Print the line
     # line=line.rstrip(os.linesp)
     # if rematch('^[ATGCN]+$',line):
        #Print the line
        print(line)
        # seq=line+seq
        kmer_length = 6
        # Calculate the stop before the loop to improve efficiency. 
        stop = len(line) -kmer_length + 1
for start in range(0,stop):
            kmer =seq[start:start + kmer_length]

            #See if its in the dictionary
            if kmer in kmer_dictionary:
                #Add one to count
                kmer_dictionary[kmer]+= 1
            else:
              #It's not in the dictionary so add with a count of 1
              kmer_dictionary[kmer] =1

#Print the number of keys in the dictionary
print(len(kmer_dictionary))

#Save a tab character to print output as tab-separated
t= "\t"
aip_kmers = open("aip_kmers.txt",'w')

#Iterate over the k-mers in the dictionary
for kmer in kmer_dictionary:
    #Get the count of how many times observed
    count=kmer_dictionary[kmer]
    #Convert the count to a string and make a tuple of the kmer and count
    out =(kmer,str(count))
    #Join the elements of the out tuple with tabs and print
    aip_kmers.write(t.join(out))


