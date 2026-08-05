1. Purpose

This document defines all REST APIs exposed by the Scalable E-Commerce Platform. It serves as the contract between the frontend, API Gateway, and microservices.

API Standards
Base URL

Development

http://localhost:8000/api/v1

Production

https://yourdomain.com/api/v1
Response Format

Every API returns the same structure.

Success
{
"success": true,
"message": "User registered successfully",
"data": {}
}
Error
{
"success": false,
"message": "Validation failed",
"errors": []
}
Authentication

Most APIs require JWT.

Header

Authorization: Bearer <JWT_TOKEN>
USER SERVICE

Base URL

/api/v1/users
Register User
POST /register
Request
{
"first_name":"Santosh",
"last_name":"Reddy",
"username":"santosh",
"email":"abc@gmail.com",
"phone":"9876543210",
"password":"Password@123"
}
Response
{
"success":true,
"message":"User Registered Successfully"
}

Status Code

201 Created
Login
POST /login
Request
{
"email":"abc@gmail.com",
"password":"Password@123"
}
Response
{
"access_token":"JWT_TOKEN",
"token_type":"Bearer"
}
Get Profile
GET /profile

Authorization Required

Update Profile
PUT /profile
Change Password
PUT /change-password
Delete Account
DELETE /account
PRODUCT SERVICE

Base URL

/api/v1/products
Get All Products
GET /

Query Parameters

?page=1

&size=20

&sort=price

&category=electronics
Get Product By ID
GET /{productId}
Add Product
POST /

Admin Only

Update Product
PUT /{productId}
Delete Product
DELETE /{productId}
Search Products
GET /search

Example

/search?q=laptop
Filter Products
GET /filter

Example

price

category

brand

rating
CATEGORY APIs
GET /categories

POST /categories

PUT /categories/{id}

DELETE /categories/{id}
BRAND APIs
GET /brands

POST /brands

PUT /brands/{id}

DELETE /brands/{id}
CART SERVICE

Base URL

/api/v1/cart
View Cart
GET /
Add Item
POST /add

Request

{
"product_id":5,
"quantity":2
}
Update Quantity
PUT /update
Remove Item
DELETE /remove/{itemId}
Clear Cart
DELETE /clear
ORDER SERVICE

Base URL

/api/v1/orders
Place Order
POST /
Get Orders
GET /
Get Order
GET /{orderId}
Cancel Order
PUT /cancel/{orderId}
Track Order
GET /track/{orderId}
PAYMENT SERVICE

Base URL

/api/v1/payments
Create Payment
POST /
Verify Payment
POST /verify
Payment History
GET /
Refund
POST /refund
NOTIFICATION SERVICE

Base URL

/api/v1/notifications
Send Email
POST /email
Send SMS
POST /sms
Notification History
GET /
API Gateway Routes
Client Request Gateway Routes To
/api/v1/users/_ User Service
/api/v1/products/_ Product Service
/api/v1/cart/_ Cart Service
/api/v1/orders/_ Order Service
/api/v1/payments/_ Payment Service
/api/v1/notifications/_ Notification Service
API Status Codes
Code Description
200 Success
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Validation Error
500 Internal Server Error
Validation Rules
User
Email must be unique
Username must be unique
Password minimum 8 characters
Phone must contain exactly 10 digits
Product
Price > 0
Stock ≥ 0
Product name required
Category required
Order
Cart cannot be empty
Payment must be successful
Stock must be available
Service Communication
Order Service
│
├────────► Product Service
│ (Verify Stock)
│
├────────► Payment Service
│ (Create Payment)
│
└────────► Notification Service
(Order Confirmation)
