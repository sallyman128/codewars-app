FROM node:18-alpine3.18

WORKDIR /display

COPY public/ /display/public
COPY src/ /display/src
COPY package.json /display/

RUN --mount=type=cache,target=/root/.npm \
    --mount=type=bind,source=package.json,target=package.json \
    npm install

CMD ["npm", "start"]

