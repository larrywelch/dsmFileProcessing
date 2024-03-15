
import os, io
from dsmFileProcessorLib.AgriStatsFileProcessor import AgriStatsFileProcessor
from dsmFileProcessorLib.PoultryPlanFileProcessor import PoultryPlanFileProcessor

def loopThroughProcessors():
    # Create a list of file processors   
    processors = [AgriStatsFileProcessor(), PoultryPlanFileProcessor()]

    print('looping through the processors...')
    for fp in processors:
        fp.onNewFile()
        fp.onFileReadyForProcessing()
        fp.onFinalResultsReadyForProcessing()
    return

'''
    testAgriStatProcessor - Test the processor using a sample file.
'''
def testAgriStatProcessor():
    print('[testAgriStatProcessor] entered...')

    # Define the connection string to the azure storage account
    blobConnStr = 'DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net'
    containerName = 'sample-files-extracted'
    virtualFolderName = '06-02-2023.zip'
    
    # Get our sample file
    base_path = os.path.dirname(os.path.realpath(__file__))
    samplesDir = os.path.join(base_path,'../sample-files')
    fileName = os.path.join(samplesDir, '06-02-2023.zip')
    with open(fileName, 'rb') as fh:
        buf = io.BytesIO(fh.read()) 
        processor = AgriStatsFileProcessor() 
        processor.onNewFile(buf, blobConnStr, containerName, virtualFolderName)
    
    print('[testAgriStatProcessor] complete.')
    return
   
def testPoultryProcessor():
    print('[testPoultryProcessor] entered...')
    
    # Define the connection string to the azure storage account
    blobConnStr = 'DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net'
    containerName = 'sample-files-extracted'
    virtualFolderName = 'Performance data Mans 20230718.pdf'
    
    # Get our sample file
    base_path = os.path.dirname(os.path.realpath(__file__))
    samplesDir = os.path.join(base_path,'../sample-files')
    fileName = os.path.join(samplesDir, 'Performance data Mans 20230718.pdf')
    with open(fileName, 'rb') as fh:
        buf = io.BytesIO(fh.read()) 
        processor = PoultryPlanFileProcessor() 
        processor.onNewFile(buf, blobConnStr, containerName, virtualFolderName)
    
    print('[testAgriStatProcessor] complete.')
    
    print('[testPoultryProcessor] complete.')
    return

def main():
    print('Starting...')  

    #testAgriStatProcessor()
    
    testPoultryProcessor()
        
main()