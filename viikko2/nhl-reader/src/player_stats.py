class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        is_nationality = lambda player : player.nationality == nationality
        players_by_nationality = list(filter(is_nationality, self.players))

        score = lambda player : player.goals + player.assists
        players_by_nationality.sort(reverse=True, key=score)

        return players_by_nationality