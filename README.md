# Epistasis Calculator

The sample_separator_v5.py can be used for demultiplexing sequencing data with multiple samples in a NGS run. It identifies sample ID and extracts barcodes for each sample from fastq files based on user-supplied sets of sample ID and user-defined parameters.

## Input
Two input files are needed: NGS data file in fastq format and a text file of sample ID. Sample ID should be written in the format of one ID for each line. The program then prompts the user to input user-defined parameters including barcode length, linker length and number of barcodes in one DNA construct. 
![Image](/images/s_1.png)

Sample ID format:
![Image](/images/s_2.png)

## Output
1. Text file
Extracted barcodes for each sample are exported as individual tab-delimited text file named with its sample ID. If the read begins with an expected sample ID, barcodes will be extracted and reads are written in rows. The first column contains barcodes representing the sample ID and the subsequent columns contain barcodes at different (nth) positions. The total number of columns depends on the number (n) of positions being mutated/barcoded in the study.
![Image](/images/s_3.png)

1. CSV file
It is a report showing the total read count for each sample in the sample ID text file.
![Image](/images/s_4.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
