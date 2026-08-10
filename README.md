"# Scalable-E-Commerce-Platform-Using-Microservices-Architecture" 
# Scalable E-Commerce Platform

A scalable microservices-based e-commerce application built using FastAPI, MySQL, React, and AWS.

## Tech Stack

Backend

- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Passlib (bcrypt)

Frontend

- React
- Bootstrap
- Axios

Database

- MySQL

Deployment

- AWS EC2
- AWS RDS

Version Control

- Git
- GitHub

---

## Project Structure

services/
│
├── user_service
├── product_service
├── cart_service
├── order_service
├── payment_service
├── notification_service
│
gateway/
│
shared/
│
frontend/

---

## Features Completed

### User Service

✔ Register

✔ Login

✔ JWT Authentication

✔ Password Hashing

✔ Get Current User

✔ Update Profile

✔ Change Password

✔ Address CRUD

✔ Admin APIs

✔ RBAC

---

## Remaining Services

- Product Service
- Cart Service
- Order Service
- Payment Service
- Notification Service
- API Gateway
- React Frontend

---

## How to Run

### Clone

git clone <repository-url>

### Create Virtual Environment

python -m venv backend_env

### Activate

backend_env\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run

uvicorn services.user_service.main:app --reload --port 8001

Swagger

http://127.0.0.1:8001/docs
