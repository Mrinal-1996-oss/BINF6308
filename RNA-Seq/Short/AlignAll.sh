#fastq path
fastqpath="./Paired/"

#R1 files
R1=".R1.fastq"

#create sam directory
mkdir -p sam

function align_reads {
for i in $fastqpath*$R1
do
	path_remove="${i/$fastqpath}"
	sample_name="${path_remove/$R1}"
	nice -n19 gsnap \
    	-A sam \
    	-D . \
    	-d AiptasiaGmapDb \
    	-s AiptasiaGmapIIT.iit \
    	$fastqpath$sample_name.R1.fastq \
    	$fastqpath$sample_name.R2.fastq \
    	1>./sam/$sample_name.sam$
done
}

align_reads
