import networkx as nx
import matplotlib.pyplot as plt

from generisanja_grafova.generisanje_er_model import generisi_er_random_mrezu
from generisanja_grafova.generisanje_ba_model import generisi_ba_random_mrezu
from generisanja_grafova.generisanje_pp_model import planted_partition_model
from racunanja.racunanje_shell_bz import izracunaj_shell_indekse_bz
from racunanja.racunanje_shell_standardno import (
    izracunaj_shell_indekse_standard,
)
from poredenja_grafova.poredenje_shell_index import uporedi_shell_indekse


# Generisanja
# Generisanje ER random mrezu
er_broj_cvorova = 2000
er_verovatnoca_ivice = 0.2

slucajna_mreza_er = generisi_er_random_mrezu(er_broj_cvorova, er_verovatnoca_ivice)

# Generisanje BA random mreze
ba_broj_cvorova = 2000
ba_broj_ivica_za_povezivanje = 3

slucajna_mreza_ba = generisi_ba_random_mrezu(
    ba_broj_cvorova, ba_broj_ivica_za_povezivanje
)
# Generisanje mreze po Planted partition modelu
ppm_broj_cvorova = 2000
ppm_velicina_osnovnog_grafa = 500
ppm_velicina_periferije = 1500
ppm_p_osnovnog_grafa = 0.2
ppm_p_periferije = 0.05
ppm_p_preseka = 0.1

slucajna_mreza_ppm = planted_partition_model(
    ppm_broj_cvorova,
    ppm_velicina_osnovnog_grafa,
    ppm_velicina_periferije,
    ppm_p_osnovnog_grafa,
    ppm_p_periferije,
    ppm_p_preseka,
)


# Racunanje shell indeksa
# Racunanje shell indeksa za ER random mrezu
shell_indeksi_er_metod_1 = izracunaj_shell_indekse_bz(slucajna_mreza_er)
shell_indeksi_er_metod_2 = izracunaj_shell_indekse_standard(slucajna_mreza_er)
# Racunanje shell indeksa za BA random mrezu
shell_indeksi_ba_metod_1 = izracunaj_shell_indekse_bz(slucajna_mreza_ba)
shell_indeksi_ba_metod_2 = izracunaj_shell_indekse_standard(slucajna_mreza_ba)
# Racunanje shell indeksa za mrezu generisanu po Planted partition modelu
shell_indeksi_ppm_metod_1 = izracunaj_shell_indekse_bz(slucajna_mreza_ppm)
shell_indeksi_ppm_metod_2 = izracunaj_shell_indekse_standard(slucajna_mreza_ppm)


# Poredenje i stampanje rezultata
procenat_isti_er = uporedi_shell_indekse(
    shell_indeksi_er_metod_1, shell_indeksi_er_metod_2
)
print(
    f"ER random mreza - Procenat cvorova sa istim shell indeksom: {procenat_isti_er}%"
)
procenat_isti_ba = uporedi_shell_indekse(
    shell_indeksi_ba_metod_1, shell_indeksi_ba_metod_2
)
print(
    f"BA random mreza - Procenat cvorova sa istim shell indeksom: {procenat_isti_ba}%"
)
procenat_isti_ppm = uporedi_shell_indekse(
    shell_indeksi_ppm_metod_1, shell_indeksi_ppm_metod_2
)
print(
    f"Mreza Planted partition model - Procenat cvorova sa istim shell indeksom: {procenat_isti_ppm}%"
)
