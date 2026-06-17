from time import time
import json, csv
from pathlib import Path

import requests

from models import Autoteilbeschreibung

BASE_URL: str = "http://127.0.0.1:8000/"

skeleton = {
    "category": "",
    "name": "",
    "description": "",
    "serial": "",
    "production_date": "",
    "price": 0,
    "currency": "",
    "authorised": False,
    "in_stock": False,
    "compatible_brands": "",
    "recalled": "",
    "digitallyTracked": False,
    "used": False,
    "aftermarket": False,
    "safetyCritical": ""
}

def csv_to_json():
    path = Path("./hersteller_daten")
    for datei in path.glob("*.csv"):
        with open(datei, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            daten_liste = list(csv_reader)
        with open(datei, mode= 'w', encoding='utf-8') as json_file:
            json.dump(daten_liste, json_file)
            print(json_file)

def create_autoteil(beschreibung: Autoteilbeschreibung):
    response = requests.post(BASE_URL + "autoteile/", beschreibung.json())
    return response.status_code


def update_autoteil(beschreibung: Autoteilbeschreibung):
    response = requests.put(BASE_URL + "autoteile/", beschreibung.json())
    return response.status_code

if __name__ == '__main__':
    autoteil = Autoteilbeschreibung(seriennummer=1, zeitstempel=time().__str__())
    print(create_autoteil(autoteil))