"""Testing for exercise_5.py"""

import sys
import io
import unittest
from unittest.mock import patch
import pandas as pd
from src.exercise_1 import solve_exercise1
from src.exercise_2 import solve_exercise2
from src.exercise_3 import solve_exercise3
from src.exercise_4 import solve_exercise4
from src.exercise_5 import stats_by_club, solve_exercise5


# Per capturar els prints i que no afegeixin soroll al terminal
suppress_text = io.StringIO()
sys.stdout = suppress_text


class TestsStatsByClub(unittest.TestCase):
    """Tests function StatsByClub"""

    def setUp(self):
        """Creates fake data for the tests"""

        self.df = pd.DataFrame({
            'biker': ['John', 'Marie', 'Claire', 'James', 'Rachel', 'Chandler'],
            'club_clean': ['Club 1', 'Club 2', 'Club 1', 'Club 1', 'Club 2', 'Club 1'],
            'time': ["03:00:04", "05:02:25", "03:01:05", "04:02:04", "02:02:25", "03:11:05"]
        })
        self.df['time'] = pd.to_datetime(self.df['time'], format='%H:%M:%S')
        self.df = self.df.sort_values(by=['time']).reset_index(drop=True)
        self.df['time'] = self.df['time'].dt.strftime('%H:%M:%S')

    def test_function_returns_dataframe_when_club_exists(self):
        """Tests function returns a dataframe if club exists"""
        self.assertIsInstance(stats_by_club(self.df, "Club 1"), pd.DataFrame)

    def test_function_returns_none_when_club_not_exists(self):
        """Tests function returns a dataframe if club doesn't exists"""
        self.assertIsNone(stats_by_club(self.df, "Club 3"), pd.DataFrame)

    def test_function_returns_correct_data(self):
        """Tests function loads dataframe okey and returns correct data"""
        result = stats_by_club(self.df, "Club 1")
        self.assertEqual(len(result), 4)

        # Comprovem els ciclistes (que ja estaran ordenats per temps)
        self.assertListEqual(list(result['biker']), ['John', 'Claire', 'Chandler', 'James'])

        # Comprovem el millor ciclista i el percentatge
        self.assertEqual(result.iloc[0]['biker'], "John")
        self.assertEqual(self.df[self.df['biker'] == "John"].index[0] + 1, 2)
        self.assertEqual(round((self.df[self.df['biker'] == "John"].index[0] + 1)
                               / len(self.df), 2), 0.33)

    @patch("builtins.print")
    def test_prints_real_club(self, mock_print):
        """Tests if prints for an existing team are correct"""
        stats_by_club(self.df, "Club 1")

        # Comprova que el mètode print es crida correctament
        mock_print.assert_any_call("ELs ciclistes del Club 1 són 4 i els seus noms són "
                                   "John, Claire, Chandler, James")
        mock_print.assert_any_call("El ciclista del Club 1 amb el millor temps és: John")
        mock_print.assert_any_call("El ciclista del Club 1 amb el millor temps va quedar en "
                                   "la posicíó 2, que representa el top 33.33% de la competició")

    @patch("builtins.print")
    def test_prints_non_real_club(self, mock_print):
        """Tests if prints for a non existing team are correct"""
        stats_by_club(self.df, "Club A")

        # Comprova que el mètode print es crida correctament
        mock_print.assert_any_call("O bé el club 'Club A' és incorrecte o cap ciclista "
                                   "va participar a la carrera en representació seva")


class TestSolveExercise5(unittest.TestCase):
    """Tests solve_exercise5 function"""

    @classmethod
    def setUpClass(cls):
        """Load data for the tests"""
        df_ex1 = solve_exercise1("./data/dataset.csv", ";")
        df_ex2 = solve_exercise2(df_ex1)
        df_ex3 = solve_exercise3(df_ex2)
        df_ex4 = solve_exercise4(df_ex3)
        cls.df_ex4 = df_ex4
        cls.df_ex5 = solve_exercise5(df_ex4, "ARIZ")

        cls.df_ex5_fake = solve_exercise5(df_ex4, "Fake Club")

    def test_function_returns_dataframe_when_club_exists(self):
        """Tests function returns a dataframe if club exists"""
        self.assertIsInstance(self.df_ex5, pd.DataFrame)

    def test_function_returns_none_when_club_not_exists(self):
        """Tests function returns a dataframe if club doesn't exists"""
        self.assertIsNone(self.df_ex5_fake)

    # No testegem la resta de la funció perquè ja ho hem fet en el test anterior.
    # Testejant el print, ja entenem que la resta és correcte.
    @patch("builtins.print")
    def test_prints(self, mock_print):
        """Tests if prints are correct"""
        solve_exercise5(self.df_ex4, "ARIZ")
        # A l'anonimitzar el fitxer, només podrem comprovar posició. No el nom
        mock_print.assert_any_call("El ciclista del ARIZ amb el millor temps va quedar "
                                   "en la posicíó 1096, que representa el top 28.20% "
                                   "de la competició")


if __name__ == "__main__":
    unittest.main()
