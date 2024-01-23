
from dataclasses import dataclass
# import requests

@dataclass(frozen=True)
class Vertex():
    id_type: str
    value: str

# Interface for the Remote IDS server
class IDS():

    def __init__(self, url: str):
        self.url = url

    def get_vertex(vertex: str) -> Vertex:
        # now go to the server and return the vertex
        return Vertex("email", "dror@lightricks.com")
