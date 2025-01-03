#! /bin/bash


java -jar picard.jar CollectInsertSizeMetrics \
      I=/Users/valishashah/Desktop/all_projects/HaLab_assessment/Sequencing_analysis_assignment/DATA/HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam \
      O=insert_size_metrics.txt \
      H=insert_size_histogram.pdf \
      M=0.5
