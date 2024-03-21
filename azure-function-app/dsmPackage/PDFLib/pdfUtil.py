import io
import string
from io import BufferedReader
from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType

class pdfUtil :
      
    def __init__(self, clientId:string, clientSecret:string):
        self.__clientId = clientId
        self.__clientSecret = clientSecret
        self.__credentials = None
        
    def getCredentials(self) -> Credentials:
        if (self.__credentials != None): return self.__credentials
    
        if(self.__clientId and self.__clientSecret):
            self.__credentials = Credentials.service_principal_credentials_builder() \
        .with_client_id(self.__clientId).with_client_secret(self.__clientSecret).build();
        
        return self.__credentials
    
    def extractFile(self, pdfReader:BufferedReader) -> FileRef:
        #Create an ExecutionContext using credentials and create a new operation instance.
        execution_context = ExecutionContext.create(self.getCredentials())
        extract_pdf_operation = ExtractPDFOperation.create_new()

        #Set operation input from a source file.
        source = FileRef.create_from_stream(pdfReader, media_type="application/pdf")
        extract_pdf_operation.set_input(source)

        #Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_elements_to_extract([ExtractElementType.TEXT, ExtractElementType.TABLES]) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        #Execute the operation.
        result = extract_pdf_operation.execute(execution_context)
        
        # return the FileRef
        return result