FROM node:18-alpine3.18

WORKDIR /display

COPY public/ /display/public
COPY src/ /display/src
COPY package.json /display/

RUN npm install

CMD ["npm", "start"]

