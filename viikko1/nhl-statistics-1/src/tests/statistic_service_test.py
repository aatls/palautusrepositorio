import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_search_palauttaa_tyhjan_kun_ei_loyda(self):
        self.assertEqual(self.stats.search("Karri"), None)

    def test_team_palauttaa_joukkueen(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    def test_top_palauttaa_eniten_pisteita(self):
        self.assertEqual(self.stats.top(1, SortBy.POINTS)[0].name, "Gretzky")

    def test_top_palauttaa_eniten_maaleja(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0].name, "Lemieux")

    def test_top_palauttaa_eniten_syottoja(self):
        self.assertEqual(self.stats.top(1, SortBy.ASSISTS)[0].name, "Gretzky")