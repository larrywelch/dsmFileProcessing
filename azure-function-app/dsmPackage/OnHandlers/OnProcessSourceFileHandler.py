'''
    handler for the OnProcessSourceFileHandler function.  Uses the processorFactory to get a processor, returns 
'''

import azure.functions as func
import logging

# Import the processor factory
from dsmPackage.Processors.processorFactory import processorFactory

def OnProcessSourceFileHandler(sourceFileBlob : func.InputStream, settings, logger: logging) -> Exception:
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
