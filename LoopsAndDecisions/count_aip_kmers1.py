import re
sequence= open ('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r') 
line= ' '
kmer_length= 6

            # 10 
kmer_dictionary= {}

#               12 
while line:
    line= sequence.readline()
    if re.match('^[ATGCN]+$', line):
        for start in range(0, len(line) - kmer_length):
            kmer= line[start:start +kmer_length]
            kmer_dictionary[kmer]=kmer_dictionary.get (kmer, 0) +1 

counted_kmer= ''

                    
for kmer, count in kmer_dictionary.items():
    counted_kmer=("{0}\t{1}\n".format(kmer, count))+ counted_kmer
    with open ("aip_kmers.txt",'w') as out:
        out.write (counted_kmer)
