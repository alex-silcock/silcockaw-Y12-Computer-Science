import requests
import json

parameters = {
    "lat": 40.71,
    "lon": -74
}

pass_times = response.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
#end function

jprint(response.json())
