import networkx as nx
import random


def planted_partition_model(
    n, veličina_centra, veličina_periferije, p_centar, p_periferija, p_preklapanje
):
    # Parametri:
    # - n: Ukupan broj čvorova u mreži.
    # - veličina_centra: Broj čvorova u centru.
    # - veličina_periferije: Broj čvorova u periferiji.
    # - p_centar: Verovatnoća formiranja grane unutar centra.
    # - p_periferija: Verovatnoća formiranja grane unutar periferije.
    # - p_preklapanje: Verovatnoća formiranja grane između centra i periferije.

    if veličina_centra + veličina_periferije != n:
        raise ValueError("veličina_centra + veličina_periferije moraju biti jednaki n")

    G = nx.Graph()

    # Kreiranje čvorova i podela u centar i periferiju
    cvorovi = list(range(n))
    cvorovi_centar = cvorovi[:veličina_centra]
    cvorovi_periferija = cvorovi[veličina_centra:]

    # Dodavanje grana unutar centra
    for i in range(veličina_centra):
        for j in range(i + 1, veličina_centra):
            if random.random() < p_centar:
                G.add_edge(cvorovi_centar[i], cvorovi_centar[j])

    # Dodavanje grana unutar periferije
    for i in range(veličina_periferije):
        for j in range(i + 1, veličina_periferije):
            if random.random() < p_periferija:
                G.add_edge(cvorovi_periferija[i], cvorovi_periferija[j])

    # Dodavanje grana između centra i periferije
    for centralni_cvor in cvorovi_centar:
        for perferijski_cvor in cvorovi_periferija:
            if random.random() < p_preklapanje:
                G.add_edge(centralni_cvor, perferijski_cvor)

    return G
