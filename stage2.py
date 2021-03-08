import requests
import json

base_url = "https://sandboxdnac.cisco.com/dna"
auth_endpoint = "/system/api/v1/auth/token"

user = 'devnetuser'
password='Cisco123!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user, password)).json()
token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

dev_endpoint = "/intent/api/v1/network-device"

local_inventory = []

try:
    dev_response = requests.get(url=f"{base_url}{dev_endpoint}", auth=(user, password), headers=headers)
    if dev_response.status_code == 200:
        devices = dev_response.json()['response']
        for dev in devices:
            local_inventory.append({
                'name' : dev['hostname'],
                'type' : dev['type'],
                'mac address' : dev['macAddress'],
                'serial' : dev['serialNumber']
                })
        for local_device in local_inventory:
            print(json.dumps(local_device))
except Exception as ex3:
    print(ex3)