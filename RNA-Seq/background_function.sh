ckground_function.sh
# Specify the input path as an absolute path.
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Specify the desired file suffix
leftSuffix="*R1.fastq"
function listFiles {
    for fastqFile in $fastqPath$leftSuffix
            do
                        echo $fastqFile
                                # The sleep command below is just to slow this down
                                        # enough for you to see in in top.
                                                sleep 30
                                                    done
                                                }
                                                # Run the function in the background, send success output to listFiles.log and 
                                                # error output to listFiles.err.
                                                listFiles 1>list.log 2>list.err &
