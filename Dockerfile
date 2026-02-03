# Utiliser une image Python légère
FROM python:3.11-slim

# Désactiver buffer pour voir les logs immédiatement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le dossier de travail dans le container
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier tout le code du projet
COPY . /app/

# Exposer le port Django
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
