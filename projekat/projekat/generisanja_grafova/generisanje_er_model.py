import networkx as nx
import random


def generisi_er_random_mrezu(broj_cvorova, verovatnoca_grane):
    graf = nx.Graph()

    # Prvo dodaj sve cvorove
    graf.add_nodes_from(range(broj_cvorova))

    # Dodaj ili ne svaku mogucu granu
    for i in range(broj_cvorova):
        for j in range(i + 1, broj_cvorova):
            if random.random() < verovatnoca_grane:
                graf.add_edge(i, j)

    return graf
