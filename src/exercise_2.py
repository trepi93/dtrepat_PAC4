"""Module to execute the second exercise of the PAC
In this module we make two functions to anonymize names
and erase null times"""

import pandas as pd
from faker import Faker


def name_surname(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Anonymize names of the cyclist dataset using Faker

    :param
        dataframe (pd.DataFrame): original dataframe
        whose names we want to anonymize. The names
        must be in the column "biker".

    :return:
        pd.DataFrame: new dataframe with anonymized names
    """

    # Comprovem si la columna "biker" existeix en el dataframe
    if "biker" not in dataframe.columns:
        raise KeyError("Column biker not in dataframe columns")

    # Inicialitzem faker
    fake = Faker()
    fake.seed_instance(1234)

    # Generem un nom per cada registre
    dataframe["biker"] = dataframe["biker"].apply(lambda _: fake.name())

    return dataframe


def solve_exercise2(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Give the answers of the second exercise of the PAC and returns a
    dataframe with anonymized biker names and no null times

    :param
        dataframe (pd.DataFrame): dataframe
        whose names we want to anonymize and erase null times.
        The names must be in the column "biker".

    :return:
        pd.DataFrame: new dataframe with anonymized biker names
        and no null times
    """
    # Creem el dataframe amb els noms anonimitzats
    anon_dataframe = name_surname(dataframe)

    print("-------------- EXERCICI 2 ----------------\n")
    print(f"Els 5 primers valors després d'anonimitzar són:\n{anon_dataframe.head(5)}")

    # Eliminem els temps nuls usant .drop
    dataframe_no_nulls = anon_dataframe.drop(
        anon_dataframe[anon_dataframe["time"] == "00:00:00"].index)

    # Creem les variables que després imprimirem. El tamany del df i un diccionari amb les
    # dades del ciclista del dorsal 1000.
    number_cyclists = len(dataframe_no_nulls)
    cyclist_dorsal_1000 = (dataframe_no_nulls.loc[dataframe_no_nulls['dorsal'] == 1000].iloc[0]
                           .to_dict())

    print(f"Els 5 primers valors després d'eliminar el temps nuls són:"
          f"\n{dataframe_no_nulls.head(5)}")
    print(f"El nombre de ciclistes després d'eliminar els temps nuls és: {number_cyclists}")
    print(f"El ciclista amb el dorsal 1000 és: {cyclist_dorsal_1000['biker']}, del club "
          f"{cyclist_dorsal_1000['club']} i amb un temps de {cyclist_dorsal_1000['time']}")
    print("------------------------------------------\n")

    return dataframe_no_nulls
