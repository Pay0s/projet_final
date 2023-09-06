# Utilisez l'image de base Python 3.8
FROM python:3.8

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgl1 -y

# Définissez le répertoire de travail dans l'image
WORKDIR /app

# Copiez le code de l'application dans le conteneur
COPY . /app

# Installez les dépendances nécessaires depuis le fichier requirements.txt
RUN pip install -r requirements.txt

# Exposez le port sur lequel l'application écoute (remplacez 8080 par le port approprié)
EXPOSE 5000

# Commande pour exécuter l'application Python (remplacez "app.py" par le nom de votre fichier principal)
CMD ["flask", "run", "--host=0.0.0.0"]