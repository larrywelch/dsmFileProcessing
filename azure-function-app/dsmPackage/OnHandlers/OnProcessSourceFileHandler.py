'''
    handler for the OnProcessSourceFileHandler function.  
    
    Handler receives the source blob, which contains the source file name.  
    It uses the source file name to retrieve the proper processor from the factory.
    
'''

import azure.functions as func
import logging

# Import the processor factory
from dsmPackage.Processors.processorFactory import processorFactory

def OnProcessSourceFileHandler(sourceFileBlob : func.InputStream, settings: dict[str, any]) -> Exception:
    ex = None
    
    # name=container/filename or dsm-source-files/06-02-2023.zip or dsm-source-files/sample.pdf
    # fileName = 06-02-2023.zip - this is then used as the virtual folder where the zip file is extracted
    fileName = sourceFileBlob.name.split('/')[1]
    logging.info('[OnProcessSourceFileHandler] entered, processing the source file...')
    logging.info(f" Name:{sourceFileBlob.name}")
    
    processor = processorFactory.getProcessor(settings, sourceFileBlob.name)
    if (processor != None):
        ex = processor.onProcessSourceFile(sourceFileBlob)
    else:
        ex = Exception(f"No Processor Found for {sourceFileBlob.name}.")
    
    return ex
