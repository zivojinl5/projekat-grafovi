import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from racunanja.racunanje_shell_bz import izracunaj_shell_indekse_bz
from ucitavanja_grafova.ucitavanje_grafova_csv import ucitaj_mreze
from util.nalazenje_jezgara import get_jezgra


def get_num_nodes(graf):
    return graf.number_of_nodes()


def get_num_links(graf):
    return graf.number_of_edges()


def get_density(graf):
    return nx.density(graf)


def get_num_connected_components(graf):
    return nx.number_connected_components(graf)


def get_largest_component(graf):
    return max(nx.connected_components(graf), key=len)


def get_num_nodes_largest_comp(graf):
    najveca_komponenta = get_largest_component(graf)
    return len(najveca_komponenta)


def get_percentage_nodes_largest_comp(graf):
    broj_cvorova = get_num_nodes(graf)
    broj_cvorova_najveca = get_num_nodes_largest_comp(graf)
    return (broj_cvorova_najveca / broj_cvorova) * 100


def get_percentage_links_largest_comp(graf):
    broj_grana = get_num_links(graf)
    najveca_komponenta = get_largest_component(graf)
    if broj_grana > 0:
        broj_grana_najveca = graf.subgraph(najveca_komponenta).number_of_edges()
        return (broj_grana_najveca / broj_grana) * 100
    else:
        return 0


def get_clustering_coefficient(graf):
    return nx.average_clustering(graf)


def get_small_world_coefficient(graf):
    random_graf = nx.random_reference(graf, niter=5)

    # Racunamo prosecan najkraci put koeficijent za oba grafa
    pravi_prosecan_najkraci_put = nx.average_shortest_path_length(graf)
    random_prosecan_najkraci_put = nx.average_shortest_path_length(random_graf)
    # Racunamo clusteing koeficijent za oba grafa
    pravi_clustering_coefficient = get_clustering_coefficient(graf)
    random_clustering_coefficient = get_clustering_coefficient(random_graf)

    small_world_koeficijent = (
        pravi_prosecan_najkraci_put / random_prosecan_najkraci_put
    ) / (pravi_clustering_coefficient / random_clustering_coefficient)

    return small_world_koeficijent


def get_diameter(graf):
    najveca_komponenta = get_largest_component(graf)
    return nx.diameter(graf.subgraph(najveca_komponenta))


def plot_jezgra_vs_metrika(
    metrika, jezgra1, jezgra2, jezgra3, imena_grafova, imena_metrika
):
    metrike1 = [metrika(jezgro) for jezgro in jezgra1]
    metrike2 = [metrika(jezgro) for jezgro in jezgra2]
    metrike3 = [metrika(jezgro) for jezgro in jezgra3]

    plt.figure(figsize=(10, 4))
    plt.subplot(131)
    plt.plot(range(len(metrike1)), metrike1)
    plt.xlabel("Jezgro")
    plt.ylabel(imena_metrika)
    plt.title(f"{imena_grafova[0]}")

    plt.subplot(132)
    plt.plot(range(len(metrike2)), metrike2)
    plt.xlabel("Jezgro")
    plt.ylabel(imena_metrika)
    plt.title(f"{imena_grafova[1]}")

    plt.subplot(133)
    plt.plot(range(len(metrike3)), metrike3)
    plt.xlabel("Jezgro")
    plt.ylabel(imena_metrika)
    plt.title(f"{imena_grafova[2]}")

    plt.tight_layout()
    plt.show()


bitcoinotc_graf, bitcoinalpha_graf, lastfm_graf, imena_grafova = ucitaj_mreze()
bitcoinotc_shell_indeksi = izracunaj_shell_indekse_bz(bitcoinotc_graf)
bitcoinalpha_shell_indeksi = izracunaj_shell_indekse_bz(bitcoinalpha_graf)
lastfm_shell_indeksi = izracunaj_shell_indekse_bz(lastfm_graf)
bitcoinotc_jezgra = get_jezgra(bitcoinotc_graf, bitcoinotc_shell_indeksi)
bitcoinalpha_jezgra = get_jezgra(bitcoinalpha_graf, bitcoinalpha_shell_indeksi)
lastfm_jezgra = get_jezgra(lastfm_graf, lastfm_shell_indeksi)

# Lista funkcija
funkcije = [
    get_num_nodes,
    get_num_links,
    get_density,
    get_num_connected_components,
    get_percentage_nodes_largest_comp,
    get_percentage_links_largest_comp,
    get_clustering_coefficient,
    get_small_world_coefficient,
    get_diameter,
]
imean_metrika = [
    "Broj cvorova",
    "Broj grana",
    "Gustina",
    "Broj povezanih komponenti",
    "Procenat cvorova u najvecoj komponenti",
    "Procenat grana u najvecoj komponenti",
    "Clustering koeficijent",
    "Small-World koeficijent",
    "Precnik",
]
for f, metric_name in zip(funkcije, imean_metrika):
    plot_jezgra_vs_metrika(
        f,
        bitcoinotc_jezgra,
        bitcoinalpha_jezgra,
        lastfm_jezgra,
        imena_grafova,
        metric_name,
    )
