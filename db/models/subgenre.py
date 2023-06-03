
### User Model ###

from pydantic import BaseModel

class Subgenre(BaseModel):
    name: str
    description: str
    linkPlaylist: str
    colors: object
    bpmRange: object
    artists: list