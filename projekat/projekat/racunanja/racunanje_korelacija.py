import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import spearmanr


def izracunaj_korelacije(shell_indeksi, metrike, graf):
    shell_indeks_vrednosti = [shell_indeksi[cvor] for cvor in graf.nodes()]
    (
        stepen,
        betweenness_centralnost,
        closeness_centralnost,
        eigenvector_centralnost,
    ) = metrike

    korelacija_stepeni = spearmanr(shell_indeks_vrednosti, list(stepen.values()))
    betweenness_korelacija = spearmanr(
        shell_indeks_vrednosti, list(betweenness_centralnost.values())
    )
    closeness_korelacija = spearmanr(
        shell_indeks_vrednosti, list(closeness_centralnost.values())
    )
    eigenvector_korelacija = spearmanr(
        shell_indeks_vrednosti, list(eigenvector_centralnost.values())
    )

    return (
        korelacija_stepeni,
        betweenness_korelacija,
        closeness_korelacija,
        eigenvector_korelacija,
    )
