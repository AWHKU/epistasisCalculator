# Epistasis Calculator

The program epistasisCalc.py calculates the epistasis scores of combinatorial protein variants. See the book chapter  Structural Genomics from Springer Nature's Methods in Molecular Biology series on High-throughput Protein Engineering by Massively Parallel Combinatorial Mutagenesis for further references.

## Input
The input format is indicated as in epcalc_demo.csv. This program requires a csv input file and runs in Python 2.7.
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
python epistasisCalc.py [input csv file] [line where the first variant start] [number of modules]
```
To run the demo file
```
python epistasisCalc.py epcalc_demo.csv 5 4
```

## Output
The program outputs a csv file showing the expected and observed log2 enrichment scores, and the epistasis score.
```
# variant,module0,module1,module2,module3,expected,observed,epistasis score
1,RQ,K,ETQ,KR,-20.7729060596,-20.7729060596,0.0
2,RA,K,ETQ,KR,-20.9623185394,-21.5305559789,-0.568237439485
3,AQ,K,ETQ,KR,-20.1811133726,-18.4057353116,1.77537806099
4,AA,K,ETQ,KR,-20.9518703101,-21.4887630616,-0.536892751533
5,RQ,A,ETQ,KR,-20.9975342482,-21.6714188139,-0.673884565696
6,RA,A,ETQ,KR,-21.186946728,-20.6643943511,0.522552376849
7,AQ,A,ETQ,KR,-20.4057415612,-21.3447975496,-0.939055988402
8,AA,A,ETQ,KR,-21.1764984987,-20.8493895046,0.327108994106
9,RQ,K,ETA,KR,-20.4675750769,-19.5515821287,0.915992948187
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
