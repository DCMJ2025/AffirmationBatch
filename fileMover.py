import os
import logging
from interfaces import FileMover
import shutil

app_logger = logging.getLogger(__name__)

class ConcreteFileMover(FileMover):

    def move_file(self, source_path: str, destination_path: str) -> bool:
        try:
            shutil.move(source_path, destination_path)
            app_logger.info(f'Successfully moved file: {os.path.basename(source_path)} to {destination_path}')
            return True
        except Exception as e:
            app_logger.error(f'Error moving file {os.path.basename(source_path)} to {destination_path}: {e}')
            return False