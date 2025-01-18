"""Testing for exercise_2.py"""
import sys
import io
import unittest
from unittest.mock import patch
import pandas as pd
from faker import Faker
from src.exercise_1 import solve_exercise1
from src.exercise_2 import name_surname, solve_exercise2

# Per capturar els prints i que no afegeixin soroll al terminal
suppress_text = io.StringIO()
sys.stdout = suppress_text


class TestsNameSurname(unittest.TestCase):
    """Tests function name_surname()"""

    def setUp(self):
        """Creates fake data for the tests"""

        self.df = pd.DataFrame({
            "biker": ["David Martínez", "Maria Pérez", "Austin Powers"],
            "dorsal": [1, 2, 3],
            "club": ["Independiente", "Independiente", "Independiente"],
            "time": ["00:00:00", "00:00:00", "00:00:00"]
        })


    def test_function_name_surname_changes_names(self):
        """Test function name_surname changes names"""

        # Fem un df anònim aplicant la funció
        df_anonymized = name_surname(self.df)

        # Comprovem que els noms han canviat
        self.assertNotEqual(df_anonymized['biker'][0], "David Martínez")
        self.assertNotEqual(df_anonymized['biker'][1], "Maria Pérez")
        self.assertNotEqual(df_anonymized['biker'][2], "Austin Powers")

    def test_seed_consistency(self):
        """Tests setting a seed works as expected"""
        # Iniciem el faker i li passem una seed
        fake = Faker()
        fake.seed_instance(1234)

        # Creem dos df que compararem
        df1 = name_surname(self.df.copy())
        df2 = name_surname(self.df.copy())

        self.assertTrue((df1['biker'] == df2['biker']).all())

    def test_other_columns_not_change(self):
        """Tests function does not modify other columns"""
        df_anonymized = name_surname(self.df)
        non_biker_columns = self.df.columns != 'biker'

        self.assertTrue((self.df.loc[:, non_biker_columns] ==
                        df_anonymized.loc[:, non_biker_columns]).all().all())

    def test_empty_df(self):
        """Tests normal behavior with an empty df """
        empty_df = pd.DataFrame(columns=['biker', 'dorsal', 'club', 'time'])
        df_anonymized = name_surname(empty_df)
        self.assertTrue(df_anonymized.empty)

    def test_if_no_biker_column_in_the_input_df(self):
        """Tests error raises if biker column does not exists"""
        df_no_biker = pd.DataFrame({
            "dorsal": [1, 2, 3],
            "club": ["Independiente", "Independiente", "Independiente"],
            "time": ["00:00:00", "00:00:00", "00:00:00"]
        })

        with self.assertRaises(KeyError) as context:
            name_surname(df_no_biker)
        self.assertEqual(str(context.exception).strip(), "'Column biker not in dataframe columns'")

    def test_function_returns_dataframe(self):
        """Tests function returns a dataframe"""
        df = name_surname(self.df)
        self.assertIsInstance(df, pd.DataFrame)


class TestsSolveEx2(unittest.TestCase):
    """ Tests function solve_exercise2"""
    @classmethod
    def setUpClass(cls):
        """Loads data for the tests"""
        df = solve_exercise1("./data/dataset.csv", ";")
        cls.df_ex2 = solve_exercise2(df)

    def test_function_returns_dataframe(self):
        """Tests the return is dataframe"""
        self.assertIsInstance(self.df_ex2, pd.DataFrame)  # Comprova que retorna pd.DataFrame

    def test_funtion_erase_null_times(self):
        """Tests all null times are eliminated"""
        self.assertNotIn('00:00:00', self.df_ex2)  # Comprova que no hi ha temps nuls

    def test_check_data_calculated_in_the_function(self):
        """Tests data is showed correctly and is real"""

        number_cyclists = len(self.df_ex2)  # Comprovem la mida del dataset
        cyclist_dorsal_1000 = (self.df_ex2.loc[self.df_ex2['dorsal'] == 1000].iloc[0]
                               .to_dict())
        self.assertEqual(number_cyclists, 3887)

        # A l'anonimitzar el fitxer, només podem comprovar club i temps, no el nom
        self.assertEqual(cyclist_dorsal_1000['club'], "C.D.El cubio ")  # Comprovem el club
        self.assertEqual(cyclist_dorsal_1000['time'], "03:56:33")  # Comprovem el temps

    @patch("builtins.print")
    def test_prints_of_the_function(self, mock_print):
        """Tests some print outputs of the function"""
        solve_exercise2(self.df_ex2)

        # Comprova que el mètode print es crida correctament
        mock_print.assert_any_call("El nombre de ciclistes després d'eliminar "
                                   "els temps nuls és: 3887")


if __name__ == "__main__":
    unittest.main()
