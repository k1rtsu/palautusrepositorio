import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()


        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
    

class PlayerStats:
    def __init__(self, reader):
        self.playerlist = reader.get_players()


    def top_scorers_by_nationality(self, nationality):
        nt = []

        for player in self.playerlist:
            if player.nationality == nationality:
                nt.append(player)

        return sorted(nt, key = lambda player: player.score() , reverse=True)
    
    



        
    

def main():

    url = 'https://studies.cs.helsinki.fi/nhlstats/2023-24/players'

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    result = stats.top_scorers_by_nationality('FIN')

    print("SUOMI")
    for p in result:
        print(p)




if __name__ == "__main__":
    main()
