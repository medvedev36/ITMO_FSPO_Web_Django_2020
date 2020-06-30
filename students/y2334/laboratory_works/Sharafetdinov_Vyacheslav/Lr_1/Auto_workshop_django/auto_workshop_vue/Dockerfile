FROM node:10-alpine

WORKDIR /auto_workshop_vue
COPY package.json .
RUN npm install
RUN npm i muse-ui -S
RUN npm install --save-dev @babel/preset-env
RUN npm install --save-dev node-loader
RUN npm install --save-dev sass-loader
COPY . /auto_workshop_vue
EXPOSE 8080

CMD ['npm', 'start']