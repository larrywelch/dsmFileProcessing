#
#
#

from io import BufferedReader
import os
from dsmPdfLib.pdfUtil import pdfUtil

def getUtil() -> pdfUtil:
  print('[getUtil] entered...')
  
  # get the pdf env vars
  pdfSvcClientId = os.getenv('PDF_SERVICES_CLIENT_ID')  
  pdfSvcClientSecret = os.getenv('PDF_SERVICES_CLIENT_SECRET')
  assert pdfSvcClientId and pdfSvcClientSecret
  util = pdfUtil(pdfSvcClientId, pdfSvcClientSecret)
  
  print('[getUtil] success!')
  return util
 
def getBufferedReader(util: pdfUtil) -> BufferedReader:
  print('[getBufferedReader] Starting...')
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir =os.path.abspath(os.path.join(base_path,'../sample-pdfs'))
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print('[getBufferedReader] processing file: ', fileName)
  
  reader = util.getBufferedReader(fileName)
  assert reader != None
  
  print('[getBufferedReader] success!')
  return reader
  
def extract(reader: BufferedReader, util:pdfUtil):
  print('[extract] entered...')
  
  # Use the pdf utility to extract the file.  The results can be saved to a zip file
  fileRef = util.extractFile(reader)

  # Save the extract results to a zip file
  zipFile = 'sample_pdf.zip'  
  if os.path.isfile(zipFile):
    os.remove(zipFile)    
  fileRef.save_as(zipFile)
  print('[extract] success! Results saved to:', zipFile)

def main() :
  print('Executing getUtil()...')
  util = getUtil()
  print('')
  
  print('executing getBufferedReader()...')
  reader = getBufferedReader(util)
  print('')
  
  print('Executing extract()...')
  extract(reader, util)
  print('')
  
  print('Complete.')
  
main()