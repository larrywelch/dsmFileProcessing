#
# Tests for the pdf util class
#

import os
from pdfLib.pdfUtil import pdfUtil

def test_createObject():
  util = pdfUtil("","")
  assert util != None

def test_getKnownEmptyCredentials():
  util = pdfUtil("", "")
  creds = util.getCredentials()
  assert creds == None
  
def test_getCredentials():
  # get the pdf env vars
  pdfSvcClientId = os.getenv('PDF_SERVICES_CLIENT_ID')  
  pdfSvcClientSecret = os.getenv('PDF_SERVICES_CLIENT_SECRET')
  assert pdfSvcClientId and pdfSvcClientSecret
    
  util = pdfUtil(pdfSvcClientId, pdfSvcClientSecret)
  creds = util.getCredentials()
  assert creds != None
  
def test_getBufferedReader():
  # get the pdf env vars
  pdfSvcClientId = os.getenv('PDF_SERVICES_CLIENT_ID')  
  pdfSvcClientSecret = os.getenv('PDF_SERVICES_CLIENT_SECRET')
  assert pdfSvcClientId and pdfSvcClientSecret
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir = os.path.join(base_path,'../sample-pdfs')
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print(fileName)
  
  util = pdfUtil(pdfSvcClientId, pdfSvcClientSecret)
  
  reader = util.getBufferedReader(fileName)
  assert reader != None
  reader.close()
  
def test_extractFile():
  # get the pdf env vars
  pdfSvcClientId = os.getenv('PDF_SERVICES_CLIENT_ID')  
  pdfSvcClientSecret = os.getenv('PDF_SERVICES_CLIENT_SECRET')
  assert pdfSvcClientId and pdfSvcClientSecret
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir =os.path.abspath(os.path.join(base_path,'../sample-pdfs'))
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print(fileName)
  
  # Create our pdf utility
  util = pdfUtil(pdfSvcClientId, pdfSvcClientSecret)
  
  # Get a reader for the sample file
  reader = util.getBufferedReader(fileName)
  assert reader != None

  # Have the utility extract the file - the resutls can be saved as a zip file
  fileRef = util.extractFile(reader)
  assert fileRef != None
  
  # Save as a zip file
  # zipFile = 'sample_pdf.zip'  
  # if os.path.isfile(zipFile):
  #   os.remove(zipFile)
    
  # fileRef.save_as(zipFile)
  