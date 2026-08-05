1.1 Project Title

Scalable E-Commerce Platform Using Microservices Architecture

1.2 Project Vision

Develop a scalable, secure, and high-performance e-commerce platform where each business function is implemented as an independent microservice. The system should support customer shopping, product management, order processing, payment handling, and notifications while remaining easy to maintain and scale.

1.3 Project Objective

Build a modern online shopping platform that:

Supports multiple users simultaneously
Uses microservices for independent development and scaling
Provides secure authentication and authorization
Allows customers to browse and purchase products
Enables administrators to manage products, inventory, and orders
Can be extended with caching, messaging, monitoring, and cloud deployment in the future
1.4 Problem Statement

Many traditional e-commerce systems are built as monolithic applications. As the number of users and features grows, these systems become difficult to maintain, update, and scale.

This project addresses these challenges by adopting a microservices architecture, where each business capability is developed as an independent service. This improves scalability, maintainability, fault isolation, and future extensibility.

1.5 Project Scope
Customer Features
User Registration
Secure Login
Profile Management
Product Browsing
Category Browsing
Product Search
Product Filtering
Shopping Cart
Checkout
Payment
Order History
Order Tracking
Product Reviews
Wishlist (Future)
Admin Features
Admin Login
Dashboard
Product Management
Category Management
Brand Management
Inventory Management
Customer Management
Order Management
Sales Analytics
1.6 Target Users
User Type Responsibilities
Customer Browse products, place orders, manage profile
Admin Manage products, inventory, orders, users, reports
System Authentication, notifications, payment processing
1.7 Business Modules
Module Description
User Management Registration, login, profile, addresses
Product Management Products, categories, brands, inventory
Shopping Cart Add, remove, update items
Order Management Place and track orders
Payment Management Process payments and refunds
Notification Management Email and SMS notifications
Administration Manage products, orders, users
1.8 Microservices
Service Responsibility Database
User Service Authentication, profile, roles user_db
Product Service Products, categories, inventory product_db
Cart Service Shopping cart cart_db
Order Service Orders order_db
Payment Service Payments payment_db
Notification Service Email & SMS notification_db
API Gateway Request routing None
1.9 Technology Stack
Frontend
React.js
Vite
Bootstrap
Axios
React Router
Backend
FastAPI
SQLAlchemy
Pydantic
JWT
Passlib
Database
MySQL
Tools
Git
GitHub
Postman
VS Code
1.10 Expected Outcomes

At the end of the project, the system should allow users to:

Register and log in securely
Browse products
Search and filter products
Add products to a shopping cart
Place orders
Make payments
Receive notifications
Track order status

Administrators should be able to:

Manage products
Manage inventory
Manage users
Manage orders
View sales information
1.11 High-Level Workflow
Customer
│
▼
React Frontend
│
▼
API Gateway
│
├───────────────┬───────────────┬───────────────┐
▼ ▼ ▼ ▼
User Service Product Service Cart Service Order Service
│
▼
Payment Service
│
▼
Notification Service
1.12 Success Criteria

The project will be considered successful if it:

Implements all planned microservices
Provides secure JWT-based authentication
Supports complete customer and admin workflows
Ensures independent databases for each service
Uses clean, modular architecture
Is documented and testable
Can be enhanced later with Docker, Redis, RabbitMQ, Kubernetes, and CI/CD
