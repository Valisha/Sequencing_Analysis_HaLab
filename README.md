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

#### b. hist_cdf_fasta.Rmd - Generate a frequency distribution plots as below. 
   i. Plot the distribution of read lengths (column 2 of the table you will generate) as a histogram  
   ii. Given a genomic signature C of a sequence S, the vector F of frequencies of 2-mers appearing in S is obtained first by adding one to each of the components of C to obtain a vector P of pseudo-counts. Then, letting L be the sum of the components of P, the frequency of the 2-mer x is calculated as follows: Fx = Px/L.
	
### Execute the script using - 
	python3 create_table_from_fasta.py

## 2. NGS Familiarity Assignment

### Included scripts are - 
##### a. download_bam_bai.sh - Download the bam file, filter the poorly mapped inserts and create a txt file with insert sizes 
##### b. plot_insert_sizes.py - plot the distribution with fragment size as the X axis. 

### Execute the script using - 
1. 		sh download_bam_bai.sh
2.		python3 plot_insert_sizes.py
   Picard sript -
3.		sh plot_inserts_picard.sh 

### 3. For paired-end sequencing, how can distributions of insert sizes be used to reveal certain types of somatic alterations?
In paired-end sequencing, insert size distributions provide valuable insights into the structure of the sequenced genome. Variations in these distributions can indicate specific types of somatic alterations:

##### 1. Deletions:
When a region of the genome is deleted, paired-end reads that were once mapped across the deletion site may now be mapped with smaller than expected insert sizes because the physical distance between paired reads is reduced due to the missing segment. 

##### 2. Duplications: 
In contrast, in regions with duplications, paired-end reads can have larger than expected insert sizes because the same pair of reads might map to duplicated regions, increasing the distance between the paired reads.

##### 3. Structural Variants (SVs):
Larger structural variations, such as inversions or translocations, can lead to abnormal insert size distributions, as the paired reads may map in unexpected locations or orientations. This will cause the insert sizes to be either too small or too large compared to the typical distribution.

Lumpy-SV and Manta could be used to detect these structural variants. And once these structural variants are identified, they can be visualized in IGV or UCSC Genome Browser
By comparing the observed insert size distribution with the expected distribution based on the reference genome, one can infer the presence of somatic alterations like deletions, duplications, and other structural variants.

