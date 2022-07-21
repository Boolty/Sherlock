import json
from urllib.request import urlopen


def iptracker():
    ip = input("Enter IP Address: ")
    url = "http://ip-api.com/json/"
    trackedip = urlopen(url + ip)
    data = trackedip.read()
    values = json.loads(data)

    print("City: " + values['city'])
    print("Country: " + values['country'])
    print("Name of the region: " + values['regionName'])
    print("Region: " + values['region'])
    print("ISP: " + values['isp'])
    print("ZIP Code: " + values['zip'])