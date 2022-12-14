import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.20.48:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
} 
basicauth = ("developer", "C1sco12345")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback99",
        "description": "LAB 2.5 Python",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.10.101",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

#resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
#response_json = resp.json()
#print(response_json)
#print(json.dumps(response_json, indent=4))
