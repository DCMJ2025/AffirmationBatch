from dataclasses import dataclass
from datetime import datetime

@dataclass
class TradeDetailsModal:
    insertiondate: datetime
    System: str
    SystemID: str
    tradeid: str
    version: int
    Confirmation: str
    Nominal: int
    Ccy: str
    Sccy: str
    SecurityData: str
    EventData: str
    Eventtype: str
    Productcategory: str
    Product: str
    Asset: str
    Rate: float
    TD: datetime
    OED: datetime
    Cptycode: str
    CptyName: str
    Party1: str
    Party2: str
    Party2email: str
    Region: str