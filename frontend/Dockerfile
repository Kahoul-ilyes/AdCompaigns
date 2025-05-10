FROM node:20-alpine

# Crée un dossier de travail
WORKDIR /app

# Copie uniquement les fichiers nécessaires à l'installation
COPY package*.json ./

# Installe les dépendances
RUN npm install

# Copie le reste du projet
COPY . .

# Expose le port par défaut de Vite
EXPOSE 5173

# Lance le serveur de dev
CMD ["npm", "run", "dev", "--", "--host"]
