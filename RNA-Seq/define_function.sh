
n.sh
# Specify the input path as an absolute path.
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Specify the desired file suffix
leftSuffix="*R1.fastq"
function listFiles {
    for fastqFile in $fastqPath$leftSuffix
            do
                        echo $fastqFile
                            done
                        }
                        listFiles 1>out3.log 2>out3.err
