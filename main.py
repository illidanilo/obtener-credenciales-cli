import json
import requests


data = {"password":"admin123!", "username":"admin"}
cabecera = {"content-type": "application/json"}
respuesta = requests.post("http://127.0.0.1:58000/api/v1/ticket", json.dumps(data), headers=cabecera)
token = (respuesta.json()["response"]["serviceTicket"])


header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get("http://127.0.0.1:58000/api/v1/global-credential/cli", headers=header)

for i in range(0, 3):

    print(r.json()["response"][i]["id"])
    print(r.json()["response"][i]["username"])
    print(r.json()["response"][i]["password"])
