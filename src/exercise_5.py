"""Module to execute the fifth exercise of the PAC
In this module we make a function to get some stats about
the bikers of a club"""

from typing import Union
import pandas as pd


def stats_by_club(dataframe: pd.DataFrame, club_name: str) -> Union[pd.DataFrame, None]:

    """
    Give some stats (bikers, top biker and best % in the competition) about the bikers
    of a specific club.

    :param
        dataframe (pd.DataFrame): dataframe with the bikers and results data
        club_name (str): name of the club for which we want to get the stats
    :return:
        None: if the club doesn't exist the function won't return anything
        pd.DataFrame: dataframe with the results of the bikers for the given club
    """

    # Convertim la columna time a datetime per poder ordenar per temps
    dataframe['time'] = pd.to_datetime(dataframe['time'], format='%H:%M:%S')

    # Ordenem el dataframe inicial per obtenir les posicions. Resetegem índexos perquè
    # això és el que ens marcarà la posició
    sorted_dataframe = dataframe.sort_values(by=['time']).reset_index(drop=True)

    # Tornem a convertir en string perquè quedi més net (sinó també ens apareix la data)
    sorted_dataframe['time'] = sorted_dataframe['time'].dt.strftime('%H:%M:%S')

    # Fitrem el dataframe pel club que volem buscar
    filtered_dataframe = sorted_dataframe[sorted_dataframe['club_clean'] == club_name]

    # Clàusula de guarda per no retornar res si el club no existeix o no
    # té ciclistes participants
    if filtered_dataframe.empty:
        print(f"O bé el club '{club_name}' és incorrecte o cap ciclista va participar "
              f"a la carrera en representació seva")
        return None

    club_bikers_list = filtered_dataframe['biker'].tolist()

    # Guardem el millor ciclista. Ho fem quedant-nos només amb el nom del ciclista
    best_cyclist = filtered_dataframe.iloc[0]['biker']

    # Busquem el nostre millor ciclista en el dataframe ordenat i la seva posició
    # Sumem 1 perquè Python comença en 0.
    position_best_cyclist = sorted_dataframe[sorted_dataframe['biker'] == best_cyclist].index[0] + 1

    # Calculem el percentatge respecte el total
    pct_above_total = (position_best_cyclist / len(dataframe)) * 100

    # Mostrem per pantalla els resultats
    print(f"ELs ciclistes del {club_name} són {len(filtered_dataframe)} i els "
          f"seus noms són {', '.join(club_bikers_list)}")
    print(f"El ciclista del {club_name} amb el millor temps és: "
          f"{best_cyclist}")
    print(f"El ciclista del {club_name} amb el millor temps va "
          f"quedar en la posicíó {position_best_cyclist}, que "
          f"representa el top {pct_above_total:.2f}% de la competició")

    return filtered_dataframe


def solve_exercise5(dataframe: pd.DataFrame, club_name: str) -> Union[pd.DataFrame, None]:
    """
    Give the answers of the fifth exercise of the PAC and returns a
    dataframe filtered with the data filtered by the given club

    :param
        dataframe (pd.DataFrame): dataframe with the bikers and results data
        club_name (str): name of the club for which we want to get the stats
    :return:
        None: if the club doesn't exist the function won't return anything
        pd.DataFrame: dataframe with the results of the bikers for the given club
    """
    print("-------------- EXERCICI 5 ----------------\n")
    return stats_by_club(dataframe, club_name)
