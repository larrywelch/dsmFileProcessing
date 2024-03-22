'''
    handler for the OnFileReadyForProcessing function
    
    Handler receives the source file name and uses it to retrieve the proper processor from the factory.
'''

import logging

# Import the processor factory
from dsmPackage.Processors.processorFactory import processorFactory

def OnProcessExtractedFilesHandler(sourceFileName: str, settings: dict[str, any]) -> Exception:
    ex = None
    
    logging.info('[OnProcessExtractedFilesHandler] entered, processing the source file...')
    logging.info(f" Source File Name:{sourceFileName}")
    processor = processorFactory.getProcessor(settings, sourceFileName)
    if (processor != None):
        ex = processor.OnProcessExtractedFiles(sourceFileName)
    else:
        ex = Exception(f"No Processor Found for {sourceFileName}.")
    return ex