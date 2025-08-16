import os
import asyncio
import json
import shutil
#import requests
from SendEmail import send_email
from Utilities.FileOperation import  is_valid_xml,parse_xml, read_all_files, AddXmlDataToDB,AddTradeDetailsToAffirmationDB,GetJWTToken,AddTradeDetailsToAffirmationDB
#import requests
from SendEmail import CreateEmailBodySendEmail

#print(requests.get('https://www.example.com'))
# Path to the folder
FOLDER_PATH = r"C:\Users\Kiosk1\Code\Python\TradeXml\Input"
FOLDER_DestPATH = r"C:\Users\Kiosk1\Code\Python\TradeXml\Processed"
FOLDER_ErrorPATH = r"C:\Users\Kiosk1\Code\Python\TradeXml\Error"

# Run the async function
if __name__ == '__main__':

    #send_email("Test Subject", "mangesh.jambhulkar@deltacapita.com", "<h1>This is a test email</h1>")

    files_data = asyncio.run(read_all_files(FOLDER_PATH))
    for file_path, content in files_data:
        filename = os.path.basename(file_path)
        if not content.strip() or not is_valid_xml(content):
            shutil.move(file_path, FOLDER_ErrorPATH + "\\" + filename)
            print(f"Skipping empty/invalid file: {file_path}")
            continue
        parsedtradeDetailsModalObj = parse_xml(file_path)
        tradeIDDetailsResult=AddXmlDataToDB(parsedtradeDetailsModalObj)
        tradeID_PK=tradeIDDetailsResult["trade_id"]
        tradeID_PKDB=AddTradeDetailsToAffirmationDB(tradeID_PK)
        tokenData=GetJWTToken(tradeID_PK)
        emailBodydata=json.loads(parsedtradeDetailsModalObj)
        CreateEmailBodySendEmail(emailBodydata, tokenData)
        print(f"--- {file_path} ---\n{content[:100]}...\n")  # Print first 100 chars
        shutil.move(file_path, FOLDER_DestPATH + "\\" + filename)
        print(f"--- File Moved...\n")  # Print first 100 chars

