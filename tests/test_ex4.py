"""Testing for exercise_4.py"""

import sys
import io
import unittest
import pandas as pd

from src.exercise_1 import solve_exercise1
from src.exercise_2 import solve_exercise2
from src.exercise_3 import solve_exercise3
from src.exercise_4 import clean_club, solve_exercise4

# Per capturar els prints i que no afegeixin soroll al terminal
suppress_text = io.StringIO()
sys.stdout = suppress_text


class TestsCleanClub(unittest.TestCase):
    """Tests function clean_club"""

    def test_function_returns_string(self):
        """Tests if the function returns a string"""
        self.assertIsInstance(clean_club("Club ciclista Alcañiz"), str)

    def test_full_replacement_string(self):
        """Tests full replacement cleaning name club"""
        self.assertEqual(clean_club("Club ciclista Alcañiz"), "ALCAÑIZ")
        self.assertEqual(clean_club("Alcañiz Agrupacion ciclista Tour"), "ALCAÑIZ TOUR")
        self.assertEqual(clean_club("Alcañiz Agrupacion Tour ciclista"),
                         "ALCAÑIZ AGRUPACION TOUR CICLISTA")

    def test_start_replacement_string(self):
        """Tests starts replacement cleaning name club"""
        self.assertEqual(clean_club("E.C. GIRONELLA "), "GIRONELLA")
        self.assertEqual(clean_club("A.C.Montjuïc"), "A.C.MONTJUÏC")
        self.assertEqual(clean_club("A.c. E.C. Montjuïc"), "E.C. MONTJUÏC")
        self.assertEqual(clean_club("T.T. Montjuïc"), "T.T. MONTJUÏC")

    def test_end_replacement_string(self):
        """Tests end replacement cleaning name club"""
        self.assertEqual(clean_club("CEADEA MTB.T.E"), "CEADEA MTB.T.E")
        self.assertEqual(clean_club("CEADEA MTB   T.E"), "CEADEA MTB")
        self.assertEqual(clean_club("CEADEA MTB "), "CEADEA MTB")
        self.assertEqual(clean_club("CEADEA MTB A.E"), "CEADEA MTB A.E")

    def test_uppercase_and_spaces_and_mixed_cases_string(self):
        """Tests uppercase and strips and some mixed and unusual cases"""
        self.assertEqual(clean_club("  C.C. BaRceLONA  "), "BARCELONA")
        self.assertEqual(clean_club("C.C.   BARCELONA  C.C."), "BARCELONA")
        self.assertEqual(clean_club("PENYA CICLISTA BARCELONA  C.C."), "BARCELONA")

    def test_blank_input(self):
        """Tests if a blank input is given"""
        self.assertEqual(clean_club(""), "")


class TestSolveExercise4(unittest.TestCase):
    """Tests solve_exercise4 function"""

    @classmethod
    def setUpClass(cls):
        """Load data for the tests"""
        df_ex1 = solve_exercise1("./data/dataset.csv", ";")
        df_ex2 = solve_exercise2(df_ex1)
        df_ex3 = solve_exercise3(df_ex2)
        cls.df_ex4 = solve_exercise4(df_ex3)

        # Creem algunes dades falses per comprovar
        data = {
                "biker": ["Marc Soldevila", "Jordi Ferrer", "Anna Vidal", "Laura Pons",
                          "Xavi Rovira", "Pau Martínez", "Clara Esteve", "Albert Roca",
                          "Marta Sànchez", "Gerard Tomàs"],
                "club": ["CC Montserrat", "Penya Ciclista del Pirineu", "CD Team Rodadors",
                         "CC Montserrat", "CC Montserrat", "CC Montserrat",
                         "Penya Ciclista del Pirineu", "Penya Ciclista del Pirineu",
                         "CC Montserrat", "CD Team Rodadors"]
        }

        cls.fake_data = solve_exercise4(pd.DataFrame(data))

    def test_returns_dataframe(self):
        """Tests it returns a dataframe"""
        self.assertIsInstance(solve_exercise4(self.df_ex4), pd.DataFrame)
        self.assertIsInstance(solve_exercise4(self.fake_data), pd.DataFrame)

    def test_clean_name_column_is_created_and_correct(self):
        """Tests if club name column creates and contains correct values"""
        # Comprovem que es crea la columna
        self.assertIn("club_clean", self.df_ex4.columns)
        self.assertEqual(self.df_ex4.shape[1], 6)  # Sumem una columna al df original (de 4 a 5)

        self.assertIn("club_clean", self.fake_data.columns)
        self.assertEqual(self.fake_data.shape[1], 3)  # Sumem una columna al df original (de 2 a 3)

        # Comprovem que les dades que conté són correctes
        expected_names = [clean_club(x) for x in self.df_ex4["club"]]
        self.assertListEqual(list(self.df_ex4["club_clean"]), expected_names)

        expected_fake_names = [clean_club(x) for x in self.fake_data["club"]]
        self.assertListEqual(list(self.fake_data["club_clean"]), expected_fake_names)
        self.assertListEqual(list(self.fake_data["club_clean"].head(4)),
                             ["MONTSERRAT", "DEL PIRINEU", "TEAM RODADORS", "MONTSERRAT"])

    def test_grouping_dataframe(self):
        """Tests if the grouping dataframe and its data is correct"""
        # Creem el dataframe agrupat
        dataframe_club_grouped = (self.df_ex4.groupby('club_clean')
                                  .size().reset_index(name='num_club_cyclists'))

        fake_data_club_grouped = (self.fake_data.groupby('club_clean')
                                  .size().reset_index(name='num_club_cyclists'))

        # I el dataframe ordenat
        dataframe_club_sorted = dataframe_club_grouped.sort_values(by=['num_club_cyclists'],
                                                                   ascending=False)

        fake_data_club_sorted = fake_data_club_grouped.sort_values(by=['num_club_cyclists'],
                                                                   ascending=False)

        # Verifiquem que els dataframes no estiguin buits
        self.assertFalse(dataframe_club_grouped.empty)
        self.assertFalse(fake_data_club_grouped.empty)

        # Verifiquem que la columna "num_cyclists" existeix
        self.assertIn("num_club_cyclists", dataframe_club_grouped.columns)
        self.assertIn("num_club_cyclists", fake_data_club_grouped.columns)

        # Verifiquem que els primers de la llista del dataframe ordenat coincideixin
        # també a nivell numèric
        self.assertListEqual(list(dataframe_club_sorted['club_clean'].head(4)),
                             ["INDEPENDIENTE", "UCSC", "SARIÑENA", "OSCENSE"])
        self.assertListEqual(list(dataframe_club_sorted["num_club_cyclists"].head(4)),
                             [2484, 19, 18, 16])

        # Verifiquem que els primers de la llista del dataframe coincideixin
        self.assertListEqual(list(fake_data_club_sorted['club_clean']),
                             ['MONTSERRAT', 'DEL PIRINEU', 'TEAM RODADORS'])
        self.assertListEqual(list(fake_data_club_sorted["num_club_cyclists"]), [5, 3, 2])


if __name__ == "__main__":
    unittest.main()
