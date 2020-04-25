#!/usr/bin/env bash
#spades.sh
mkdir -p Rhodo
/usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
-1 Paired/SRR522244_1.fastq -2 Paired/SRR522244_2.fastq \
-t 4 \
-o Rhodo
