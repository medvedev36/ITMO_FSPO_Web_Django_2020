FROM node:current-slim
WORKDIR /my-project/
COPY package.json .
RUN npm install
RUN npm i muse-ui -S
RUN npm install --save-dev @babel/preset-env
EXPOSE 8080
CMD ['npm', 'start']
COPY . .