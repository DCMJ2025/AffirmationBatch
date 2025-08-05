import os
import logging
from dotenv import load_dotenv

from folderManager import ConcreteFolderManager
from xmlValidator import ConcreteXmlValidator
from fileMover import ConcreteFileMover

from SendEmail import extract_data

load_dotenv()

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"), 
        logging.StreamHandler()         
    ]
)
app_logger = logging.getLogger(__name__) 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_FOLDER = os.getenv('PROCESSED_FOLDER', 'processed_xmls')
BROKEN_XMLS = os.getenv('BROKEN_XMLS', 'broken_xmls')
SOURCE_FOLDER = os.getenv('SOURCE_FOLDER', 'C:\\XMLs')

PROCESSED_FOLDER_PATH = os.path.join(BASE_DIR, PROCESSED_FOLDER)
BROKEN_XMLS_PATH = os.path.join(BASE_DIR, BROKEN_XMLS)


def index(folder_path: str):


    folder_manager= ConcreteFolderManager()
    xml_validator= ConcreteXmlValidator()
    file_mover = ConcreteFileMover() 


    if not folder_manager.ensure_folder_exists(PROCESSED_FOLDER_PATH, PROCESSED_FOLDER):
        return
    if not folder_manager.ensure_folder_exists(BROKEN_XMLS_PATH, BROKEN_XMLS):
        return


    xml_files_processed= []
    files_moved_count= 0
    broken_xmls_count= 0

    if not folder_path:
        app_logger.error("No folder path provided")
        return
    elif not os.path.isdir(folder_path):
        app_logger.error(f"{folder_path} is not a valid directory")
        return
    app_logger.info(f"Scanning directory: {folder_path} for XML files.")
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith('.xml'):
                file_full_path = os.path.join(folder_path, filename)

                if xml_validator.validate(file_full_path):
                    extract_data(file_full_path)  
                    if file_mover.move_file(file_full_path, PROCESSED_FOLDER_PATH):
                        xml_files_processed.append(filename)
                        files_moved_count += 1
                                                                   
                else:
                    if file_mover.move_file(file_full_path, BROKEN_XMLS_PATH):
                        broken_xmls_count+= 1           

        if not xml_files_processed and files_moved_count== 0:
            app_logger.info(f'No valid XML files found or moved from "{folder_path}"')
        elif files_moved_count > 0:
            app_logger.info(f'Successfully moved {files_moved_count} XML files to "{PROCESSED_FOLDER_PATH}"')
        else:
            app_logger.info('No files were moved during this operation.')

                
    except Exception as e:
        app_logger.exception(f'An unexpected error occurred while scanning folder {folder_path}')

if __name__ == '__main__':

    if SOURCE_FOLDER:
        app_logger.info(f"Reading folder path from .env: {SOURCE_FOLDER}")
        index(SOURCE_FOLDER.strip()) 
    else:
        app_logger.error("Error: SOURCE FOLDER is not set in the .env file. Please add it with path to your XML folder")

    print("\nProcessing complete. Check 'app.log' for details")