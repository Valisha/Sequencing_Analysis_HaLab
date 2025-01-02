#! /bin/python3 

from collections import Counter
import pandas as pd

# Function to extract readID from the header line
def extract_read_id(header):
    """ This function splits the header using '|' and return the third element (index 3)"""
    return header.strip().split("|")[3]

# Function to generate reverse complement
def reverse_complement(seq):
    """This function creates the reverse complement on the 5-mer.
    Input: nucleotide sequence (in this case, 5-mer)
    Output: complement nucleotide sequence
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': '_'}
    return ''.join(complement[base] for base in reversed(seq))

# Function to generate the 2-mer count vector
def generate_2mer_vector(seq):
    """This function creates the list of 2-mers, and counts their occurrences in the whole sequence
    """
    # All possible 2-mers in lexicographic order
    possible_2mers = [a+b for a in "ACGT" for b in "ACGT"]
    # Count occurrences of each 2-mer in the sequence
    counter = Counter(seq[i:i+2] for i in range(len(seq)-1))
    return [counter.get(mer, 0) for mer in possible_2mers]

# Parse FASTA file and generate table
def parse_fasta_to_tsv(fasta_file, output_file):
    """This function compiles all the rows with the calculations"""
    result = []

    # Define 2-mer names for header
    possible_2mers = [a+b for a in "ACGT" for b in "ACGT"]
    header_columns = ["readID", "length", "5-mer", "Reverse complement"] + possible_2mers
    with open(fasta_file, 'r') as file:
        seq = ""
        read_id = ""
        for line in file:
            print(line)
            print(read_id)
            if line.startswith(">"):
                read_id = extract_read_id(line)
                if seq:
                    # Process the previous sequence
                    length = len(seq)
                    midpoint = length // 2
                    five_mer = seq[midpoint-2:midpoint+3]  # Extract the 5-mer centered on the midpoint
                    rev_complement = reverse_complement(five_mer)
                    vector_c = generate_2mer_vector(seq)
                    result.append([read_id, length, five_mer, rev_complement] + vector_c)
                # Start a new read
                seq = ""
            else:
                seq += line.strip()  # Concatenate sequence lines
                
        # Process the last sequence in the file
        if seq:
            length = len(seq)
            midpoint = length // 2
            five_mer = seq[midpoint-2:midpoint+3]  # Extract the 5-mer centered on the midpoint
            rev_complement = reverse_complement(five_mer)
            vector_c = generate_2mer_vector(seq)
            result.append([read_id, length, five_mer, rev_complement] + vector_c)
    
    # Write the output to a TSV file
    with open(output_file, 'w') as out_file:
        # Write header
        out_file.write("\t".join(header_columns) + "\n")
        # Write data
        for row in result:
            out_file.write("\t".join(map(str, row)) + "\n")


# Example usage
fasta_file = "Sequencing_Analysis_Assignment.fasta"
output_file = "parsed_fasta_data.tsv"
parse_fasta_to_tsv(fasta_file, output_file)


