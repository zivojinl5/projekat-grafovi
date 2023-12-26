import networkx as nx
import random


def izracunaj_shell_indekse_bz(graf):
    stepeni = dict(graf.degree())
    maks_stepen = max(stepeni.values())

    skupovi_cvorova = [set() for stepen in range(maks_stepen + 1)]

    for cvor, stepen in stepeni.items():
        skupovi_cvorova[stepen].add(cvor)

    mapa_cvor_shell = {}

    for stepen in range(maks_stepen + 1):
        while skupovi_cvorova[stepen]:
            random_cvor = random.choice(list(skupovi_cvorova[stepen]))
            skupovi_cvorova[stepen].remove(random_cvor)
            mapa_cvor_shell[random_cvor] = stepen

            for sused in graf.neighbors(random_cvor):
                if stepeni[sused] > stepen:
                    skupovi_cvorova[stepeni[sused]].remove(sused)
                    skupovi_cvorova[stepeni[sused] - 1].add(sused)
                    stepeni[sused] = stepeni[sused] - 1

    return mapa_cvor_shell
