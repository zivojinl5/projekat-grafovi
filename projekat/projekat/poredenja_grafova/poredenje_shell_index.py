import networkx


def uporedi_shell_indekse(mapa_cvor_shell_1, mapa_cvor_shell_2):
    brojac_isti_indeksi = 0
    ukupno_cvorova = len(mapa_cvor_shell_1)

    for cvor in mapa_cvor_shell_1.keys():
        index_method_1 = mapa_cvor_shell_1.get(cvor, "N/A")
        index_method_2 = mapa_cvor_shell_2.get(cvor, "N/A")
        if index_method_1 == index_method_2:
            brojac_isti_indeksi += 1

    # Izracunaj procenat cvorova sa istim shell indeksima
    procenat_poklapanja = (
        (brojac_isti_indeksi / ukupno_cvorova) * 100 if ukupno_cvorova > 0 else 0
    )

    return procenat_poklapanja
