import pickle

class DbManager:
    def __init__(self):
        pass
    def read_players(self):
        try:
            with open("players_db.dat", "rb") as file:
                players = pickle.load(file)
        except FileNotFoundError:
            players = []        
        return players
    def write_players(self, player):
            try:
                with open("players_db.dat", "rb") as file:
                    players = pickle.load(file)
            except FileNotFoundError:
                players = []
            players.append(player)
            with open('players_db.dat', "wb") as file:
                pickle.dump(players, file)

