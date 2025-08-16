import os
import requests
import xml.etree.ElementTree as ET
import asyncio
import aiofiles
import datetime
import json
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string: str) -> bool:
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

#from DataModal.tradeDetails import TradeDetailsModal
# Function to read a single file asynchronously
async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()
    return file_path, contents

# Main function to read all files in the folder
async def read_all_files(folder_path):
    tasks = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            tasks.append(read_file(full_path))

    results = await asyncio.gather(*tasks)
    return results

def parse_xml(file_path: str) -> str:
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # tradeDetailsModalObj = TradeDetailsModal(
    # insertiondate=datetime.datetime.now(),
    # System=root.findtext("Upstream/System"),
    # SystemID=root.findtext("Upstream/SystemID"),
    # tradeid=root.findtext("Tradedetails/tradeid"),
    # version=int(root.findtext("Tradedetails/version")),
    # Confirmation=root.findtext("Tradedetails/Confirmation"),
    # Nominal=int(root.findtext("Tradedetails/Nominal")),
    # Ccy=root.findtext("Tradedetails/Ccy"),
    # Sccy=root.findtext("Tradedetails/Sccy"),
    # SecurityData=root.findtext("Tradedetails/Security"),
    # EventData=root.findtext("Tradedetails/Event"),
    # Eventtype=root.findtext("Tradedetails/Eventtype"),
    # Productcategory=root.findtext("Tradedetails/Productcategory"),
    # Product=root.findtext("Tradedetails/Product"),
    # Asset=root.findtext("Tradedetails/Asset"),
    # Rate=float(root.findtext("Tradedetails/Rate")),
    # TD=datetime.datetime.strptime(root.findtext("Tradedetails/TD"), '%Y-%m-%dT%H:%M:%SZ'),
    # OED=datetime.datetime.strptime(root.findtext("Tradedetails/MD"), '%Y-%m-%dT%H:%M:%SZ'),
    # Cptycode=root.findtext("Tradedetails/Cptycode"),
    # CptyName=root.findtext("Tradedetails/CptyName"),
    # Party1=root.findtext("Party/Party1"),
    # Party2=root.findtext("Party/Party2"),
    # Party2email=root.findtext("Party/Party2email"),
    # Region=root.findtext("Party/Region")
    # )
        
    # print(f"TradeDetailsModal Object: {tradeDetailsModalObj}")
    
    data = {
        "insertiondate": datetime.datetime.now().isoformat(),
        "System": root.findtext("Upstream/System"),
        "SystemID": root.findtext("Upstream/SystemID"),
        "tradeid": root.findtext("Tradedetails/tradeid"),
        "version": int(root.findtext("Tradedetails/version")),
        "Confirmation": root.findtext("Tradedetails/Confirmation"),
        "Nominal": int(root.findtext("Tradedetails/Nominal")),
        "Ccy": root.findtext("Tradedetails/Ccy"),
        "Sccy": root.findtext("Tradedetails/Sccy"),
        "SecurityData": root.findtext("Tradedetails/Security"),
        "EventData": root.findtext("Tradedetails/Event"),
        "Eventtype": root.findtext("Tradedetails/Eventtype"),
        "Productcategory": root.findtext("Tradedetails/Productcategory"),
        "Product": root.findtext("Tradedetails/Product"),
        "Asset": root.findtext("Tradedetails/Asset"),
        "Rate": float(root.findtext("Tradedetails/Rate")),
        "TD": datetime.datetime.strptime(root.findtext("Tradedetails/TD"), '%Y-%m-%dT%H:%M:%SZ').isoformat(),
        "OED": datetime.datetime.strptime(root.findtext("Tradedetails/MD"), '%Y-%m-%dT%H:%M:%SZ').isoformat(),
        "Cptycode": root.findtext("Tradedetails/Cptycode"),
        "CptyName": root.findtext("Tradedetails/CptyName"),
        "Party1": root.findtext("Party/Party1"),
        "Party2": root.findtext("Party/Party2"),
        "Party2email": root.findtext("Party/Party2email"),
        "Region": root.findtext("Party/Region")
    }
    # Convert to JSON string
    json_object = json.dumps(data, indent=4)
    print(json_object)  # Ready to send via POST
    return json_object 
     
def AddXmlDataToDB(tradeDetailsModalObj: str):
        # Define the API endpoint
        url = 'http://localhost:5000/api/tradedetails'
        # Make the GET request
        response = requests.post(url, json=tradeDetailsModalObj)
        # Check if the request was successful
        if response.status_code >= 200:
            data = response.json()  # Parse JSON response
            print("Trade Details:", data)
            return data
        else:
            print(f"Error {response.status_code}: {response.text}")

def AddTradeDetailsToAffirmationDB(tradeId: int):
        # Define the API endpoint
        url = 'http://localhost:5000/api/insert'
        data = {
        "tradeID": tradeId,
         }
        # Make the GET request
        response = requests.post(url, json=data)
        # Check if the request was successful
        if response.status_code >= 200:
            data = response.json()  # Parse JSON response
            print("Trade Details:", data)
        else:
            print(f"Error {response.status_code}: {response.text}")
            
def GetJWTToken(tradeId: int):
        # Define the API endpoint
        url = 'http://localhost:5000/api/token'
        data = {
        "tradeID": tradeId,
         }
        # Make the GET request
        response = requests.post(url, json=data)
        # Check if the request was successful
        if response.status_code >= 200:
            data = response.json()  # Parse JSON response
            print("Trade Details:", data)
            return data['token']
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None