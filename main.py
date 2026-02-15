import json
import csv

json_datei = "namen.json"
csv_datei = "namen.csv"

with open(csv_datei, "r", encoding="utf-8") as csv_readed:
    csv_reader = csv.DictReader(csv_readed)
    csv_list = list(csv_reader)

with open(json_datei, "w", encoding="utf-8") as json_written:
    json_dump = json.dump(csv_list, json_written, indent=4, ensure_ascii=False)

with open(json_datei, "r", encoding="utf-8") as json_readed:
    json_loader = json.load(json_readed)

for n in json_loader:
    name = n.get("name")
    nachname = n.get("nachname")

    print(" " + name)
    print(nachname + "\n")
