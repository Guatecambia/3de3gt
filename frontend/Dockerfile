FROM node:10.15.1-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

RUN mkdir 3de3

# install vue.clie
RUN npm install -g @vue/cli

# install bootstrap dependencies
#RUN npm install -g bootstrap jquery popper.js
RUN npm install -g bootstrap-vue

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install -g

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

WORKDIR /app/3de3

EXPOSE 8080
# CMD [ "http-server", "dist" ]
