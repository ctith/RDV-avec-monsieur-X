#!/usr/bin/env python
# coding: utf-8

from imp import reload
from unidecode import unidecode
import codecs
import xlsxwriter
from xlwt import Workbook
import requests
from bs4 import BeautifulSoup, NavigableString
import re

##################################################################
# création

excel = Workbook('unicode _french_ utf8.xlsx')

# création de la feuille 1
f1 = excel.add_sheet('emission monsieur x')

# ajout des en-têtes
#f1.write(0, 0, 'Date(s) de diffusion(s)')
f1.write(0, 1, 'titre')
f1.write(0, 2, 'description')
f1.write(0, 3, 'bibliographie')
f1.write(0, 4, 'discographie')
f1.write(0, 0, 'mp3')

# taille des colonnes
f1.col(0).width = 8000
f1.col(1).width = 8000
f1.col(2).width = 20000
f1.col(3).width = 8000
f1.col(4).width = 8000
#f1.col(5).width = 8000

# liens à scrapper
contenu = open("liens fiche émission.txt", "r")
liste = contenu.read().splitlines()

# pour chaque page d'émission
for url in liste:
    # créer la ligne excel n°1
    globals()['ligne' + str(liste.index(url)+1)] = f1.row(liste.index(url)+1)
    f1._cell_overwrite_ok = True

    # Recupere reponse HTTP GET du site
    r = requests.get(url)

    # transformer html en dom
    dom = BeautifulSoup(r.text, "html.parser")

    # recuperer ligne html qui nous interesse
    divmp3 = dom.find(id="icone_telechargement").find(href=re.compile("audio"))
    amp3 = str(divmp3).replace('<a href="../', "")
    shortmp3 = amp3[0:25]
    mp3 = "http://rendezvousavecmrx.free.fr/" + shortmp3

    #date = dom.find(id="centre").text
    titre = dom.find(id="titre").text
    description = dom.find(id="emission").text
    bibliographie = dom.find(id="biblio").text
    discographie = dom.find(id="disco").text

    print(titre, description, bibliographie, discographie, mp3)

    # écriture des lignes
    #globals()['ligne' + str(liste.index(url)+1)].write(0, str(date))
    globals()['ligne' + str(liste.index(url)+1)].write(1, str(titre))
    globals()['ligne' + str(liste.index(url)+1)].write(2, str(description))
    globals()['ligne' + str(liste.index(url)+1)].write(3, str(bibliographie))
    globals()['ligne' + str(liste.index(url)+1)].write(4, str(discographie))
    globals()['ligne' + str(liste.index(url)+1)].write(0, str(mp3))

# création matérielle du fichier résultant
excel.save('emissions.xls')