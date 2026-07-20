#----------------------- HOMEWORK ------------------------

import json

with open("python/oyin.json", "r") as f:
    data = json.load(f)

players = data["players"]

players = sorted(players, key=lambda x: x["ball"], reverse=True)

print("TOP 3 O'YINCHI:")

for i in range(3):
    print(f"{i+1}.{players[i]['ism']} - {players[i]['ball']} ball")

eng_past = min(players, key=lambda x: x["ball"])

print("\nENG PAST BALL:")
print(f"{eng_past['ism']} - {eng_past['ball']} ball")
