'''
    handler for the OnProcessSourceFileHandler function
'''

import azure.functions as func
import logging

def OnProcessSourceFileHandler(inputBlob: func.InputStream, logger: logging) -> bool:
    return True
