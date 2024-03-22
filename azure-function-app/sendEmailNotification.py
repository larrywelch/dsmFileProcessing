
from configuration import settings
from dsmPackage.AzureLib.emailUtil import emailUtil

EMAIL_NOTIFICATION_ENABLE = settings['email-notification-enabled']
EMAIL_SVC_CONN_STR = settings['email-notification-svc-conn-str']
EMAIL_SEND_TO_LIST = settings['email-notification-send-to-list']
EMAIL_SENDER_ADDRESS = settings['email-notification-sender-address']


def sendEmail(subject, message):  
  if (EMAIL_NOTIFICATION_ENABLE) :   
    util = emailUtil(EMAIL_SVC_CONN_STR, EMAIL_SENDER_ADDRESS) 
    util.sendEmail(subject, message, EMAIL_SEND_TO_LIST)