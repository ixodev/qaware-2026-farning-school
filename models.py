from typing import Optional

from pydantic import BaseModel


class Autoteilbeschreibung(BaseModel):
    # TODO: Füge relevante Daten hinzu
    seriennummer: int
    zeitstempel: Optional[str]

    def to_dict(self):
        return {
            # TODO: Füge relevante Daten hinzu
            "seriennummer": self.seriennummer,
            "zeitstempel": self.zeitstempel
        }
