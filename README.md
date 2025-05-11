# 🚀 Fullstack AdCampaign managing App (Vue 3 + FastAPI + MySQL)

This project is a fullstack web application powered by:

- **Frontend**: Vue 3 with Vite
- **Backend**: FastAPI (Python)
- **Database**: MySQL 8
- All orchestrated with **Docker Compose**

---

## ⚙️ Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Getting Started

To run the full application, simply execute:

```bash
docker-compose up --build
```

---

## 🔗 Entrypoints

| Service        | URL                                                        | Description                   |
| -------------- | ---------------------------------------------------------- | ----------------------------- |
| **Frontend**   | [http://localhost:3000](http://localhost:3000)             | Vue 3 Application             |
| **Backend**    | [http://localhost:8000](http://localhost:8000)             | FastAPI Root                  |
| **Swagger UI** | [http://localhost:8000/docs](http://localhost:8000/docs)   | Interactive API Documentation |
| **ReDoc**      | [http://localhost:8000/redoc](http://localhost:8000/redoc) | Static API Docs (ReDoc)       |
| **MySQL**      | `localhost:3306`                                           | Accessible from DB clients    |

