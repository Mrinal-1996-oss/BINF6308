#!/usr/bin/env bash
# append_output.sh
# Specify the input path as an absolute path.
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Specify the desired file suffix
leftSuffix="*R1.fastq"
# Empty the log file before starting
echo '' 1>out2.log
# Empty the err file before starting
echo '' 2>out2.err
for fastqFile in $fastqPath$leftSuffix
do
        echo $fastqFile 1>> out2.log 2>> out2.err
    done
