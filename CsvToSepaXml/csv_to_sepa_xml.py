import csv
import random
import string
import json

from datetime import datetime

from .sepa_xml_templates import *

class CsvToSepaXML:
    def __init__(self):
        self.total_transactions = 0
        self.club_name = ""
        self.total_sum = 0
        with open("config/config.json", encoding="utf-8") as config_file:
            self.config = json.load(config_file)
        self.csvFile = None

    def generate_end_to_end_id(self) -> str:
        return "".join(random.sample(string.ascii_lowercase + string.digits, 35))

    def load_club(self) -> dict:
        with open("config/verein.json", encoding="utf-8") as f:
            club_dict = json.load(f)
        return club_dict

    def generate_debitor_infos(self, reader: csv.DictReader) -> str:
        reader = csv.DictReader(self.csvFile, delimiter=';')
        end_to_end_ids = []
        debitors = ''
        beitragsrechnung = int(self.config['BeitragsrechnungStart'])

        for row in reader:
            end_to_end_id = self.generate_end_to_end_id()
            end_to_end_ids.append(end_to_end_id)
            full_name = f"{row['first_name']} {row['last_name']}"
            debitors += sepa_debitor_xml.format(
                self.total_transactions,
                end_to_end_id, 
                row['amount'],
                row['mandate_id'],
                row['mandate_date'],
                full_name,
                row['IBAN'],
                beitragsrechnung
            )
            self.total_sum += int(row['amount'])
            self.total_transactions += 1
            beitragsrechnung += 1

        if(len(set(end_to_end_ids)) < len(end_to_end_ids)):
            print("Duplicate end to end id detected, aborting...")
            exit(1)
        
        return debitors

    def generate_club_infos(self) -> str:
        club = self.load_club()
        creditor = sepa_creditor_xml.format(
            club['name'],
            club['IBAN'],
            club['BIC'],
            club['CreditorSchemeID']
        )
        self.club_name = club['name']

        return creditor
    
    def generate_xml(self, csv_path: str) -> str:
        file = open(csv_path, encoding='utf-8-sig')
        self.csvFile = file
        with(open(csv_path, encoding="utf-8-sig")):
            debitors = self.generate_debitor_infos()
        creditor = self.generate_club_infos()
        collection_date = self.config['CollectionDate']

        doc = sepa_doc_xml.format(
            datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            self.total_transactions,
            self.total_sum,
            self.club_name,
            self.total_transactions,
            self.total_sum,
            collection_date,
            creditor,
            debitors
        )
        return doc