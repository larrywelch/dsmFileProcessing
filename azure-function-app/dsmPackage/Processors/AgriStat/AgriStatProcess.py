'''
    process.py  Logic for processing the AgriStat excel files. 
'''
from io import BytesIO
import pandas as pd
from pandas import DataFrame
from azure.storage.blob import StorageStreamDownloader
from dsmPackage.AzureLib.azureUtil import azureUtil
from dsmPackage.AzureLib.azureFunctions import azureFunctions

'''
    downloadBlob - Download a blob from an Azure Storage Container, and then return the DataFrame
'''
def downloadBlob(azUtil: azureUtil, virtualFolder: str, fileName: str) -> DataFrame:
    path = "{z}/{f}"
    fullFileName = path.format(z=virtualFolder, f=fileName)
    downloader : StorageStreamDownloader  = azureFunctions.downloadBlob(azUtil, fullFileName)   
    return pd.read_excel(BytesIO(downloader.readall()), engine="openpyxl")

'''
    process - process the azure blob, which is an excel file, using the script originally created by Chelsea
'''
def process(azUtil: azureUtil,  virtualFolder: str) :
    ###logging.info("Starting Chelsea's logic...")
    w2= downloadBlob(azUtil, virtualFolder, "WEEK_W2.XLSX") # pd.read_excel(containerClient.download_blob(f"{virtualFolderName}/WEEK_W2.XLSX").readall(), engine="openpyxl")
    w3= downloadBlob(azUtil, virtualFolder, "WEEK_W3.XLSX") # pd.read_excel("WEEK_W3.XLSX", engine="openpyxl")
    w4= downloadBlob(azUtil, virtualFolder, "WEEK_W4.XLSX") #pd.read_excel("WEEK_W4.XLSX", engine="openpyxl")
    w5= downloadBlob(azUtil, virtualFolder, "WEEK_W5.XLSX") #pd.read_excel("WEEK_W5.XLSX", engine="openpyxl")
    #w5a= pd.read_excel("WEEK_W5a.XLSX", engine="openpyxl")
    #w5aALT= pd.read_excel("WEEK_W5aALT.XLSX", engine="openpyxl")
    w5b= downloadBlob(azUtil, virtualFolder, "WEEK_W5b.XLSX") #pd.read_excel("WEEK_W5b.XLSX", engine="openpyxl")
    w6= downloadBlob(azUtil, virtualFolder, "WEEK_W6.XLSX") #pd.read_excel("WEEK_W6.XLSX", engine="openpyxl")
    w7= downloadBlob(azUtil, virtualFolder, "WEEK_W7.XLSX") #pd.read_excel("WEEK_W7.XLSX", engine="openpyxl")
    #w7a= pd.read_excel("WEEK_W7a.XLSX", engine="openpyxl")
    w7b= downloadBlob(azUtil, virtualFolder, "WEEK_W7b.XLSX") #pd.read_excel("WEEK_W7b.XLSX", engine="openpyxl")
    #w8= pd.read_excel("WEEK_W8.XLSX", engine="openpyxl")

    #On all data sheets delete rows 2 through 6
    ##logging.info("On all data sheets delete rows 2 through 6")
    w2.drop(index=[0,1,2,3,4], inplace=True)
    w3.drop(index=[0,1,2,3,4], inplace=True)
    w4.drop(index=[0,1,2,3,4], inplace=True)
    w5.drop(index=[0,1,2,3,4], inplace=True)
    #w5a.drop(index=[0,1,2,3,4], inplace=True)
    #w5aALT.drop(index=[0,1,2,3,4], inplace=True)
    w5b.drop(index=[0,1,2,3,4], inplace=True)
    w6.drop(index=[0,1,2,3,4], inplace=True)
    w7.drop(index=[0,1,2,3,4], inplace=True)
    #w7a.drop(index=[0,1,2,3,4], inplace=True)
    w7b.drop(index=[0,1,2,3,4], inplace=True)
    #w8.drop(index=[0,1,2,3,4], inplace=True)

    #On all data sheets delete all rows missing a "D" under the Type column
    ##logging.info("On all data sheets delete all rows missing a D under the Type column")
    w2= w2.loc[w2['TYPE'] == "D"]
    w3= w3.loc[w3['TYPE'] == "D"]
    w4= w4.loc[w4['TYPE'] == "D"]
    w5= w5.loc[w5['TYPE'] == "D"]
    #w5a= w5a.loc[w5a['TYPE'] == "D"]
    #w5aALT= w5aALT.loc[w5aALT['TYPE'] == "D"]
    w5b= w5b.loc[w5b['TYPE'] == "D"]
    w6= w6.loc[w6['TYPE'] == "D"]
    w7= w7.loc[w7['TYPE'] == "D"]
    #w7a= w7a.loc[w7a['TYPE'] == "D"]
    w7b= w7b.loc[w7b['TYPE'] == "D"]
    #w8= w8.loc[w8['TYPE'] == "D"]

    #rename columns in w2
    ##logging.info("rename columns in w2")
    w2.drop(columns=['A', 'F', 'H', 'I', 'J', 'K','L', 'N', 'S', 'W', 'X','BWRNG'], inplace=True)
    #w2 = w2.rename({"A" : "live production variance"}, axis = 1)
    w2 = w2.rename({"B" : "live production cost"}, axis = 1)
    w2 = w2.rename({"C" : "chick cost"}, axis = 1)
    w2 = w2.rename({"D" : "house cost"}, axis = 1)
    w2 = w2.rename({"E" : "feed ingr cost"}, axis = 1)
    #w2 = w2.rename({"F" : "mill deliv cost"}, axis = 1)
    w2 = w2.rename({"G" : " vaccine medicat cost"}, axis = 1)
    #w2 = w2.rename({"H" : "catch haul cost"}, axis = 1)
    #w2 = w2.rename({"I" : "superv cost"}, axis = 1)
    #w2 = w2.rename({"J" : "misc cost"}, axis = 1)
    #w2 = w2.rename({"K" : "dept overhd cost"}, axis = 1)
    #w2 = w2.rename({"L" : "wb & fld parts condemn actual"}, axis = 1)
    w2 = w2.rename({"M" : "doa cost actual"}, axis = 1)
    #w2 = w2.rename({"N" : "bird weight"}, axis = 1)
    #w2 = w2.rename({"BWRNG" : "bird weight range"}, axis = 1)
    w2 = w2.rename({"O" : "age"}, axis = 1)
    w2 = w2.rename({"P" : "% livability"}, axis = 1)
    w2 = w2.rename({"Q" : "calorie conver"}, axis = 1)
    #w2 = w2.rename({"S" : "ingred own var"}, axis = 1)
    #w2 = w2.rename({"W" : "volume birds"}, axis = 1)
    #w2 = w2.rename({"X" : "pounds"}, axis = 1)

    #rename columns in w3
    ##logging.info("#rename columns in w3")
    w3.drop(columns=['A','B','D','E','J','K','M','N','P', 'C', 'F', 'G', 'H', 'I', 'L', 'O', 'T','BWRNG'], inplace=True)
    #w3 = w3.rename({"A" : "performance index var"}, axis = 1)
    #w3 = w3.rename({"B" : "performance index var cents/lb"}, axis = 1)
    #w3 = w3.rename({"C" : "chick cost $.42 &bw wt rk"}, axis = 1)
    #w3 = w3.rename({"D" : "chick cost $.42 &bw wt cent/lb"}, axis = 1)
    #w3 = w3.rename({"E" : "42-mort"}, axis = 1)
    #w3 = w3.rename({"F" : "feed cost @300 cal cost"}, axis = 1)
    #w3 = w3.rename({"G" : "feed cost @300 cal cost cent/lb"}, axis = 1)
    #w3 = w3.rename({"H" : "feed cost @300 cal cost adj c/lb"}, axis = 1)
    #w3 = w3.rename({"I" : "whole bird condem @ $.46"}, axis = 1)
    #w3 = w3.rename({"J" : "cent/lb"}, axis = 1)
    #w3 = w3.rename({"K" : "whole bird condem @ $.46 %condem"}, axis = 1)
    #w3 = w3.rename({"L" : "field parts condem @ $.46 rk"}, axis = 1)
    #w3 = w3.rename({"M" : "field parts condem @ $.46 cents/lb"}, axis = 1)
    #w3 = w3.rename({"N" : "field parts condem @ $.46 %condem"}, axis = 1)
    #w3 = w3.rename({"O" : "doa @ $.46 rk"}, axis = 1)
    #w3 = w3.rename({"P" : "doa @ $.46 cent/lb"}, axis = 1)
    w3 = w3.rename({"Q" : "doa @ $.46 %doa"}, axis = 1)
    #w3 = w3.rename({"T" : "bird wt"}, axis = 1)
    #w3 = w3.rename({"BWRNG" : "body weight range"}, axis = 1)
    w3 = w3.rename({"U" : "age"}, axis = 1)
    w3 = w3.rename({"V" : "days to @bw lb"}, axis = 1)
    w3 = w3.rename({"W" : "down time"}, axis = 1)

    #rename columns in w4
    #logging.info("rename columns in w4")
    w4.drop(columns=['A','B','C', 'D', 'E','F','G','I', 'K','M','O','Q','S','Z','AB','U', 'BWRNG', 'X'], inplace=True)
    #w4 = w4.rename({"A" : "total mort loss % & cal conv loss/lv lb variance"}, axis = 1)
    #w4 = w4.rename({"B" : "total mort loss % & cal conv loss/lv lb %"}, axis = 1)
    #w4 = w4.rename({"C" : "total mort loss % & cal conv loss/lv lb cal"}, axis = 1)
    #w4 = w4.rename({"D" : "mort loss %42 days cal conv loss/lv lb rank"}, axis = 1)
    #w4 = w4.rename({"E" : "mort loss %42 days cal conv loss/lv lb var"}, axis = 1)
    #w4 = w4.rename({"F" : "mort loss %42 days cal conv loss/lv lb %"}, axis = 1)
    #w4 = w4.rename({"G" : "mort loss %42 days cal conv loss/lv lb cal"}, axis = 1)
    w4 = w4.rename({"H" : "loss 0-7 days %"}, axis = 1)
    #w4 = w4.rename({"I" : "loss 0-7 days cal"}, axis = 1)
    w4 = w4.rename({"J" : "loss 8-14 days %"}, axis = 1)
    #w4 = w4.rename({"K" : "loss 8-14 days cal"}, axis = 1)
    w4 = w4.rename({"L" : "loss 15-21 days %"}, axis = 1)
    #w4 = w4.rename({"M" : "loss 15-21 days cal"}, axis = 1)
    w4 = w4.rename({"N" : "loss 22-28 days %"}, axis = 1)
    #w4 = w4.rename({"O" : "loss 22-28 days cal"}, axis = 1)
    w4 = w4.rename({"P" : "loss 29-35 days %"}, axis = 1)
    #w4 = w4.rename({"Q" : "loss 29-35 days cal"}, axis = 1)
    w4 = w4.rename({"R" : "loss 36-42 days %"}, axis = 1)
    #w4 = w4.rename({"BWRNG" : "body weight range"}, axis = 1)
    #w4 = w4.rename({"S" : "loss 36-42 days cal"}, axis = 1)
    w4 = w4.rename({"Y" : "loss 43-49 days %"}, axis = 1)
    #w4 = w4.rename({"Z" : "loss 43-49 days cal"}, axis = 1)
    w4 = w4.rename({"AA" : "loss 50-56 days %"}, axis = 1)
    #w4 = w4.rename({"AB" : "loss 50-56 days cal"}, axis = 1)
    w4 = w4.rename({"T" : "loss after 56 days %"}, axis = 1)
    #w4 = w4.rename({"U" : "loss after 56 days cal"}, axis = 1)
    w4 = w4.rename({"W" : "age"}, axis = 1)
    #w4 = w4.rename({"X" : "bird wt"}, axis = 1)

    #rename columns in w5
    #logging.info("rename columns in w5")
    w5.drop(columns=['A', 'C','D','E', 'F', 'BWRNG', 'G','H', 'I', 'J', 'N', 'O','P', 'R','S', 'T', 'V', 'Y', 'AD', 'AE','AF'], inplace=True)
    #w5 = w5.rename({"A" : "act feed cost/lb meat var"}, axis = 1)
    w5 = w5.rename({"B" : "act feed cost/lb meat indred cost"}, axis = 1)
    #w5 = w5.rename({"C" : "act feed cost/lb meat indred w/mill & del"}, axis = 1)
    #w5 = w5.rename({"D" : "act feed cost/lb meat indred rk"}, axis = 1)
    #w5 = w5.rename({"E" : "act feed cost/lb meat indred adj wt & own"}, axis = 1)
    #w5 = w5.rename({"F" : "effect of own xanth wt per lb vs avg total"}, axis = 1)
    #w5 = w5.rename({"G" : "effect of own xanth wt per lb vs avg own & xan"}, axis = 1)
    #w5 = w5.rename({"H" : "effect of own xanth wt per lb vs avg wt"}, axis = 1)
    #w5 = w5.rename({"I" : "actual feed efficiency rk"}, axis = 1)
    #w5 = w5.rename({"J" : "actual feed efficiency var"}, axis = 1)
    w5 = w5.rename({"K" : "actual feed efficiency actual calorie"}, axis = 1)
    w5 = w5.rename({"L" : "actual feed efficiency actual conv"}, axis = 1)
    w5 = w5.rename({"M" : "calorie level"}, axis = 1)
    #w5 = w5.rename({"N" : "actual feed cost rk"}, axis = 1)
    #w5 = w5.rename({"O" : "actual feed cost var"}, axis = 1)
    #w5 = w5.rename({"P" : "cost/1500"}, axis = 1)
    w5 = w5.rename({"Q" : "actual feed cost/ton"}, axis = 1)
    #w5 = w5.rename({"R" : "actual feed cost mill & del"}, axis = 1)
    #w5 = w5.rename({"BWRNG" : "body weight range"}, axis = 1)
    #w5 = w5.rename({"S" : "actual feed cost with m&d"}, axis = 1)
    #w5 = w5.rename({"T" : "formula cost vs actual"}, axis = 1)
    #w5 = w5.rename({"V" : "% males"}, axis = 1)
    w5 = w5.rename({"W" : "% mort"}, axis = 1)
    w5 = w5.rename({"X" : "age"}, axis = 1)
    #w5 = w5.rename({"Y" : "bird wt"}, axis = 1)
    #w5 = w5.rename({"AD" : "live cost adj wt, own, xanth, & no live haul rk"}, axis = 1)
    #w5 = w5.rename({"AE" : "live cost adj wt, own, xanth, & no live haul var"}, axis = 1)
    #w5 = w5.rename({"AF" : "live cost adj wt, own, xanth, & no live haul cent/lb"}, axis = 1)

    #rename columns in w5b
    #logging.info("rename columns in w5b")
    w5b.drop(columns=['A','B', 'D', 'E', 'BWRNG', 'G','K','L', 'M', 'N', 'O', 'P', 'Q', 'R','U','V', 'W', 'Y'], inplace=True)
    #w5b = w5b.rename({"A" : "fd ingred cost/lb meat var"}, axis = 1)
    #w5b = w5b.rename({"B" : "fd ingred cost/lb meat adj wt & own"}, axis = 1)
    w5b = w5b.rename({"C" : "fd ingred cost/lb meat actual"}, axis = 1)
    #w5b = w5b.rename({"D" : "feed efficiency rk"}, axis = 1)
    #w5b = w5b.rename({"E" : "feed efficiency var"}, axis = 1)
    w5b = w5b.rename({"F" : "feed efficiency adj to @bw lb"}, axis = 1)
    #w5b = w5b.rename({"G" : "feed efficiency adj"}, axis = 1)
    w5b = w5b.rename({"H" : "feed efficiency actual cal/lb"}, axis = 1)
    w5b = w5b.rename({"I" : "feed efficiency adj conv"}, axis = 1)
    w5b = w5b.rename({"J" : "feed efficiency actual conv"}, axis = 1)
    #w5b = w5b.rename({"K" : "feed efficiency cal level"}, axis = 1)
    #w5b = w5b.rename({"L" : "feed efficiency eff. on cent/lb mt"}, axis = 1)
    #w5b = w5b.rename({"M" : "feed efficiency $/ton equal"}, axis = 1)
    #w5b = w5b.rename({"N" : "feed efficiency mort eff on cal"}, axis = 1)
    #w5b = w5b.rename({"O" : "grower calorie conv.p rk"}, axis = 1)
    #w5b = w5b.rename({"P" : "grower calorie conv.p vs co. avg"}, axis = 1)
    #w5b = w5b.rename({"BWRNG" : "body weight range"}, axis = 1)
    #w5b = w5b.rename({"Q" : "grower calorie conv.p top 25%"}, axis = 1)
    #w5b = w5b.rename({"R" : "grower calorie conv.p spread"}, axis = 1)
    w5b = w5b.rename({"S" : "bird density sq ft place"}, axis = 1)
    w5b = w5b.rename({"T" : "bird density sq ft kill"}, axis = 1)
    #w5b = w5b.rename({"U" : "bird density lbs/sq ft"}, axis = 1)
    #w5b = w5b.rename({"V" : "condemn wb & feild parts"}, axis = 1)
    #w5b = w5b.rename({"W" : "% males"}, axis = 1)
    w5b = w5b.rename({"X" : "age"}, axis = 1)
    #w5b = w5b.rename({"Y" : "bird wt"}, axis = 1)

    #rename columns in w6
    #logging.info("rename columns in w6")
    w6.drop(columns=['A', 'B', 'C','E','F','I','J','K','N','O','P','U','T','S', 'BWRNG', 'Y'], inplace=True)
    #w6 = w6.rename({"A" : "eff feed sched/avg $/ton"}, axis = 1)
    #w6 = w6.rename({"B" : "eff feed sched/avg req cal"}, axis = 1)
    #w6 = w6.rename({"C" : "eff feed sched/avg cal var"}, axis = 1)
    w6 = w6.rename({"D" : "prestart & start feed lbs fed"}, axis = 1)
    #w6 = w6.rename({"E" : "prestart & start feed % fed"}, axis = 1)
    #w6 = w6.rename({"F" : "prestart & start feed days fed"}, axis = 1)
    w6 = w6.rename({"G" : "starter $/ton"}, axis = 1)
    w6 = w6.rename({"H" : "grower feeds lbs fed"}, axis = 1)
    #w6 = w6.rename({"I" : "grower feeds % fed"}, axis = 1)
    #w6 = w6.rename({"J" : "grower feeds begin age"}, axis = 1)
    #w6 = w6.rename({"K" : "grower feeds days fed"}, axis = 1)
    w6 = w6.rename({"L" : "grower feeds cost $/ton"}, axis = 1)
    w6 = w6.rename({"M" : "first withdraw feeds lbs fed"}, axis = 1)
    #w6 = w6.rename({"N" : "first withdraw feeds % fed"}, axis = 1)
    #w6 = w6.rename({"O" : "first withdraw feeds begin age"}, axis = 1)
    #w6 = w6.rename({"P" : "first withdraw feeds days fed"}, axis = 1)
    #w6 = w6.rename({"BWRNG" : "body weight range"}, axis = 1)
    w6 = w6.rename({"Q" : "first withdraw feeds cost $/ton"}, axis = 1)
    w6 = w6.rename({"R" : "final withdraw feeds lbs fed"}, axis = 1)
    #w6 = w6.rename({"U" : "final withdraw feeds days fed"}, axis = 1)
    #w6 = w6.rename({"T" : "final withdraw feeds begin age"}, axis = 1)
    #w6 = w6.rename({"S" : "final withdraw feeds % fed"}, axis = 1)
    w6 = w6.rename({"V" : "final withdraw feeds cost $/ton"}, axis = 1)
    w6 = w6.rename({"W" : "total lbs fed/bird"}, axis = 1)
    w6 = w6.rename({"X" : "age"}, axis = 1)
    #w6 = w6.rename({"Y" : "bird wt"}, axis = 1)

    #rename columns in w7
    #logging.info("rename columns in w7")
    w7.drop(columns=['A','B','C','D','F','G','H','I','N','O','P', 'BWRNG'], inplace=True)
    #w7 = w7.rename({"A" : "fd ingred cost/lb meat adj wt & own"}, axis = 1)
    #w7 = w7.rename({"B" : "calorie cost-adj own/xan"}, axis = 1)
    #w7 = w7.rename({"C" : "cal per lb meat adj @bw"}, axis = 1)
    #w7 = w7.rename({"D" : "days to @bw"}, axis = 1)
    w7 = w7.rename({"E" : "age"}, axis = 1)
    #w7 = w7.rename({"F" : "actual weight"}, axis = 1)
    #w7 = w7.rename({"G" : "days starter prestr"}, axis = 1)
    w7 = w7.rename({"H" : "days grower feeds"}, axis = 1)
    w7 = w7.rename({"I" : "days w/d feeds"}, axis = 1)
    w7 = w7.rename({"J" : "avg cal level"}, axis = 1)
    w7 = w7.rename({"K" : "% protein per 1500"}, axis = 1)
    w7 = w7.rename({"L" : "% lysine per 1500"}, axis = 1)
    w7 = w7.rename({"M" : "% TSAA per 1500"}, axis = 1)
    #w7 = w7.rename({"N" : "% trypto per 1500"}, axis = 1)
    #w7 = w7.rename({"O" : "% argine per 1500"}, axis = 1)
    #w7 = w7.rename({"P" : "% threon per 1500"}, axis = 1)
    #w7 = w7.rename({"BWRNG" : "body weight range"}, axis = 1)
    w7 = w7.rename({"Q" : "% a.phos per 1500"}, axis = 1)
    w7 = w7.rename({"R" : "% calcium per 1500"}, axis = 1)
    w7 = w7.rename({"S" : "% animal protein"}, axis = 1)
    w7 = w7.rename({"T" : "% added fat"}, axis = 1)

    #rename columns in w7b
    #logging.info("rename columns in w7b")
    w7b.drop(columns=['A','B', 'D', 'E', 'BWRNG', 'M', 'N','U', 'W'], inplace=True)
    #w7b = w7b.rename({"A" : "field condem w/b & field parts var"}, axis = 1)
    #w7b = w7b.rename({"B" : "field condem w/b & field parts cent/lb"}, axis = 1)
    w7b = w7b.rename({"C" : "field condem w/b & field parts %"}, axis = 1)
    #w7b = w7b.rename({"D" : "w/b disease condemn % rk"}, axis = 1)
    #w7b = w7b.rename({"E" : "w/b disease condemn % var"}, axis = 1)
    w7b = w7b.rename({"F" : "w/b disease condemn % total wb%"}, axis = 1)
    #w7b = w7b.rename({"M" : "parts condemned rk"}, axis = 1)
    #w7b = w7b.rename({"N" : "parts condemned var"}, axis = 1)
    w7b = w7b.rename({"O" : "parts condemned 50% field"}, axis = 1)
    #w7b = w7b.rename({"BWRNG" : "body weight range"}, axis = 1)
    #w7b = w7b.rename({"U" : "usda inspect area"}, axis = 1)
    w7b = w7b.rename({"V" : "age"}, axis = 1)
    #w7b = w7b.rename({"W" : "bird wt"}, axis = 1)

    #merge
    #logging.info("Merging and dropping duplicates....")
    w23=pd.merge_ordered(w2, w3, fill_method="ffill", on=['ENDPERIOD','age'])
    w45=pd.merge_ordered(w4, w5, fill_method="ffill", on=['ENDPERIOD','age'])
    w5b6=pd.merge_ordered(w5b, w6, fill_method="ffill", on=['ENDPERIOD','age'])
    w77b=pd.merge_ordered(w7, w7b, fill_method="ffill", on=['ENDPERIOD','age'])

    #drop the duplicates for the values which we were not able to match
    w23.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)
    w45.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)
    w5b6.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)
    w77b.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)

    w2345=pd.merge_ordered(w23, w45, on=['ENDPERIOD','age'])
    w2345.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)

    w5b677b=pd.merge_ordered(w5b6, w77b, on=['ENDPERIOD','age'])
    w5b677b.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)

    #TODO - This returns a DataFrame - believe we can use it to push data directly to Cosmo DB - Will probably just write this to a new file for now
    w23455b677b=pd.merge_ordered(w5b677b, w2345, on=['ENDPERIOD','age'])
    w23455b677b.drop_duplicates(subset=['ENDPERIOD','age'], inplace=True)
    w23455b677b['ENDPERIOD']=w23455b677b['ENDPERIOD'].astype(str)

    #TODO This looks like the final step with the final data - need to confirm with Chelsea.
    #logging.info("Preparing final results...")
    #TODO Create a new blob and store the results
    return w23455b677b.to_csv(index=False, encoding="utf-8")
    # blobClient = container.get_blob_client(f"{virtualFolder}/final_results.csv")
    # blobClient.upload_blob(output, blob_type="BlockBlob", overwrite = True)
    # #logging.info("Uploaded finalResults.csv")

    # LOOKS TO BE A DUPLICATE OF THE SAME LOGIC BELOW - COMMENTING THIS OUT FOR NOW
    # def preprocess(x):
    #     x['ENDPERIOD']=x['ENDPERIOD'].astype(str)
    #     try:
    #         df = pd.merge(w5b677b, x)
    #         df.to_csv("3_agristats_jan2020_oct2022.csv", mode="a", index=False)
    #     except ValueError:
    #         print (x[['ENDPERIOD','age']])
    # reader = pd.read_csv("w2345.csv", chunksize=1000)

    # for r in reader:
    #     preprocess(r) 

    # File creation is commented out above - going to comment this out as well - sent email to Chelsea
    # def preprocess(x):
    #     x['ENDPERIOD']=x['ENDPERIOD'].astype(str)
    #     try:
    #         df = pd.merge(w5b677b, x, on=['ENDPERIOD','age'])
    #         df.to_csv("agristats_jan2020_oct2022.csv", mode="a", index=False)
    #     except ValueError:
    #         print (x[['ENDPERIOD','age']])
    # reader = pd.read_csv("w2345.csv", chunksize=1000)

    # for r in reader:
    #     preprocess(r) 
    #w5b677b=pd.merge(w5b6, w77b, on=['ENDPERIOD','age'])
