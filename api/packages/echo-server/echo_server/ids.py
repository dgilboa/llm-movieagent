
from dataclasses import dataclass
import requests
import json

@dataclass(frozen=True)
class Vertex():
    id_type: str
    value: str

# Interface for the Remote IDS server
class IDS():

    def __init__(self, url: str):
        self.url = url + "/api/graphql"

    def get_vertex(self, vertex: str) -> Vertex:
        payload = json.dumps({
            "query": "query{\n getEmail(email: \"" + f"{vertex}" + "\"){\n id createdBy createdAt \n}\n}"
        })

        headers = {
            'Content-Type': 'application/json'
        }
        print("self :" + self.url)
        from socket import gethostbyname
        ip = gethostbyname('docker.for.mac.localhost')

        urll = "http://"+ip+":8088/api/graphql"

        response = requests.post(url=urll, data=payload, headers=headers)
        print(response.text)
        res = json.loads(response.text)

        if not res.get("data").get("getEmail"):
            return Vertex("email", "not exist")
        else:
            return Vertex("email", res.get("data").get("getEmail").get("id"))
