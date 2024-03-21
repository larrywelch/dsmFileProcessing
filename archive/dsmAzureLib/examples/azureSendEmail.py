#
# Use the Azure Library to perform functions
#

import os
from dsmAzureLib.emailUtil import emailUtil

def sendEmail():
  print('[sendEmail] sending email...')
  
    # Get environment variables
  emailSvcConnStr = os.environ.get('AZURE_EMAIL_SVC_CONNECTION_STRING')
  emailSvcSenderAddress = os.environ.get('AZURE_EMAIL_SVC_SENDER_ADDRESS')
  emailSvcSendToList = os.environ.get('AZURE_EMAIL_SVC_SEND_TO_LIST')
  
  assert emailSvcConnStr and emailSvcSenderAddress and emailSvcSendToList
  
  # Create the email notification object
  emn = emailUtil(emailSvcConnStr, emailSvcSenderAddress)
  emn.sendEmail('Email from the examples code', \
    'This email was sent from the examples code.', \
    emailSvcSendToList
    )
  
  print('[sendEmai] complete!')
  
def main():
 
  print('Executing sendEmail()...')
  sendEmail()
  print('')
  
  print('Complete.')
  
main()
