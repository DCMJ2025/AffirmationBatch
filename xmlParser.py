import os
import logging
from Trades import TradeDetails, Party, Trade 
from typing import Optional, Any
import xml.etree.ElementTree as ET 

app_logger = logging.getLogger(__name__) 

class XmlParser:

    def parse_xml(self, file_path: str) -> Optional[Trade]:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            def findtext(element, tag, default='N/A'):
                found_element = element.find(tag)
                return found_element.text if found_element is not None else default

            # upstream_elem = root.find('Upstream')
            # upstream_data = Upstream(
            #     System=findtext(upstream_elem, 'System'),
            #     SystemID=findtext(upstream_elem, 'SystemID')
            # )
            
            trade_details_elem = root.find('Tradedetails')
            trade_details_data = TradeDetails(
                tradeid=findtext(trade_details_elem, 'tradeid'),
                # version=findtext(trade_details_elem, 'version'),
                # Confirmation=findtext(trade_details_elem, 'Confirmation'),
                # Nominal=findtext(trade_details_elem, 'Nominal'),
                # Ccy=findtext(trade_details_elem, 'Ccy'),
                # Sccy=findtext(trade_details_elem, 'Sccy'),
                # Security=findtext(trade_details_elem, 'Security'),
                # Event=findtext(trade_details_elem, 'Event'),
                # Eventtype=findtext(trade_details_elem, 'Eventtype'),
                # Productcategory=findtext(trade_details_elem, 'Productcategory'),
                # Product=findtext(trade_details_elem, 'Product'),
                Asset=findtext(trade_details_elem, 'Asset'),
                Rate=findtext(trade_details_elem, 'Rate'),
                TD=findtext(trade_details_elem, 'TD'),
                # OED=findtext(trade_details_elem, 'OED'),
                # MD=findtext(trade_details_elem, 'MD'),
                # Cptycode=findtext(trade_details_elem, 'Cptycode')
            )

            party_elem = root.find('Party')
            party_data = Party(
                # Party1=findtext(party_elem, 'Party1'),
                # Party2=findtext(party_elem, 'Party2'),
                Party2email=findtext(party_elem, 'Party2email'),
                # Region=findtext(party_elem, 'Region')
            )
            
            app_logger.info(f"Parsed XML file {os.path.basename(file_path)} successfully.")
            return Trade(trade_details=trade_details_data, party=party_data)
            
        except ET.ParseError as e:
            self.app_logger.error(f"Error parsing XML file {file_path}: {e}")
            return None
        except Exception as e:
            self.app_logger.exception(f"An unexpected error occurred while parsing {file_path}")
            return None