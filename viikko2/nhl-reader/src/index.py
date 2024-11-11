# import requests
# from player import Player

# def main():
#     url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
#     response = requests.get(url).json()

#     print("JSON-muotoinen vastaus:")
#     print(response)

#     players = []

#     for player_dict in response:
#         player = Player(player_dict)
#         players.append(player)

#     print("Oliot:")

#     for player in players:
#         print(player)

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


main()