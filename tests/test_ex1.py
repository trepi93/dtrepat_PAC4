"""Testing for exercise_1.py"""

import unittest
from unittest.mock import patch
import pandas as pd
from src.exercise_1 import read_csv, solve_exercise1


class TestsReadCsv(unittest.TestCase):
    """Tests per la funció csv_read()"""
    invalid_extension = None

    @classmethod
    def setUpClass(cls):
        """Creates different types of path for testing"""

        cls.valid_path = "./data/dataset.csv"
        cls.invalid_extension = "./data/invalid_extesnion_file.txt"
        cls.non_existing_file = "./data/nonexisting_file.csv"

        # Creem un fitxer temporal amb extensió incorrecta
        with open(cls.invalid_extension, "w", encoding="utf-8") as f:
            f.write("Biker, time, club, dorsal")

    def test_read_valid_csv_and_returns_dataframe(self):
        """Tests if a valid csv is readed and returns a dataframe"""
        df = read_csv(self.valid_path, separator=",")
        self.assertIsInstance(df, pd.DataFrame)  # Comprovem que és df
        self.assertGreater(len(df), 0)  # Comprovem que hi ha dades

    # Referència per assert.Raises (apartat assertRaises)
    # https://docs.python.org/3/library/unittest.html
    def test_file_with_invalid_extension(self):
        """Test if exception raise with a file with a invalid extension"""
        with self.assertRaises(ValueError) as context:
            read_csv(self.invalid_extension, separator=";")
        self.assertEqual(str(context.exception), "The extension isn't valid. Only csv accepted")

    def test_file_not_found(self):
        """Test if exception raise if a file doesn't exist"""
        with self.assertRaises(ValueError) as context:
            read_csv(self.non_existing_file, separator=";")
        self.assertEqual(str(context.exception), "Path doesn't exist")

    def test_data_is_read_correct_and_is_the_right_one(self):
        """Comprova que les dades del dataframe es llegeixin correctament"""
        df = read_csv(self.valid_path, separator=";")

        # Comprovem les dades bàsiques
        self.assertEqual(list(df.columns), ["dorsal", "biker", "club", "time"])
        self.assertEqual(len(df), 3975)
        self.assertEqual(df['biker'].iloc[0], "Christopher Bauer")


class TestsSolveEx1(unittest.TestCase):
    """Tests for the function solve_exercise1"""
    temporal_path = None

    @classmethod
    def setUpClass(cls):
        """Creates fake data for the tests"""
        cls.temporal_path = "./data/csv_with_fake_data_for_testing.csv"

        data = ("dorsals, bikers, clubs, times\n"
                "1, 2, 3, 4\n"
                "Person 1, Person 2, Person 3, Person 4\n"
                "Independiente,Independiente,Independiente,Independiente\n"
                "00:00:00,00:00:00,00:00:00,00:00:00")

        with open(cls.temporal_path, "w", encoding="utf-8") as f:
            f.write(data)

    # Referència pels mock_prints:
    # https://realpython.com/lessons/mocking-print-unit-tests/
    @patch("builtins.print")
    def test_prints(self, mock_print):
        """Tests some print outputs of the function"""
        solve_exercise1(self.temporal_path, ",")

        # Comprova que el mètode print es crida correctament
        mock_print.assert_any_call("El nombre de ciclistes és: 4")
        mock_print.assert_any_call("Les columnes del dataset són: dorsals,  bikers,  clubs,  times")


if __name__ == "__main__":
    unittest.main()
