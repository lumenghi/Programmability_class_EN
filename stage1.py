
import requests
import json

merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = 'https://api.meraki.com/api/v0'
endpoint = '/organizations'

headers = {
    'X-Cisco-meraki-API-Key': merakikey
}

#stage1
endpoint_network = endpoint + '/' + str(orgId) + '/networks'
endpoint_devices = endpoint + '/' + str(orgId) + '/devices'
try:
    response = requests.get(url=f"{base_url}{endpoint_network}", headers=headers)
    if response.status_code == 200:
        networks = response.json()
        for network in networks:
            if network['name']== 'DevNet Sandbox ALWAYS ON':
                networkId = network['id']
except Exception as ex1:
    print(ex1)

local_inventory = []

try:
    response = requests.get(url=f"{base_url}{endpoint_devices}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            if device['networkId']== networkId:
                # populate local inventory
                local_inventory.append({
                    'name' : device['name'],
                    'type' : device['model'],
                    'mac address' : device['mac'],
                    'serial' : device['serial'],
                    'category' : device['Meraki'],
                    })
        # conver local inventory to JSON and print
        for local_device in local_inventory:
            print(json.dumps(local_device))

except Exception as ex2:
    print(ex2)