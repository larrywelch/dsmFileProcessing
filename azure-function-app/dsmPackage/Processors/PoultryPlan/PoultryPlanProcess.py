'''
    Logic for converting the fileoutpart1.xlsx to a csv file
'''

from io import BytesIO
import pandas as pd
from pandas import DataFrame
from azure.storage.blob import StorageStreamDownloader
from dsmPackage.AzureLib.azureUtil import azureUtil
from dsmPackage.AzureLib.azureFunctions import azureFunctions

def downloadBlob(azUtil: azureUtil, virtualFolder: str, fileName: str) -> DataFrame:
    path = "{z}/{f}"
    fullFileName = path.format(z=virtualFolder, f=fileName)
    downloader : StorageStreamDownloader  = azureFunctions.downloadBlob(azUtil, fullFileName)   
    return pd.read_excel(BytesIO(downloader.readall()), engine="openpyxl")

'''
    Download table/fileoutpart1.xlsx, convert to csv
    return a string to be saved as a csv file
'''
def process(azUtil: azureUtil,  virtualFolder: str) -> str :
    path = "{z}/{f}"
    fullFolderName = path.format(z=virtualFolder, f='tables')
    fileName = 'fileoutpart1.xlsx'
    fileToProcess = downloadBlob(azUtil, fullFolderName, fileName)
    
    # Remove escape chars
    fileToProcess.replace(to_replace=[r' _x000D_'], value=[''], regex=True, inplace=True)
    fileToProcess.columns = fileToProcess.columns.str.replace(' _x000D_', '').str.strip()

    # Rename the columns - Any change to this must also be made to the CreateSQLDBTable Utilitye
    #df.rename(columns={"A": "a", "B": "c"})
    fileToProcess.rename(
        columns=
        {
            "Leg%": "Leg% Koppel", 
            "Unnamed: 5": "Leg% Norm",
            "Eigewicht (gr)": "Eigewicht (gr) Koppel",
            "Unnamed: 7": "Eigewicht (gr) Norm",
            "Eimassa (gr)" : "Eimassa (gr) Koppel",
            "Unnamed: 9" : "Eimassa (gr) Norm",
            "Water per dag (I)" : "Water per dag (I) Koppel",
            "Unnamed: 11" : "Water per dag (I) Norm",
            "Voer per dag (gr)" : "Voer per dag (gr) Koppel",
            "Unnamed: 13" : "Voer per dag (gr) Norm",
            "vc" : "VC Koppel",
            "Unnamed: 15" : "VC Norm",
            "Voer poh cum. (kg)": "Voer poh cum. (kg) Koppel",
            "Unnamed: 17": "Voer poh cum. (kg) Norm",
            "Ei poh cum.": "Ei poh cum. Kopper",
            "Unnamed: 19": "Ei poh cum. Norm",
            "Eimassa poh cum. (kg)": "Eimassa poh cum. (kg) Kopper",
            "Unnamed: 21" : "Eimassa poh cum. (kg) Norm",
            "VC cum.": "VC cum. Koppel",
            "Unnamed: 23" : "VC cum. Norm",
            "Uitval % cum." : "Uitval % cum. Koppel",
            "Unnamed: 25" : "Uitval % cum. Norm",
            "Lichaamsgewicht (gr)": "Lichaamsgewicht (gr) Koppel",
            "Unnamed: 27" : "Lichaamsgewicht (gr) Norm"
        },
        inplace=True
    )
 
    return fileToProcess.to_csv(index=False, encoding="utf-8")
    