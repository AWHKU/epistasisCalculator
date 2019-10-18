import sys, math 
import pandas as pd
#import seaborn as sns

fn=sys.argv[1]
outfn=fn.split(".")[0]+"_output.csv"
heatfn=fn.split(".")[0]+"_heatmapIn.csv"
startln=int(sys.argv[2])-1
modules=int(sys.argv[3])
heatmap1, heatmap2=sys.argv[4], sys.argv[5]

def joinAA(aalist,modules):
 key=""
 for i in range (modules):
  key+=aalist[i]+","
 key=key.strip(",")
 return key

def enrichmentRatio(set):
 selected, total=float(set[0]), float(set[1])
 E=selected/total
 return E

def openFile(fn,startln,modules):
 obsDict={}
 file=open(fn,"r")
 for i in range (int(startln)):
  file.readline()
 for l in file:
  ln=l.strip("\r\n").split(",")
  if "LOW" in l and ln[0] == "1":
   print("Error, the wide type protein has low read!")
   sys.exit(0)
  if "LOW" not in l and ln[0] == "1":
   wtseq=ln[1:modules+1]
  if "LOW" not in l:
   key=joinAA(ln[1:],modules)
   setA, setB=ln[-4:-2], ln[-2:]
   meanlgE= math.log((0.5*(enrichmentRatio(setA)+enrichmentRatio(setB))),2.0)
   obsDict[key]=(ln[0],meanlgE,ln[1:modules+1])
 return (obsDict,wtseq)
Ofile=openFile(fn,startln,modules)
obsDict, wtseq=Ofile[0],Ofile[1]

def libVariants(modules,obsDict,wtseq):
 libs=[]
 for an in range (modules):
  libs.append({wtseq[an]:obsDict[joinAA(wtseq,modules)]})
  for dr in obsDict:
   if obsDict[dr][-1][an] != wtseq[an]:
    ew=0
    for i in range (modules):
     if obsDict[dr][-1][i] == wtseq[i]:
      ew+=1
    if ew == modules-1:
     libs[an][obsDict[dr][-1][an]]=obsDict[joinAA(obsDict[dr][-1],modules)]
 return libs
libs=libVariants(modules,obsDict,wtseq)

def epistasisOut(modules,libs,obsDict,outfn):
 outlns=[]
 for ng in obsDict:
  er, so=0, 0
  for ll in range (modules):
   if obsDict[ng][-1][ll] in libs[ll]:
    er+=libs[ll][obsDict[ng][-1][ll]][1]
    so+=1
  er=er/float(modules)
  epistasis=obsDict[ng][1]-er
  if so < 4:
   outlns.append((int(obsDict[ng][0]),obsDict[ng][0]+","+ng+"\r\n"))
  else:
   outlns.append((int(obsDict[ng][0]),obsDict[ng][0]+","+ng+","+str(er)+","+str(obsDict[ng][1])+","+str(epistasis)+"\r\n"))
  outlns.sort()
  outfile=open(outfn,"w")
  row="# variant"
  for i in range(modules):
   row+= ",module"+str(i)
  row+=",expected,observed,epistasis score"+"\r\n"
  outfile.write(row)
  for ln in outlns:
   outfile.write(ln[1])
  outfile.close()
epistasisOut(modules,libs,obsDict,outfn)

def genHeatmapIn(heatmap1,heatmap2,outfn,heatfn):
 file=open(outfn,"r")
 outfile=open(heatfn,"w")
 D1,D2=heatmap1.split(","),heatmap2.split(",")
 for ln in file:
  ln=ln.split(",")
  if len(ln) > 5:
   one,two="",""
   for i in D1:
    one+=ln[int(i)]+"_"
   one=one.strip("_")
   for j in D2:
    two+=ln[int(j)]+"_"
   two=two.strip("_")
   outfile.write(one+","+two+","+ln[-1])
 outfile.close()
genHeatmapIn(heatmap1,heatmap2,outfn,heatfn)
 
def genHeatmap(heatfn):
 alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 file=open(heatfn,"r")
 hpic=heatfn.split(".")[0].strip("In")+".xlsx"
 h=file.readline().strip("\r\n").split(",")
 mat=pd.read_csv(heatfn)
 mini, maxi= mat[h[2]].min(), mat[h[2]].max()
 mat=mat.pivot(h[0],h[1],h[2])
 shape=mat.shape
 dim='B2:'+alphabets[shape[1]]+str(shape[0]+1)
 excel_file=hpic
 sheet_name='Sheet1'
 writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
 mat.to_excel(writer, sheet_name=sheet_name)
 workbook=writer.book
 worksheet=writer.sheets[sheet_name]
 format1 = workbook.add_format({'bg_color':'gray'})
 worksheet.conditional_format(dim,{'type':'cell','criteria':'==','value': '""', 'format': format1})
 worksheet.conditional_format(dim,{'type':'3_color_scale','max_color':'red','min_color':'blue','mid_color':'white'})
 writer.save()
genHeatmap(heatfn)
