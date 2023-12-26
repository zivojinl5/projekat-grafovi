import networkx as nx
import matplotlib.pyplot as plt


def izracunaj_metrike_centralnosti(graf):
    stepen = dict(nx.degree(graf))

    betweenness_centralnost = nx.betweenness_centrality(graf)
    closeness_centralnost = nx.closeness_centrality(graf)
    eigenvector_centralnost = nx.eigenvector_centrality(graf)

    return (
        stepen,
        betweenness_centralnost,
        closeness_centralnost,
        eigenvector_centralnost,
    )
