"""Module to execute the fourth exercise of the PAC
In this module we make a function to clean and normalize
club names"""

import re
import pandas as pd


def clean_club(club_name: str) -> str:

    """
    Cleans club names to erase some repetitive or
    redundant words or acronyms.

    :param
        club_name (str): club name we want to clean/normalize
    :return:
        str: club name cleaned
    """

    # Indiquem les diferents expressions a eliminar. Hem respectat els espais al final
    # de les cadenes de text, tot i que en algun cas implica que paraules que es troben
    # al final es mantinguin (per exemple SPORT CLUB, ja que ' CLUB' no figura entre
    # la llista de valors)
    full_replacement = ['PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
                        'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ',
                        'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB ']

    start_replacement = ['C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ',
                         'A.C. ', 'A.C ', 'AC ', 'A.D. ', 'A.D ', 'AD ',
                         'A.E. ', 'A.E ', 'AE ', 'E.C. ', 'E.C ', 'EC ',
                         'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD ']

    end_replacement = [' T.T.', ' T.T', ' TT', ' T.E.', ' T.E', ' TE', ' C.C.',
                       ' C.C', ' CC', ' C.D.', ' C.D', ' CD', ' A.D.', ' A.D',
                       ' AD', ' A.C.', ' A.C', ' AC']

    # Noms en majúscules i eliminem espais a inici i final, per tractar millor
    # els diferents casos
    club_name_cleaned = club_name.upper()

    # Per cada tipologia de mots a reemplaçar creem el patró i posteriorment, usant
    # re.sub ho substituïm per netejar el nom. En tots els casos usem re.escape per
    # tractar els caràcters especials com a literals. També usem en alguns casos
    # non-capturing groups per una qüestió d'eficiència, ja que no capturem les
    # coincidències però, tot i així podem treballar amb elles

    # Quan és un reemplaçament complet, simplement unim les diferents expressions a
    # tenir en compte
    full_replacement_pattern = r'|'.join([re.escape(item) for item in full_replacement])
    club_name_cleaned = re.sub(full_replacement_pattern, '', club_name_cleaned).strip()

    # Quan és a inici de paraula, usem el símbol ^ per indicar que ho ha de buscar a
    # l'inici de a paraula, i que ho haurà de substituir.
    start_replacement_pattern = r'^(?:' + '|'.join([re.escape(item)
                                                    for item in start_replacement]) + ')'
    club_name_cleaned = re.sub(start_replacement_pattern, '', club_name_cleaned).strip()

    # Quan és a final de paraula, usem el símbol $ per dir que la coincidència ha de
    # ser al final de paraula
    end_replacement_pattern = r'(?:' + '|'.join([re.escape(item)
                                                 for item in end_replacement]) + ')$'
    club_name_cleaned = re.sub(end_replacement_pattern, '', club_name_cleaned).strip()

    # Retornem el nom traient tots els espais en blanc a principi o final de cadena
    return club_name_cleaned


def solve_exercise4(dataframe: pd.DataFrame) -> pd.DataFrame:

    """
    Give the answers of the fourth exercise of the PAC and returns a
    dataframe with a new column where the name club is normalized.
    Also prints a dataframe with the clubs with most bikers

    :param
        dataframe (pd.DataFrame): dataframe of bikers, whose club
        names we want to normalize.

    :return:
        pd.DataFrame: new dataframe with normalized/cleaned club names
    """

    dataframe['club_clean'] = dataframe['club'].apply(clean_club)

    print("-------------- EXERCICI 4 ----------------\n")
    print(f"Els 15 primers valors després de netejar el nom dels clubs "
          f"són:\n{dataframe.head(15)}")

    bikers_by_club = (dataframe.groupby('club_clean')
                      .size().reset_index(name='num_club_cyclists'))

    bikers_by_club = bikers_by_club.sort_values(by=['num_club_cyclists'],
                                                ascending=False)

    print(f"Els 10 primers clubs amb més ciclistes són:"
          f"\n{bikers_by_club.head(10)}")

    print("------------------------------------------\n")

    return dataframe
