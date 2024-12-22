
from typing import Dict
from referee import Referee
from server.illegal_match_access_error import IllegalMatchAccessException

MatchesSchema = Dict[ str, Referee ]
class MatchMaking:
    def __init__(self):
        self.matches: MatchesSchema = {}

    def create_game(self, sesh_id: str):
        self.matches[ sesh_id ] = Referee()
        return self.matches[ sesh_id ]

    def get_game(self, sesh_id: str):
        if not self.matches[ sesh_id ]:
            raise IllegalMatchAccessException('Trying to access a non-existent match') 
        return self.matches[ sesh_id ]

