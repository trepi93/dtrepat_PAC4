"""Module to execute the third exercise of the PAC
In this module we make functions to convert time
into a grouped format and to make a histogram with
the grouped times of the cyclists"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def minutes_002040(time: str) -> str:
    """
    Converts time into bins of 20 minutes. So, if a time is between XX:00 and XX:19
    the function will return XX:00. If it's between XX:20 and XX:39, the function
    will return XX:20, and so on.

    :param
    time (str): time string (hh:mm:ss) to be converted

    :return:
    str: string with the time converted into hh:mm with the bins explained above
    """

    # Fem una estructura try-except per controlar el cas en què el format sigui
    # incorrecte
    try:
        # Creem variables per les hores i els minuts (passades a int).
        hh, mi, ss = map(int, time.split(":"))

        # Controlem els valors de les hores i els minuts perquè estigui
        # dins del rang de temps.
        if not 0 <= hh < 24:
            return f"Hour '{hh}' is out of range. Must be between 00 and 23."
        if not 0 <= mi < 60:
            return f"Minute '{mi}' is out of range. Must be between 00 and 59."
        if not 0 <= ss < 60:
            return f"Second '{ss}' is out of range. Must be between 00 and 59."

        # Amb una estructura condicional assignem uns valors als minuts
        # segons les regles de l'enunciat
        if mi < 20:
            mi_grouped = 0
        elif mi < 40:
            mi_grouped = 20
        else:
            mi_grouped = 40

        # Retornem la string sencera, amb els canvis fets
        return f"{hh:02}:{mi_grouped:02}"

    except ValueError as e:
        raise ValueError(f"Time format of '{time}' isn't correct. It must be hh:mm:ss.") from e


def make_histogram(intervals: pd.Series, frequencies: pd.Series,
                   graph_params: dict = None, show=False):
    """
    It makes a histogram and saves it.

    :param
        intervals (pd.Series): data intervals for the histogram (X-axis)
        frequencies (pd.Series): frequencies for each interval (Y-axis)
        graph_params (dict): dictionary containing title, xlabel, ylabel, and saving_path.
                             Optional parameter, by default None
        show (bool): boolean to say if you want to show the histogram or not. Optional
                     parameteter, by default False, so it will not be shown, only saved.
    :return
        None
    """
    # Clàusula per si no es passen paràmetres del gràfic
    if graph_params is None:
        graph_params = {
            "title": "Histogram",
            "xlabel": "Intervals",
            "ylabel": "Frequencies",
            "saving_path": "histogram.png"
        }
    # Variables d'estil del gràfic, segons el diccionari que es passi
    title = graph_params.get("title", "Histogram")
    xlabel = graph_params.get("xlabel", "Intervals")
    ylabel = graph_params.get("ylabel", "Frequencies")
    saving_path = graph_params.get("saving_path", "../histogram.png")

    # Assegura que el directori existeixi abans de guardar
    directory = os.path.dirname(saving_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Creem l'histograma
    plt.figure(figsize=(10, 8))

    # Ho fem així per poder posar etiquetes a les barres
    counts, _, patches = plt.hist(x=intervals,
                                  bins=len(intervals),
                                  weights=frequencies,
                                  color='orange',
                                  edgecolor='black',
                                  align='mid'
                                  )

    plt.bar_label(patches, labels=[f'{int(c)}' for c in counts], label_type='edge')

    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.savefig(saving_path)

    if show:
        plt.show()

# Referència per afegir labels i crear l'histograma:
# https://www.geeksforgeeks.org/adding-labels-to-histogram-bars-in-matplotlib/


def solve_exercise3(dataframe: pd.DataFrame, hist=True) -> pd.DataFrame:

    """
    Give the answers of the third exercise of the PAC and returns a
    dataframe with grouped times and generates a histogram. Also, it
    prints a dataframe with the grouped times.

    :param
        dataframe(pd.DataFrame): dataframe you want to
                                group time in bins.
        hist(bool): boolean to say if the function make_histogram()
                    have to be executed or not. Optional parameter,
                    by default True
    :return:
        pd.DataFrame: new dataframe with a grouped time column
    """

    # Creem la nova columna
    dataframe["time_grouped"] = dataframe["time"].apply(minutes_002040)

    # Agrupem el dataframe per la nova columna
    dataframe_time_grouped = (dataframe.groupby('time_grouped')
                              .size().reset_index(name="num_cyclists"))

    print("-------------- EXERCICI 3 ----------------\n")
    print(f"Els 15 primers valors després d'agrupar es temps "
          f"són:\n{dataframe.head(15)}")
    print(f"Mostrem els valors del nou dataframe agrupat\n {dataframe_time_grouped}")

    # Mostrem l'histograma (incorporem el paràmetre pels tests, que no volem que el
    # creï ja que el sobreescriuria)
    if hist:
        make_histogram(
            intervals=dataframe_time_grouped['time_grouped'],
            frequencies=dataframe_time_grouped['num_cyclists'],
            graph_params={
                "title": "Histograma dels temps dels ciclistes",
                "xlabel": "Intervals de temps",
                "ylabel": "Frequencies",
                "saving_path": "./img/histogram.png"
            }
        )
    print("------------------------------------------\n")

    return dataframe
