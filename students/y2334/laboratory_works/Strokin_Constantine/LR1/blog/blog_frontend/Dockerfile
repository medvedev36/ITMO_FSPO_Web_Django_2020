FROM node:latest


WORKDIR /code/

COPY package*.json /code/
COPY . .

RUN npm install


EXPOSE 8080

CMD ["npm", "start"]
