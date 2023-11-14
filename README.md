# ue19_labo09-10

## Ceci est une application Python 3 qui interroge une service d'API public nommé PunAPI

### Description

Ce projet est une application Python qui interroge l'API PunAPI pour afficher un jeu de mots. L'application utilise la bibliothèque "requests" pour effectuer une requête GET à l'URL de l'API PunAPI, puis affiche le jeu de mots si la requête réussit.

## Comment installer et exécuter le projet

- Tout d'abord, installez tous les fichiers du dépôt GitHub sur votre machine.
- Ensuite, ouvrez votre invite de commande en mode administrateur.
- Installez et ouvrez également l'application Docker Desktop.
- Changer dans le fichier Dockerfile.tkt, a la suite de "WORKDIR", et placez votre chemin d'accés vers le repertoire ou ce trouve
- Saisissez la commande suivante dans l'invite de commande : "docker build . -f Dockerfile.txt -t app-api".
- L'image sera ainsi créée dans Docker Desktop avec le nom "app-api".
- Ensuite, saisissez la commande : "docker run --rm -it app-api" pour lancer cette image.
- Vous pouvez également créer un conteneur en appuyant sur le bouton "play" sur l'image, ce qui vous permettra de lancer l'application.

## Lien d'aide

https://stackoverflow.com/questions/64985913/failed-to-solve-with-frontend-dockerfile
