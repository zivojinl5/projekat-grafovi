import networkx as nx
import random


def generisi_ba_random_mrezu(broj_cvorova, broj_grana_koje_dodajemo):
    if broj_cvorova <= broj_grana_koje_dodajemo:
        raise ValueError("Broj grana za povezivanje mora biti manji od broja čvorova.")

    graf = nx.Graph()

    # Inicijalizuj pocetnu mrezu
    početna_veličina = min(broj_cvorova, broj_grana_koje_dodajemo)
    for i in range(početna_veličina):
        for j in range(i + 1, početna_veličina):
            graf.add_edge(i, j)

    # Dodaj preostale cvorove sa preferencijalnim povezivanjem
    for i in range(početna_veličina, broj_cvorova):
        stepeni_cvorova = list(graf.degree())
        ukupan_stepen = sum(stepen for _, stepen in stepeni_cvorova)
        verovatnoce = [stepen / ukupan_stepen for _, stepen in stepeni_cvorova]
        ciljevi = random.choices(
            range(i), weights=verovatnoce, k=broj_grana_koje_dodajemo
        )

        for cilj in ciljevi:
            graf.add_edge(i, cilj)

    return graf
