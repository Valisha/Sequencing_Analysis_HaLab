#! /bin/bash

samtools index HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam

### find the insert sizes
# samtools view -f 1 HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam | awk '{print $9}' > insert_sizes.txt

##### Inspecting the negative insert sizes
# samtools view -h HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam | head -n 20

### Check for discordant or misaligned 

# samtools view -f 4 HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam 

### Inspect the region or the coverage 

# samtools flagstat HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam


### Visualize the coverage 

# bedtools genomecov -ibam HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam > coverage.txt

### Filter out the negative insert sizes
samtools view -f 1 -F 12 HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam | awk '$9 >= 0 {print $0}' > filtered_bam.bam

### save the filtered bam as a table 

awk '{print $9}' filtered_bam.bam > insert_sizes_filtered.txt

###### insert sizes - picard collect insert sizes

