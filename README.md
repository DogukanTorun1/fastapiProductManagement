# Product Management Backend  

A scalable and production-ready backend service for managing products, built with FastAPI, PostgreSQL, Docker, and Kubernetes. This project features role-based access control (RBAC) for admin and user roles, with CRUD operations and authentication.  

---

## Features  
- **Role-Based Access Control (RBAC):**  
  - Admins: Full CRUD permissions  
  - Users: Read-only access  
- **Authentication and Authorization:** Secure login and token-based access.  
- **Database Management:** PostgreSQL with migrations handled by Alembic.  
- **Containerization:** Dockerized for portability.  
- **Orchestration:** Kubernetes for scaling and deployment.

---

## Technologies Used  
- **FastAPI**: Backend framework  
- **PostgreSQL**: Relational database  
- **Alembic**: Database migrations  
- **Docker**: Containerization  
- **Kubernetes**: Deployment and orchestration

---

## Prerequisites  
Ensure you have the following installed:  
- Docker  
- Kubernetes
- Python 3.13+

---

### 1. Clone the Repository  
```bash
git clone https://github.com/DogukanTorun1/fastapiProductManagement.git
```

### 2. Start Kubernetes Pods
```bash
kubectl apply -f postgres_deployment.yaml
kubectl apply -f fastapi_deployment.yaml
```

### 3. Access the Application
```bash
minikube service fastapi-service
```

# File Structure

project-management-backend/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── routes/              # API routes
│   │   ├── auth.py          # Authentication routes
│   │   ├── product.py       # Product routes
│   │   ├── producttype.py   # Product type routes
│   │   └── user.py          # User routes
│   ├── utils.py             # Utility functions
│   ├── database.py          # Database connection and session
│   ├── oauth2.py            # OAuth2 and JWT handling
│   └── config.py            # Configuration and environment management
│
├── alembic/
│   ├── versions/            # Migration files
│   └── env.py               # Alembic configuration
│
├── .github/                 # GitHub-specific configurations
│   └── workflows/           # GitHub Actions for CI/CD
│       └── build-deploy.yml # CI/CD workflow definition
│
├── .gitignore               # Ignored files for Git
├── .dockerignore            # Ignored files for Docker
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── postgres_deployment.yml # Kubernetes deployment for PostgreSQL
├── fastapi_deployment.yml  # Kubernetes deployment for FastAPI
└── README.md                # Project documentation

