import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from typing import Optional, Any


# @dataclass
# class Upstream:
#     System: str
#     SystemID: str

@dataclass
class TradeDetails:
    tradeid: str
    # version: str
    # Confirmation: str
    # Nominal: str
    # Ccy: str
    # Sccy: str
    # Security: str
    # Event: str
    # Eventtype: str
    # Productcategory: str
    # Product: str
    Asset: str
    Rate: str
    TD: str
    # Cptycode: str
    # OED: Optional[str] = None
    # MD: Optional[str] = None 

@dataclass
class Party:
    # Party1: str
    # Party2: str
    Party2email: str
    # Region: str

@dataclass
class Trade:
    # upstream: Upstream
    trade_details: TradeDetails
    party: Party