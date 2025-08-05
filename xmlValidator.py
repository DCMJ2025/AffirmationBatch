import os
import logging
from interfaces import XmlValidator
import xml.etree.ElementTree as ET

app_logger = logging.getLogger(__name__) 

class ConcreteXmlValidator(XmlValidator):

    def validate(self, file_path: str) -> bool:
        try:
            ET.parse(file_path)
            app_logger.info(f"XML file {os.path.basename(file_path)} is well-formed.")
            return True
        except ET.ParseError as e:
            app_logger.warning(f"Error parsing XML file {os.path.basename(file_path)}: {e}")
            return False