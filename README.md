# RDV-avec-monsieur-X
Scrapping du site

But : récupérer tous les mp3 du site http://rendezvousavecmrx.free.fr
```shell
wget -r -nd -A.mp3 http://rendezvousavecmrx.free.fr/page/liste.php?tri=3
```

MAIS, on a souvent des coupures de wifi, ce qui plombe tout le téléchargement (30h pour 22,5 Go de mp3 à retélécharger, ce n'est pas négligeable.) Donc, les scripts permettent de récupérer toutes les données dans un fichier texte ou excel afin de lancer un wget par année et limiter les risques de pertes d'émissions lors de leur téléchargement.

