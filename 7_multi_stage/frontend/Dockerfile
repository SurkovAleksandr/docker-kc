FROM node:22 AS build
WORKDIR /app/frontend
COPY todo-list .
RUN npm install && npm install react-scripts --save-dev && npm run build

FROM nginx:1.29
WORKDIR /app/nginx
COPY --from=build /app/frontend/dist/index.html static/index.html
COPY --from=BUILD /app/frontend/dist/static/css static/css
COPY --from=BUILD /app/frontend/dist/static/js static/js