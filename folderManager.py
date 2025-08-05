import os
import logging
from interfaces import FolderManager

app_logger = logging.getLogger(__name__) 

class ConcreteFolderManager(FolderManager):

    def ensure_folder_exists(self, path: str, folder_name: str) -> bool:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                app_logger.info(f"Created folder: {folder_name} at {path}")
                return True
            except OSError as e:
                app_logger.error(f"Error creating folder {folder_name} at {path}: {e}")
                return False
        app_logger.debug(f"Folder already exists: {folder_name} at {path}")
        return True