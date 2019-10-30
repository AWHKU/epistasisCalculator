# Epistasis Calculator

The program epistasisCalc.py calculates the epistasis scores of combinatorial protein variants. See the book chapter  Structural Genomics from Springer Nature's Methods in Molecular Biology series on High-throughput Protein Engineering by Massively Parallel Combinatorial Mutagenesis for further references.
Tutorial: https://www.youtube.com/watch?v=32bAxORsvUA&feature=youtu.be

## Input
The input format is indicated as in epcalc_demo.csv. This program requires a csv input file and runs in Python 2.7.
The demo input is from https://www.nature.com/articles/s41592-019-0473-0 (G.C.G. Choi et al., Nat. Methods, 2019) and generates the heatmap equivalent to the sg5-on heatmap in Figure 4.
```
variant #,module 1,module 2,module 3,module 4,Bin A,unsorted,Bin A,unsorted
1,RQ,K,ETQ,KR,4450.26,1435.77,4284.28,1249.13
2,RA,K,ETQ,KR,1400.07,1847.80,3310.70,1641.19
3,AQ,K,ETQ,KR,642.39,983.92,1354.38,354.04
4,AA,K,ETQ,KR,1440.43,1566.68,2216.73,1880.55
5,RQ,A,ETQ,KR,2770.97,1896.66,1896.78,1762.74
6,RA,A,ETQ,KR,1662.72,1442.40,1682.18,1153.76
```

## Run
```
python epistasisCalc.py [input file] [line the first variant starts] [# of modules] [heatmap Dimension1] [heatmap Dimension2]
```
To run the demo file
```
python epistasisCalc.py epcalc_demo.csv 5 4 1,3 2,4
```

## Output
1. The program outputs a csv file showing the expected and observed log2 enrichment scores, and the epistasis score.
```
# variant,module1,module2,module3,module4,expected,observed,epistasis score
1,RQ,ETQ,K,KR,0,0,0.0
2,RA,ETQ,K,KR,0.946801128994,0.946801128994,0.0
3,AQ,ETQ,K,KR,1.11476322013,1.11476322013,0.0
4,AA,ETQ,K,KR,0.755807978993,0.755807978993,0.0
5,RQ,ETQ,A,KR,1.05216244686,1.05216244686,0.0
6,RA,ETQ,A,KR,1.99896357585,-0.167208855943,-2.2
7,AQ,ETQ,A,KR,2.16692566698,0.87895350402,-1.3
8,AA,ETQ,A,KR,1.80797042585,-0.812034285604,-2.6
9,RQ,ETA,K,KR,1.0971081258,1.0971081258,0.0
```
2. The program outputs a csv file, which is used as the input for heatmap generation. Column 1 contains the indicated modules in [heatmap Dimension1], and Column 2 contains the indicated modules in [heatmap Dimension2].
```
RA_ETQ,A_KR,-2.2
AQ_ETQ,A_KR,-1.3
AA_ETQ,A_KR,-2.6
RQ_ETA,K_KR,
RA_ETA,K_KR,
AQ_ETA,K_KR,
AA_ETA,K_KR,
RQ_ETA,A_KR,-2.5
RA_ETA,A_KR,-1.4
AQ_ETA,A_KR,-2.9
AA_ETA,A_KR,-1.5
```
3. The heatmap (an Excel matrix) of the calcuated epistasis scores for each combination.
![Image](heatmap_pic.png)

## Note
csv files can be opened using excel or other spreadsheet softwares.

## License
[MIT](https://choosealicense.com/licenses/mit/)
