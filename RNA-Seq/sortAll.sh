 #!/usr/bin/env bash
 # sortAll.sh
sampath="./sam/"

#make a directory
mkdir -p $bam
#Sorting function
function sortAll {
for leftInFile in $sampath*
do
  #Get the sample name
  samplename="${leftInFile/$sampath/}"
   echo samplename
    samtools sort \
    $sampath$samplename.sam \
   -o./bam/$samplename.sorted.bam
done
}
sortAll  1>sample_name.sort.log 2>sample_name.sort.err &


