#!/usr/env bash
#alignPredicted.sh
#BLASTing the Trinity.Decoder from the Trinity.fasta.transdecoder.pep file and comparing it with the SwissProt database  
blastp -query Trinity.fasta.transdecoder.pep  -db swissprot  1  -outfmt "6 qseqid sacc qlen slen length nident pident evalue stitle"  -evalue  1e-10 -num_threads 4  1> alignPredicted.txt 2>alignPredicted.err &
