import networkx as nx


def izracunaj_shell_indekse_standard(graf):
    # Napravi kopiju grafa zbog ocuvanja originala
    kopija = graf.copy()
    mapa_cvor_shell = {cvor: -1 for cvor in kopija.nodes()}

    max_stepen = max(dict(kopija.degree()).values())

    for i in range(max_stepen + 1):
        cvorovi_sa_stepenom_i = [
            cvor for cvor in kopija.nodes() if kopija.degree(cvor) == i
        ]

        # Postavi shell indeks na i za svaki cvor u listi
        for node in cvorovi_sa_stepenom_i:
            mapa_cvor_shell[node] = i

        # Uklanjaj cvorove stepena i iz grafa i nastavite dok ih ima
        while cvorovi_sa_stepenom_i:
            cvor_koji_uklanjamo = cvorovi_sa_stepenom_i.pop()
            susedi_sa_stepenom_i = [
                cvor
                for cvor in kopija.neighbors(cvor_koji_uklanjamo)
                if kopija.degree(cvor) == i + 1
            ]
            # Azurirati listu sa odgovarajucim susedima
            cvorovi_sa_stepenom_i.extend(susedi_sa_stepenom_i)
            kopija.remove_node(cvor_koji_uklanjamo)

            for cvor in susedi_sa_stepenom_i:
                mapa_cvor_shell[cvor] = i

    return mapa_cvor_shell
