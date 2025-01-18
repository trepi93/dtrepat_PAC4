"""Module where execute all the exercises, sequentially or
 one by one"""

import argparse
from src.exercise_1 import solve_exercise1
from src.exercise_2 import solve_exercise2
from src.exercise_3 import solve_exercise3
from src.exercise_4 import solve_exercise4
from src.exercise_5 import solve_exercise5


def main(exercise_number=5):
    """
    Executes the exercises of the PAC 4

    :param
        exercise_number (int): number of exercise you want to execute (and impicitly
                               all the previous ones)
    :return:
        None
    """
    # Amb una estructura condicional, anem controlant  quines funcions s'executen

    bikers_dataframe = None

    if exercise_number >= 1:
        print("Executant Exercici 1...")
        bikers_dataframe = solve_exercise1("./data/dataset.csv", ";")

    if exercise_number >= 2:
        print("Executant Exercici 2...")
        bikers_dataframe = solve_exercise2(bikers_dataframe)

    if exercise_number >= 3:
        print("Executant Exercici 3...")
        bikers_dataframe = solve_exercise3(bikers_dataframe)

    if exercise_number >= 4:
        print("Executant Exercici 4...")
        bikers_dataframe = solve_exercise4(bikers_dataframe)

    if exercise_number == 5:
        print("Executant Exercici 5...")
        bikers_dataframe = solve_exercise5(bikers_dataframe, "UCSC")

    print("Execució completada.")


if __name__ == "__main__":
    # Usant argparse incorporem arguments quan executem el fitxer main.
    parser = argparse.ArgumentParser(description="Executa els exercicis de forma sel·lectiva."
                                                 "Si no indiques cap sel·lecció, els executa tots")
    # Afegim l'argument, que en aquest cas serà opcional. Si no s'indica
    # res s'executaran tots.
    parser.add_argument("--exercise", type=int, default=5, choices=range(1, 6),
                        help="Especifica el número d'exercici a executar (1-5). "
                             "Tots els exercicis anteriors s'executaran també"
                             "P.ex: Si indiques 2, s'executarà l'1 i el 2")

    args = parser.parse_args()
    main(args.exercise)
