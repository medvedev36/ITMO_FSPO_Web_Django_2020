FROM node:14.4.0-alpine3.10

ENV CI=true

WORKDIR /frontend
COPY package.json .
RUN npm i && npm audit fix
COPY . .
EXPOSE 3000

