import requests
import json
from datetime import datetime, timedelta
url = "https://api.mcsrranked.com/users/"
user = str(input("username of players stats you want: "))
response = requests.get(f"{url}{user}")
print(response)
parsed = json.loads(response.text)


elo = parsed['data']['eloRate'] #easy parse
print(f"current elo: {elo}")

pb_unparsed = parsed['data']['statistics']['total']['bestTime']['ranked'] #holy pb is long parse

duration = timedelta(milliseconds=pb_unparsed)
total_seconds = int(duration.total_seconds())
minutes, seconds = divmod(total_seconds, 60)

pb = f"{minutes:02d}:{seconds:02d}"

print(f"pb: {pb}")

totalwins = parsed['data']['statistics']['total']['wins']['ranked']
totalloses = parsed['data']['statistics']['total']['loses']['ranked']

wr = int((totalwins / (totalwins + totalloses)) * 100)
print(f"win rate: {wr}%")

