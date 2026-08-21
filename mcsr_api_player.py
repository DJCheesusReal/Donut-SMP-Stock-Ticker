import requests
import json
from datetime import datetime, timedelta
url = "https://api.mcsrranked.com/users/"
user = str(input("Who stats: "))
response = requests.get(f"{url}{user}")

print(response)

parsed = json.loads(response.text)
print(parsed)

#we need eloRate, bestTime value, ['data']['statistics']['total']['wins']['ranked'], ['data']['statistics']['total']['loses']['ranked']

elo = parsed['data']['eloRate']
print(elo)

pb_unparsed = parsed['data']['statistics']['total']['bestTime']['ranked']

duration = timedelta(milliseconds=pb_unparsed)
total_seconds = int(duration.total_seconds())
minutes, seconds = divmod(total_seconds, 60)

pb = f"{minutes:02d}:{seconds:02d}"

print(pb)

totalwins = parsed['data']['statistics']['total']['wins']['ranked']
totalloses = parsed['data']['statistics']['total']['loses']['ranked']

wr = int((totalwins / (totalwins + totalloses)) * 100)
print(f"{wr}%")
