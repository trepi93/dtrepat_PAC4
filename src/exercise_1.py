"""Module to execute the first exercise of the PAC.
In this module we make a function to read csv"""

import os
import pandas as pd


def read_csv(path: str, separator: str) -> pd.DataFrame:

    """
    Read a csv file using pandas library
    :param
        path (str): path where the csv is
                    located
        separator (str): separator of the csv
    :return:
        pd.DataFrame: pandas Dataframe with
        the csv data
    """

    if not os.path.exists(path):
        raise ValueError("Path doesn't exist")

    # Extraiem l'extensió del fitxer
    file_extension = os.path.splitext(path)[1]

    # Si és un fitxer csv, creem el pd.DataFrame
    # i imprimim el nombre de ciclistes, els primers
    # valors i les columnes.
    if file_extension == ".csv":
        dataset = pd.read_csv(path, sep=separator)

    # Si no és un csv, s'aixeca una excepció
    else:
        raise ValueError("The extension isn't valid. Only csv accepted")

    return dataset


def solve_exercise1(path: str, separator: str) -> pd.DataFrame:
    """
    Give the answers of the first exercise of the PAC and returns the
    dataframe from reading the csv
    :param
        path (str): path where the csv is
                    located
        separator (str): separator of the csv
    :return:
        pd.DataFrame: pandas Dataframe with
        the csv data if csv file
    """
    # Llegim el csv i creem el dataframe
    dataframe = read_csv(path, separator)

    # Creem les variables per printar-les
    number_cyclists = len(dataframe)
    columns_dataframe = list(dataframe.columns)

    print("-------------- EXERCICI 1 ----------------\n")
    print(f"Els 5 primers valors són:\n{dataframe.head(5)}")
    print(f"El nombre de ciclistes és: {number_cyclists}")
    print(f"Les columnes del dataset són: {', '.join(columns_dataframe)}")
    print("------------------------------------------\n")

    return dataframe
