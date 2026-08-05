Software Requirements Specification (SRS)

1. Introduction
   1.1 Purpose

The purpose of this document is to define the software requirements for the Scalable E-Commerce Platform using Microservices Architecture.

The system enables customers to purchase products online while allowing administrators to manage products, inventory, orders, users, and payments.

1.2 Scope

The system provides:

User Registration
Authentication
Product Management
Shopping Cart
Order Management
Payment Processing
Notifications
Admin Dashboard

The platform follows a Microservices Architecture where every module operates independently.

1.3 Definitions
Term Description
API Application Programming Interface
JWT JSON Web Token
Microservice Independent service responsible for one business capability
Gateway Entry point for client requests
CRUD Create, Read, Update, Delete 2. Overall Description
Product Perspective

The platform consists of:

React Frontend
API Gateway
User Service
Product Service
Cart Service
Order Service
Payment Service
Notification Service
Separate MySQL database for each service
Product Functions

The platform should support:

User Authentication
Product Browsing
Product Search
Cart Management
Checkout
Payment
Order Tracking
Email Notifications
Admin Management
User Classes
Customer

Permissions

Register
Login
Browse Products
Add Cart
Place Orders
Payment
Track Orders
Administrator

Permissions

Manage Products
Manage Categories
Manage Inventory
Manage Orders
Manage Customers 3. Functional Requirements
User Module
FR-001

Customer shall register using

Name
Email
Password
Phone Number
FR-002

Customer shall login using

Email
Password
FR-003

System shall generate JWT Token.

FR-004

Customer shall update profile.

FR-005

Customer shall manage addresses.

Product Module
FR-101

Admin shall add products.

FR-102

Admin shall update products.

FR-103

Admin shall delete products.

FR-104

Customer shall browse products.

FR-105

Customer shall search products.

FR-106

Customer shall filter products.

FR-107

Customer shall view product details.

Cart Module
FR-201

Customer shall add products.

FR-202

Customer shall update quantity.

FR-203

Customer shall remove products.

FR-204

Customer shall clear cart.

FR-205

Customer shall view cart summary.

Order Module
FR-301

Customer shall place order.

FR-302

Customer shall cancel order.

FR-303

Customer shall view order history.

FR-304

Customer shall track order.

Payment Module
FR-401

Customer shall pay online.

FR-402

System shall verify payment.

FR-403

System shall generate transaction ID.

FR-404

System shall update payment status.

Notification Module
FR-501

System shall send order confirmation email.

FR-502

System shall send shipping updates.

FR-503

System shall send password reset email.

Admin Module
FR-601

Admin shall manage products.

FR-602

Admin shall manage categories.

FR-603

Admin shall manage inventory.

FR-604

Admin shall manage users.

FR-605

Admin shall manage orders.

4. Non-Functional Requirements
   Performance
   API response time should generally be under 2 seconds for normal operations.
   Search should return results quickly even with a large product catalog.
   Security
   JWT Authentication
   Password Encryption (bcrypt)
   Role-Based Access Control
   HTTPS in production
   Input Validation
   Scalability

System should support

Independent service deployment
Horizontal scaling
Database scaling
Reliability
Error handling
Logging
Backup
Recovery
Maintainability
Modular Code
Documentation
Standard Naming
API Versioning 5. System Constraints
Backend Framework: FastAPI
Frontend: React
Database: MySQL
Communication: REST API
Authentication: JWT
Initial deployment without Docker 6. Assumptions
Users have internet access.
MySQL server is available.
SMTP server is available for emails.
Payment gateway may initially be mocked. 7. Business Rules
BR-001

Email must be unique.

BR-002

Username must be unique.

BR-003

Products with zero stock cannot be ordered.

BR-004

Only Admin can manage products.

BR-005

Payment must succeed before an order is confirmed.

BR-006

Only authenticated users can place orders.

BR-007

Cancelled orders cannot be shipped.

BR-008

Inventory must be updated after a successful order.

8. External Interfaces
   Frontend
   React Application
   Database
   MySQL
   Payment Gateway
   Mock Payment
   Stripe (Future)
   Razorpay (Future)
   Email Service
   SMTP
   SendGrid (Future)
9. Use Cases
   UC-01

User Registration

UC-02

User Login

UC-03

Browse Products

UC-04

Search Products

UC-05

Add Cart

UC-06

Checkout

UC-07

Payment

UC-08

Track Order

UC-09

Manage Products

UC-10

Manage Inventory

10. Acceptance Criteria

The project is accepted when:

Customers can register and log in.
JWT authentication works.
Products can be created, updated, deleted, and searched.
Shopping cart functions correctly.
Orders can be placed and tracked.
Payments are processed successfully.
Notifications are sent.
Admin can manage products, users, inventory, and orders.
Services communicate correctly through the API Gateway.
All APIs are tested and documented.
