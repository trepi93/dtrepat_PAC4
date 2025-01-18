"""Tests for main.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from src.main import main


class TestMainFunction(unittest.TestCase):
    """Tests main function that prints exercises"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_of_main_when_a_exercise_is_selected(self, mock_stdout):
        """Tests main function when we pass an argument"""

        # Simula una crida amb un número d'exercici
        with patch('sys.argv', ['main.py', '--exercise', '3']):
            main(3)

        # Obtenim la sortida capturada
        output = mock_stdout.getvalue()

        # Comprovem que s'imprimeixen els exercicis fins al 3 i no el 4 i 5
        self.assertIn("Executant Exercici 1...", output)
        self.assertIn("Executant Exercici 2...", output)
        self.assertIn("Executant Exercici 3...", output)
        self.assertNotIn("Executant Exercici 4...", output)
        self.assertNotIn("Executant Exercici 5...", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_of_main_when_no_exercise_is_selected(self, mock_stdout):
        """Tests main function when no exercise is passed"""

        # Simulem que no es passa cap argument
        with patch('sys.argv', ['main.py']):
            main()

        # Obtenim la sortida capturada
        output = mock_stdout.getvalue()

        # Comprovem que s'imprimeixen tots els exercicis
        self.assertIn("Executant Exercici 1...", output)
        self.assertIn("Executant Exercici 2...", output)
        self.assertIn("Executant Exercici 3...", output)
        self.assertIn("Executant Exercici 4...", output)
        self.assertIn("Executant Exercici 5...", output)

# Referència per capturar la sortida de les funcions i veure si s'han executat
# https://www.geeksforgeeks.org/python-testing-output-to-stdout/


if __name__ == '__main__':
    unittest.main()
