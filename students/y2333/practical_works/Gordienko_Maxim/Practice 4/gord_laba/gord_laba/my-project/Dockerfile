FROM node:10-alpine
WORKDIR /my-project
COPY package.json .
RUN npm install
RUN npm i muse-ui -S
RUN npm install --save-dev @babel/preset-env
COPY . /my-project
EXPOSE 8080
CMD ['npm', 'start'] 



