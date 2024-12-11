# Étape 1 : Construction de l'application frontend avec Node.js
FROM node:16 AS build

WORKDIR /app
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend ./
RUN npm run build

# Étape 2 : Utiliser Nginx pour servir l'application construite
FROM nginx:1.23

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
