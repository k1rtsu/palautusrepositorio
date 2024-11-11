import requests
from player import Player
from rich import print
from rich.prompt import Prompt
from rich.table import Table



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
    while True:
        season = Prompt.ask("Select season [purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/purple]")
        nationality = Prompt.ask("Select nationality [purple][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/purple]")


        url = 'https://studies.cs.helsinki.fi/nhlstats/2023-24/players'
        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        result = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} in {season}")
        table.add_column("name", style="deep_sky_blue1")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green3")
        table.add_column("assists", style="green3")
        table.add_column("points", style="green3")

        for player in result:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        print(table)






if __name__ == "__main__":
    main()
