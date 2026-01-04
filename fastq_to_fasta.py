def fastq_to_fasta(fastq_file, fasta_file):
    # Open FASTQ file to read and FASTA file for writing
    with open(fastq_file, 'r') as fq, open(fasta_file, 'w') as fa:
        # Loop through each line in the FASTQ file
        for line in fq:
            # FASTQ header '@'
            if line.startswith('@'):
                # Read the sequence line
                seq = fq.readline().strip()

                # Skip two lines
                fq.readline()
                fq.readline()

                # Write FASTA header
                fa.write('>' + line[1:])

                # Write the sequence
                fa.write(seq + '\n')
if __name__ == "__main__":
    fastq_to_fasta("test.fastq", "test_output.fasta")