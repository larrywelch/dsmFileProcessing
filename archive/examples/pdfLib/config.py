'''
    config.py - provides configuration values for the application.  Will use values found in environment variables, or defaults.
'''

import os

settings = {
    'PDF_SERVICES_CLIENT_ID': os.getenv('PDF_SERVICES_CLIENT_ID', '0dc643ef927c4fa184f8b99117b17235'),
    'PDF_SERVICES_CLIENT_SECRET': os.getenv('PDF_SERVICES_CLIENT_SECRET', 'p8e-VUKWlq_QHi-v0OSHLpJEFlc6E8Mi-BP5')
 }