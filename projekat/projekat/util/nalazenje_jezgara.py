import networkx
from collections import defaultdict


def get_jezgra(graf, mapa_cvor_shell):
    jezgra = defaultdict(list)

    for cvor, indeks in mapa_cvor_shell.items():
        if indeks not in jezgra:
            jezgra[indeks] = []
        jezgra[indeks].append(cvor)

    jezgra_podgrafi = []

    for indeks, cvorovi in jezgra.items():
        jezgro_podgraf = graf.subgraph(cvorovi)
        jezgra_podgrafi.append(jezgro_podgraf)

    return jezgra_podgrafi
