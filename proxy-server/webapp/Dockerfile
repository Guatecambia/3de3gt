FROM node:10.15.1-alpine as build-stage
WORKDIR /app
RUN mkdir 3de3
RUN npm install -g @vue/cli
RUN npm install -g bootstrap-vue
COPY ../../frontend/package*.json ./
RUN npm install -g
WORKDIR /app
COPY ../../frontend .
WORKDIR /app/3de3
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
