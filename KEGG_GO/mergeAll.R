#!/usr/bblast$cov <- blast$nident/blast$sleniiin/env Rscript
cdesci

# Load BLAST results as a table using tab (\t) as separator.
# There is no header with column names, so set header=FALSE
blast <- read.table("../BLAST/alignPredicted.txt", sep="\t", header=FALSE)
# Set column names to match fields selected in BLAST
colnames(blast) <- c("qseqid", "sacc", "qlen", "slen","length", "nident", "pident", "evalue", "stitle")
# Calculate the coverage as nident/slen
blast$cov <- blast$nident/blast$slen
# Select only blast rows where coverage is greater than .9
blast <- subset(blast, cov > .9, select=-c(stitle))
# Read kegg.txt, produced by get_kegg_ids, as a table
kegg <- read.table("kegg.txt", sep="\t", header=FALSE)
# Set the column names for kegg
colnames(kegg) <- c("sacc", "kegg")
# Remove the up: prefix from the accession number so it will match the BLAST
# subject accession (sacc)
kegg$sacc <- gsub("up:", "", kegg$sacc)
# Merge the tables. Since one column name in common, just give
# the two tables as parameters to merge.
blast_kegg <- merge(blast, kegg)
# Display the first few lines of output
head(blast_kegg)
go <- read.csv("sp_go.txt", sep="\t", header=FALSE)
head(go)
# Finish this script to merge the rest of the data requested in
# the assignment
#Giving the access number and go id
colnames(go) <- c("sacc","go")
#Giving the head of the file
head(go)
#Merging the BLAST and GO file and finding the equal columns
blast_kegg_go <- merge(blast_kegg, go)
#Getting the KO-ID
ko_id<- read.table("ko.txt" ,sep="\t",header=FALSE)
#Giving the column names
colnames(ko_id) <- c("kegg","ko")
#Reading the path.txt file
k_path<- read.table("path.txt",sep ="\t", header=FALSE)
#Giving the column names
colnames(k_path)<- c("ko", "path")
#Giving the description
desc<- read.table("ko" , sep="\t",header=FALSE)
#Giving the column description
colnames(desc) <- c("path","desc")
#Getting the head of description
head(desc)
#Merging the BLAST and ko_id
koblast <-merge(blast_kegg_go, ko_id)
#Merging with path
pathblast <- merge(koblast, k_path)
#Merging with description
desc_blast <- merge(pathblast, desc)
#Head of description
head(desc_blast)
#Write it into a .csv file
write.table(desc_blast, "desc_blast.csv")
