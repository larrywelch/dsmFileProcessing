#
# Email Notifications via Azure
#

import string
from azure.communication.email import EmailClient

class emailUtil() :
  def __init__(self, svcConnectionString: string, senderAddress: string):
      self.__svcConnectionString = svcConnectionString
      self.__sendAddress = senderAddress
      self.__pollerWaitTime = 10
      
  def createAddresses(self, recipientsList: list) -> list:
    addresses = []
    for recipient in recipientsList:
      # Make sure we have a recipient
      if recipient:
        addresses.append( 
          {
            "address": recipient,
            "displayName": recipient
          }
        )

    return addresses
  
  def sendEmail(self, subject: string, message: string, sendToList: string):
    # Send an email
    try:
      # Create the EmailClient object that you use to send Email messages.
      email_client = EmailClient.from_connection_string(self.__svcConnectionString)
      toAddresses = self.createAddresses(sendToList.split(';'))
      email_message = {
          "content": {
            "subject": subject,
            "plainText": message,
            "html" : f"<html><h1>{subject}</h1><br>{message}</html>"
          },
          "recipients" : {
            "to": toAddresses
          },
          "senderAddress": self.__sendAddress
        }

        # Send the email
      print('sending email...')
      poller = email_client.begin_send(email_message)

      time_elapsed = 0
      while not poller.done():
        print("Email send poller status: " + poller.status())

        poller.wait(self.__pollerWaitTime)
        time_elapsed += self.__pollerWaitTime

        if time_elapsed > 18 * self.__pollerWaitTime:
            raise RuntimeError("Polling timed out.")
        
        if poller.result()["status"] == "Succeeded":
          print(f"Successfully sent the email (operation id: {poller.result()['id']})")
        else:
          raise RuntimeError(str(poller.result()["error"]))

      print('email sent.')

    except Exception as ex:
      print(f'Exception sending email: {ex}')  
