import json
class GameStatus:

    def __init__(self, name, shorts, win, lose):
        self.name = name
        self.shorts = shorts
        self.win = win
        self.lose = lose

    def __iter__(self):
        yield from{
            "name": self.name,
            "shorts": self.shorts,
            "win": self.win,
            "lose": self.lose
        }.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii = False)

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return GameStatus(json_dct["name"],
                        json_dct["shorts"],
                        json_dct["win"],
                        json_dct["lose"])
  