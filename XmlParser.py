import asyncio
from Utilities.FileOperation import read_all_files

# Path to the folder
FOLDER_PATH = r"C:\Users\Kiosk1\Code\Python\SampleXMLFiles"


# Run the async function
if __name__ == '__main__':
    files_data = asyncio.run(read_all_files(FOLDER_PATH))
    for file_path, content in files_data:
        print(f"--- {file_path} ---\n{content[:100]}...\n")  # Print first 100 chars
