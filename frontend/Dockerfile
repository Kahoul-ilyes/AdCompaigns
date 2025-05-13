# Step 1: Build the frontend
FROM node:20-alpine AS builder

WORKDIR /app

# Copy necessary files to install dependencies
COPY package*.json ./

RUN npm install

# Copy the rest of the files and build the project
COPY . .

RUN npm run build

# Step 2: Static file server with nginx
FROM nginx:stable-alpine

# Remove the default nginx configuration
RUN rm -rf /usr/share/nginx/html/*

# Copy built files to nginx's served directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom nginx config if needed
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
