# Inventory Management System

![AWS](https://img.shields.io/badge/Deployed-AWS-orange)
![Django](https://img.shields.io/badge/Backend-Django%20REST-green)
![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-blue)

A full-stack inventory management system with separate backend and frontend repositories, deployed on AWS using Docker and GitHub Actions.

## Features
- Product Management
    -CRUD Operation
    -Store Product name, Description, Price and Stock quantity
- Inventory Management
    -Track stock levels
    -Api to get low-stock alerts
- User authentication
- Responsive UI
- REST API backend
- CI/CD Pipeline
- Dockerized deployment

## Tech Stack
**Backend:**
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker

**Frontend:**
- React
- Vite
- Tailwind CSS
- Axios
- Docker

**DevOps:**
- AWS EC2
- GitHub Actions
- Nginx
- Docker Hub

## Project Structure
├── api/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
├── backend/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── Dockerfile
├── manage.py
├── requirements.txt
└── deploy.yml