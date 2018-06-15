import requests
from bs4 import BeautifulSoup
import re

# structure de la page html
url = "http://rendezvousavecmrx.free.fr/page/liste.php?tri=3"

"""
<tr class="gris">
    <td class="icone">
        <a href="../audio/mr_x_1997_01_04.mp3"><img src="../image/haut_parleur_petit.png" alt="La 5Ã¨me colonne" title="La 5Ã¨me colonne" /></a></td>
    <td class="titre_emission">
        <a href="detail_emission.php?cle_emission=1">La 5Ã¨me colonne</a></td>
</tr>
<tr class="">
    <td class="icone">
        <a href="../audio/mr_x_1997_01_11.mp3"><img src="../image/haut_parleur_petit.png" alt="Rennes-le-ChÃ¢teau et l'abbÃ© SauniÃ¨res" title="Rennes-le-ChÃ¢teau et l'abbÃ© SauniÃ¨res" /></a></td>
    <td class="titre_emission">
        <a href="detail_emission.php?cle_emission=2">Rennes-le-ChÃ¢teau et l'abbÃ© SauniÃ¨res</a></td>
</tr>
...
"""

# Recupere reponse HTTP GET du site
r = requests.get(url)

# fichier output liens a telecharger
f = open("liens mp3.txt", "w")

# transformer html en dom
dom = BeautifulSoup(r.text, "html.parser")

# recuperer ligne html qui nous interesse
liensHTML = dom.find_all(href=re.compile("audio"))

# recuperer info dans le bloc html qui nous interesse
for liens in liensHTML:
    liensCourts = str(liens.get('href'))
    liensCourts = liensCourts.replace("../", "")
    print (liensCourts)


    liensLongs = "http://rendezvousavecmrx.free.fr/"+liensCourts+'\n'
    f.write(liensLongs)
    print(liensLongs)

f.close()