import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from racunanja.racunanje_shell_bz import izracunaj_shell_indekse_bz
from ucitavanja_grafova.ucitavanje_grafova_csv import ucitaj_mreze
from racunanja.racunanje_metrika_centralnosti import izracunaj_metrike_centralnosti
from racunanja.racunanje_korelacija import izracunaj_korelacije
from util.vizualizacija import vizualizuj_podatke


# Ucitaj mreze
graf1, graf2, graf3, imena_grafova = ucitaj_mreze()

shell_indeksi_graf1 = izracunaj_shell_indekse_bz(graf1)
shell_indeksi_graf2 = izracunaj_shell_indekse_bz(graf2)
shell_indeksi_graf3 = izracunaj_shell_indekse_bz(graf3)

shell_indeksi_lista = [shell_indeksi_graf1, shell_indeksi_graf2, shell_indeksi_graf3]


for i, graf in enumerate([graf1, graf2, graf3]):
    shell_indeksi = shell_indeksi_lista[i]
    ime_grafa = imena_grafova[i]

    metrike = izracunaj_metrike_centralnosti(graf)

    vizualizuj_podatke(shell_indeksi, metrike, ime_grafa, graf)

    (
        korelacija_stepeni,
        betweenness_korelacija,
        closeness_korelacija,
        eigenvector_korelacija,
    ) = izracunaj_korelacije(shell_indeksi, metrike, graf)

    print(f"Korelacija za graf '{imena_grafova[i]}':")
    print("Stepen:", korelacija_stepeni)
    print("Betweenness centralnost:", betweenness_korelacija)
    print("Closeness centralnost:", closeness_korelacija)
    print("Eigenvector centralnost:", eigenvector_korelacija)
