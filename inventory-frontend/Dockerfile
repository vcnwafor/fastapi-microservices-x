FROM node:16.13.0-alpine3.14

WORKDIR /app

COPY ./package.json /app/package.json

RUN npm install

COPY . /app/

# Use the environment variables directly in the Dockerfile
ENV BACKEND_API_URL $BACKEND_API_URL

RUN npm run build

EXPOSE 3000