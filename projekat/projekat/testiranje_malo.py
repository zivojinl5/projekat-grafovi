import networkx as nx
import matplotlib.pyplot as plt

from racunanja_shell_indeksa.racunanje_shell_bz import izracunaj_shell_indekse_bz

# Lista cvorov, za svaki ista
cvorovi = list(range(1, 21))

# Grane za svaki graf
grane1 = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 11),
    (4, 12),
    (4, 13),
    (5, 14),
    (5, 15),
    (5, 16),
    (6, 17),
    (6, 18),
    (6, 19),
    (7, 20),
]

grane2 = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 11),
    (4, 12),
    (4, 13),
    (5, 14),
    (5, 15),
    (5, 16),
    (6, 17),
    (6, 18),
    (6, 19),
    (7, 20),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 12),
    (13, 14),
    (14, 15),
    (15, 16),
    (17, 18),
    (18, 19),
    (19, 20),
]

grane3 = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 11),
    (4, 12),
    (4, 13),
    (5, 14),
    (5, 15),
    (5, 16),
    (6, 17),
    (6, 18),
    (6, 19),
    (7, 20),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 12),
    (13, 14),
    (14, 15),
    (15, 16),
    (17, 18),
    (18, 19),
    (19, 20),
    (8, 13),
    (11, 16),
    (17, 20),
]

graf1 = nx.Graph()
graf1.add_nodes_from(cvorovi)
graf1.add_edges_from(grane1)

graf2 = nx.Graph()
graf2.add_nodes_from(cvorovi)
graf2.add_edges_from(grane2)

graf3 = nx.Graph()
graf3.add_nodes_from(cvorovi)
graf3.add_edges_from(grane3)

# Iscrtaj grafove
plt.figure(figsize=(10, 3))

plt.subplot(131)
nx.draw(graf1, with_labels=True)
plt.title("Graf 1")

plt.subplot(132)
nx.draw(graf2, with_labels=True)
plt.title("Graf 2")

plt.subplot(133)
nx.draw(graf3, with_labels=True)
plt.title("Graf 3")

plt.tight_layout()
plt.show()


shell_indeksi_1 = izracunaj_shell_indekse_bz(graf1)
for cvor, shell_index in shell_indeksi_1.items():
    print(f"Cvor: {cvor}, Shell indeks: {shell_index}")
shell_indeksi_2 = izracunaj_shell_indekse_bz(graf2)
for cvor, shell_index in shell_indeksi_2.items():
    print(f"Cvor: {cvor}, Shell indeks: {shell_index}")
shell_indeksi_3 = izracunaj_shell_indekse_bz(graf3)
for cvor, shell_index in shell_indeksi_3.items():
    print(f"Cvor: {cvor}, Shell indeks: {shell_index}")
