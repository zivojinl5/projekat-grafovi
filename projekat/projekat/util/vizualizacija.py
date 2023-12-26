import networkx as nx
import matplotlib.pyplot as plt


# Vizualizacija
def vizualizuj_podatke(shell_indeksi, metrike, ime_grafa, graf):
    shell_indeks_vrednosti = [shell_indeksi[cvor] for cvor in graf.nodes()]
    (
        degree,
        betweenness_centrality,
        closeness_centrality,
        eigenvector_centrality,
    ) = metrike

    # Stepen
    plt.scatter(shell_indeks_vrednosti, list(degree.values()))
    plt.xlabel("Shell index")
    plt.ylabel("Stepen")
    plt.title(f"{ime_grafa}")
    plt.show()

    # Betweenness centralnost
    plt.scatter(shell_indeks_vrednosti, list(betweenness_centrality.values()))
    plt.xlabel("Shell index")
    plt.ylabel("Betweenness centralnost")
    plt.title(f"{ime_grafa}")
    plt.show()

    # Closeness centralnost
    plt.scatter(shell_indeks_vrednosti, list(closeness_centrality.values()))
    plt.xlabel("Shell index")
    plt.ylabel("Closeness centralnost")
    plt.title(f"{ime_grafa}")
    plt.show()

    # Eigenvector centralnost
    plt.scatter(shell_indeks_vrednosti, list(eigenvector_centrality.values()))
    plt.xlabel("Shell index")
    plt.ylabel("Eigenvector centralnost")
    plt.title(f"{ime_grafa}")
    plt.show()
