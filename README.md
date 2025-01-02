# Sequencing_analysis_assignment

## 1. Fasta File Assignment

### Included scripts are - 
#### a. create_table_from_fasta.py - Generate a tab-delimited table from the fasta file using python scripting
	- column 1: Read ID   
	- column 2: Length of the nucleotide sequence   
	- column 3: The 5-mer centered on the midpoint of the sequence   
	- column 4: The reverse complement of the 5-mer in column 3   
	- columns 5-20: A vector C defined in the following manner:   
  		- For a given nucleotide sequence S in the fasta file, C is a vector of length 16 indexed by all 2-mers in alphabetical order (for example, `'AA','AC','AG'`,etc), such that Cx is the number of times the 2-mer x appears in the sequence S  

- Plot the distribution of read lengths (column 2 of the table you will generate) as a histogram  
- Create a new plot. Within one pair of axes, draw the cumulative distribution of 2-mer frequencies (F) for each sequence S, defined as follows:    
	- Given a genomic signature C of a sequence S, the vector F of frequencies of 2-mers appearing in S is obtained first by adding one to each of the components of C to obtain a vector P of pseudo-counts. Then, letting L be the sum of the components of P, the frequency of the 2-mer x is calculated as follows: Fx = Px/L.
	
	
### 2. NGS Familiarity

Download the chromosome 20 bam file HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam and its corresponding .bai file from here:  
- ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/HG00096/alignment/

Find insert sizes for mapped read pairs and plot their distribution with fragment size as the X axis. Document and explain all the steps and commands you execute.  

For paired-end sequencing, how can distributions of insert sizes be used to reveal certain types of somatic alterations?
