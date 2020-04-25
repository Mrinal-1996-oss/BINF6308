#!/usr/bin/env python
#count_kmers.py
#nitialize an empty dictionary
kmer_counts = dict()
# Create an array of kmers
kmers = ['atccg', 'ttttt', 'ccccc', 'ccccc', 'aaaaa']
# Iterate over the array of kmers
for kmer in kmers:
    # Check if the kmer is in the dictionary
    if kmer in kmer_counts:
       # If in dictionary, increment count
       kmer_counts[kmer]+=1
    else:
       # Else initialize count to 1
       kmer_counts[kmer]=1
# Iterate over the kmers in the dictionary
for kmer in kmer_counts:
                                                                            # Check if count is one (kmer is unique)
                                                                            if kmer_counts[kmer] == 1:
                                                                               #Print unique kmer
                                                                               print kmer
