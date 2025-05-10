# Étape 1 : Image de base
FROM python:3.11-slim

# Étape 2 : Installer netcat-openbsd pour wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd curl && apt-get clean

# Étape 3 : Définir le répertoire de travail
WORKDIR /app

# Étape 4 : Copier les fichiers nécessaires
COPY ./app /app

# Ajoute le chemin du projet au PYTHONPATH
ENV PYTHONPATH=/app/app

# Étape 5 : Copier le script wait-for-it.sh
RUN curl -sSL https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -o /wait-for-it.sh

# Étape 6 : Rendre wait-for-it.sh exécutable
RUN chmod +x /wait-for-it.sh

# Étape 7 : Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 8 : Lancer l’application avec wait-for-it.sh
CMD ["/wait-for-it.sh", "mysql:3306", "--", "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
