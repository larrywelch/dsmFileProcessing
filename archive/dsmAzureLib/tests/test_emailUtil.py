#
# Tests for the azure email notification class
#

import os
from dsmAzureLib.emailUtil import emailUtil

def test_createObject():
  em = emailUtil("", "")
  assert em != None
  
def test_createAddressEmptyList():
  em = emailUtil("", "")
  addresses = em.createAddresses(''.split(';'))
  assert addresses != None
  
  assert len(addresses) == 0
  
def test_createAddressSingleEmail():
  em = emailUtil("", "")
  addresses = em.createAddresses('bob@bob.com'.split(';'))
  assert addresses != None
  
  assert len(addresses) == 1
  
  for address in addresses:
    print('Address info:')
    print(' address: ', address['address'], ' displayName: ', address['displayName'])
    assert address['address'] and address['displayName']
    
def test_createAddressMultipleEmails():
  em = emailUtil("", "")
  addresses = em.createAddresses('bob@bob.com;sally@sally.com'.split(';'))
  assert addresses != None
  
  assert len(addresses) == 2
  
  for address in addresses:
    print('Address info:')
    print(' address: ', address['address'], ' displayName: ', address['displayName'])
    assert address['address'] and address['displayName']
    
def test_sendEmailTest():
  # Get environment variables
  emailSvcConnStr = os.environ.get('AZURE_EMAIL_SVC_CONNECTION_STRING')
  emailSvcSenderAddress = os.environ.get('AZURE_EMAIL_SVC_SENDER_ADDRESS')
  emailSvcSendToList = os.environ.get('AZURE_EMAIL_SVC_SEND_TO_LIST')
  
  assert emailSvcConnStr and emailSvcSenderAddress and emailSvcSendToList
  
  # Create the email notification object
  emn = emailUtil(emailSvcConnStr, emailSvcSenderAddress)
  emn.sendEmail('Email from Unit Test', \
    'This email was sent from the unit tests.', \
    emailSvcSendToList
    )