from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from models import Autoteilbeschreibung

app = FastAPI()
app.data = [{"category": "2",
             "name": "1",
             "description": "3",
             "serial": "5"}]  # Enthält eine Liste aller Autoteilinformationen


@app.get("/hello_world/", response_description="Hello World!")
def hello_world():
    """Hello World :D

    :return Hello World!
    """

    response = "Hello World!"
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/autoteile/", response_description="Erstellt einen Eintrag eines Autoteils", response_model=Autoteilbeschreibung)
def create(data: Autoteilbeschreibung):
    """Erstellt eine Autoteilbeschreibung im lokalen Speicher des Verwaltungssystems

    :param data:    Autoteilbeschreibung, die abgespeichert werden soll
    :return Autoteilbeschreibung, die gespeichert wurde
    """

    # TODO: Wurde diese Beschreibung vielleicht bereits gescanned?
    # TODO: Fehlen Informationen zur Beschreibung die benötigt werden?
    app.data += [data]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=data.json())


@app.put("/autoteile/", response_description="Aktualisiert eine Autoteilbeschreibung", response_model=Autoteilbeschreibung)
def update(data: Autoteilbeschreibung):
    """Aktualisiert eine Autoteilbeschreibung im lokalen Speicher des Verwaltungssystems

    :param data:    Aktualisierte Autoteilbeschreibung, die im Speicher abgelegt werden soll
    :return Gespeicherte, aktualisierte Autoteilbeschreibung
    """

    # TODO: Suche im lokalen Speicher nach der Autoteilbeschreibung und aktualisiere ihre Daten
    # TODO: Was tun wir, wenn die gegebene Autoteilbeschreibung nicht existiert?
    return JSONResponse(status_code=status.HTTP_200_OK, content=data.json())


@app.get("/autoteile/{seriennummer}", response_description="Erhebt eine Autoteilbeschreibung", response_model=Autoteilbeschreibung)
def get(seriennummer: int):
    """Erhebt eine Autoteilbeschreibung basierend auf der übergebenen Seriennummer

    :param seriennummer:      Seriennummer des zu erhebenden Autoteils
    :return Autoteil mit gegebener Seriennummer
    """

    # TODO: Suche im lokalen Speicher nach der korrekten Autoteilbeschreibung
    # TODO: Was tun wir, wenn die gegebene Autoteilbeschreibung nicht existiert?
    return JSONResponse(status_code=status.HTTP_200_OK, content=None)
