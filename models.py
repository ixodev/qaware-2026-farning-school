from typing import Optional

from pydantic import BaseModel


class Autoteilbeschreibung(BaseModel):
    category: str
    name: str
    description: int
    serial: str


    def to_dict(self):
        return {
            "category": self.category,
            "name": self.name,
            "description": self.description,
            "serial": self.serial
        }
