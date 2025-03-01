import requests
import json
import urllib3

#Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_restconf_data(url, headers):
    try:                                                         # Added error handling BRANCH
        response = requests.get(url, headers=headers, timeout=10) # Added timeout main
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RESTCONF data: {e}")
        return None

def main():
    base_url = "https://api.example.com/restconf/data"
    endpoint = "/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1"
    headers = {"Content-Type": "application/yang-data+json", "Authorization": "Basic token"} # Added authorization header BRANCH
    if data := get_restconf_data(base_url + endpoint, headers):
        print(f"RESTCONF Data: {data}") # Added formatted print main
    else:
        print("Failed to fetch RESTCONF data.")

if __name__ == "__main__":
    main()
