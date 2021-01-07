# Création d'une application Streamlit permettant de faire des requêtes SQL sur une base de données comprenant des données sur le suicide, l'indicateur de bonheur et le taux d'homicide de différents pays dans le monde. 

Les différentes étapes du projet : 
- Scraper un tableau sur Wikipédia indiquant le taux d'homicide volontaire pour différents pays dans le monde et conversion des données en dataset
- Import de deux datasets, l'un sur l'indicateur de bonheur dans différents pays et l'autre sur le taux de suicide de 1985 à 2016
- Nettoyage des datasets et concaténation des trois datasets en un dataset final
- Création de tables de relation pour la base SQL
- Elaboration de deux fichiers Docker : un Dockerfile et un docker-compose pour créer deux conteneurs Docker, un pour la base SQL et un pour l'application Streamlit, et les relier entre
eux afin de pouvoir lancer une instance de l'application par le biais de Docker en local. 

