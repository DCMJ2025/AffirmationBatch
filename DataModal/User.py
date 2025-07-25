# -- Data model --
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    user_id: str
    name: str
    email: str
    age: Optional[int] = None