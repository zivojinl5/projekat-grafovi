import networkx as nx
import pandas as pd


def ucitaj_mreze():
    # Ucitaj 'soc-sign-bitcoinotc.csv'
    bitcoinotc_path = "data/soc-sign-bitcoinotc.csv"
    bitcoinotc_columns = ["SOURCE", "TARGET", "RATING", "TIME"]
    bitcoinotc_data = pd.read_csv(
        bitcoinotc_path, names=bitcoinotc_columns, header=None
    )
    bitcoinotc_graf = nx.from_pandas_edgelist(
        bitcoinotc_data, "SOURCE", "TARGET", edge_attr=["RATING", "TIME"]
    )
    bitcoinotc_ime = "BitcoinOTC_graf"
    grafovi_imena = [bitcoinotc_ime]  # Dodajemo ime u listu imena

    # Ucitaj 'soc-sign-bitcoinalpha.csv'
    bitcoinalpha_path = "data/soc-sign-bitcoinalpha.csv"
    bitcoinalpha_columns = ["SOURCE", "TARGET", "RATING", "TIME"]
    bitcoinalpha_data = pd.read_csv(
        bitcoinalpha_path, names=bitcoinalpha_columns, header=None
    )
    bitcoinalpha_graf = nx.from_pandas_edgelist(
        bitcoinalpha_data, "SOURCE", "TARGET", edge_attr=["RATING", "TIME"]
    )
    bitcoinalpha_ime = "BitcoinAlpha_graf"
    grafovi_imena.append(bitcoinalpha_ime)

    # Ucitaj 'lastfm_asia_edges.csv'
    lastfm_path = "data/lastfm_asia_edges.csv"
    lastfm_columns = ["node_1", "node_2"]
    lastfm_data = pd.read_csv(lastfm_path, names=lastfm_columns)
    lastfm_graf = nx.from_pandas_edgelist(lastfm_data, "node_1", "node_2")
    lastfm_ime = "LastFM_graf"
    grafovi_imena.append(lastfm_ime)

    return bitcoinotc_graf, bitcoinalpha_graf, lastfm_graf, grafovi_imena
