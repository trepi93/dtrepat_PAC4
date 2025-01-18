"""Testing for exercise_3.py"""

import sys
import io
import unittest
import pandas as pd

from src.exercise_1 import solve_exercise1
from src.exercise_2 import solve_exercise2
from src.exercise_3 import minutes_002040, solve_exercise3


# Per capturar els prints i que no afegeixin soroll al terminal
suppress_text = io.StringIO()
sys.stdout = suppress_text


class TestsMinutes002040(unittest.TestCase):
    """Tests function minutes_002040()"""

    def test_function_returns_string(self):
        """Test return of function is a string"""
        self.assertIsInstance(minutes_002040("06:19:40"), str)

    def test_time_convertion(self):
        """Tests time convertion is okey"""
        self.assertEqual(minutes_002040("06:19:40"), "06:00")
        self.assertEqual(minutes_002040("06:29:40"), "06:20")
        self.assertEqual(minutes_002040("06:59:40"), "06:40")
        self.assertEqual(minutes_002040("00:00:00"), "00:00")
        self.assertEqual(minutes_002040("23:59:59"), "23:40")

    def test_when_time_is_not_in_range(self):
        """Tests time convertion for timestamp out of range"""
        self.assertEqual(minutes_002040("24:00:30"), "Hour '24' is out of range. "
                                                     "Must be between 00 and 23.")
        self.assertEqual(minutes_002040("00:60:30"), "Minute '60' is out of range. "
                                                     "Must be between 00 and 59.")
        self.assertEqual(minutes_002040("00:30:60"), "Second '60' is out of range. "
                                                     "Must be between 00 and 59.")

    def test_when_time_has_error_format(self):
        """Tests raise error if timestamp is not in a good format"""
        with self.assertRaises(ValueError) as context:
            minutes_002040("00:00")
        self.assertEqual(str(context.exception), "Time format of '00:00' isn't correct. "
                                                 "It must be hh:mm:ss.")

        with self.assertRaises(ValueError) as context:
            minutes_002040("00:00:cc")
        self.assertEqual(str(context.exception), "Time format of '00:00:cc' isn't correct. "
                                                 "It must be hh:mm:ss.")


class TestSolveExercise3(unittest.TestCase):
    """Tests solve_exercise3 function"""

    @classmethod
    def setUpClass(cls):
        """Load data for the tests"""
        df_ex1 = solve_exercise1("./data/dataset.csv", ";")
        df_ex2 = solve_exercise2(df_ex1)
        cls.df_ex3 = solve_exercise3(df_ex2)

        # Creem algunes dades falses per comprovar
        time_values = [
            "00:02:00", "00:05:00", "00:10:00", "00:15:00", "00:18:00",
            "00:20:00", "00:25:00", "00:30:00", "00:35:00", "00:40:00",
            "00:45:00", "00:50:00", "00:55:00", "01:00:00", "01:05:00"
        ]

        cls.fake_data = solve_exercise3(pd.DataFrame({"time": time_values}), hist=False)

    def test_time_grouped_column_is_created(self):
        """Tests if grouped column creates and contains correct values"""
        # Verifiquem que es crea la columna tant en el df com en la fake_data
        self.assertIn("time_grouped", self.df_ex3.columns)
        self.assertEqual(self.df_ex3.shape[1], 5)  # Sumem una columna al df original (de 4 a 5)

        self.assertIn("time_grouped", self.fake_data.columns)
        self.assertEqual(self.fake_data.shape[1], 2) # Sumem una columna al df fake (de 1 a 2)

        # Verifiquem que els valors en "time_grouped" siguin els esperats
        expected_groups = [minutes_002040(x) for x in self.df_ex3["time"]]
        self.assertListEqual(list(self.df_ex3["time_grouped"]), expected_groups)

        # També amb la fake_data
        self.assertListEqual(list(self.fake_data["time_grouped"]), ['00:00', '00:00', '00:00',
                                                                    '00:00', '00:00', '00:20',
                                                                    '00:20', '00:20', '00:20',
                                                                    '00:40', '00:40', '00:40',
                                                                    '00:40', '01:00', '01:00'])

    def test_if_grouping_dataframe_is_correct(self):
        """Tests if the grouping dataframe and its data is correct"""
        # Creem el dataframe agrupat
        dataframe_time_grouped = (self.df_ex3.groupby('time_grouped')
                                  .size().reset_index(name="num_cyclists"))

        fake_data_grouped = (self.fake_data.groupby('time_grouped')
                                 .size().reset_index(name="num_cyclists"))

        # Verifiquem que els dataframes no estiguin buits
        self.assertFalse(dataframe_time_grouped.empty)
        self.assertFalse(fake_data_grouped.empty)

        # Verifiquem que la columna "num_cyclists" existeix
        self.assertIn("num_cyclists", dataframe_time_grouped.columns)
        self.assertIn("num_cyclists", fake_data_grouped.columns)

        # Verifiquem el nombre de grups del df original
        self.assertEqual(len(dataframe_time_grouped), 18)

        # Verifiquem els grups del dataframe fake
        self.assertListEqual(list(fake_data_grouped["time_grouped"]), ['00:00', '00:20',
                                                                       '00:40', '01:00'])
        self.assertListEqual(list(fake_data_grouped["num_cyclists"]), [5, 4, 4, 2])

    def test_function_returns_dataframe(self):
        """Tests function returns a dataframe"""
        self.assertIsInstance(self.df_ex3, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
