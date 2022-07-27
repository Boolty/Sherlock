import requests


def iptracker():
    ip = input("Enter IP Address: ")
    #ip = 8.8.8.8
    trackedip = requests.get(f"http://ip-api.com/json/{ip}")
    values = trackedip.json()
    #print(values)

    print("Status: " + values['status'])
    print("ISP: " + values['isp'])
    print("DNS: " + values['org'])
    print("Country: " + values['country'])
    print("CountryCode: " + values['countryCode'])
    print("Region: " + values['region'])
    print("Name of the region: " + values['regionName'])
    print("City: " + values['city'])
    print("Zip: " + values['zip'])
    print("Latitude: " + str(values['lat']))
    print("Longitude: " + str(values['lon']))
    print("Timezone: " + values['timezone'])
    print("AS: " + values['as'])
    print("Query: " + values['query'])

    input()
