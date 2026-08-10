# User Service APIs

## Authentication

POST /api/v1/auth/register

POST /api/v1/auth/login

## Profile

GET /api/v1/users/me

PUT /api/v1/users/me

PUT /api/v1/users/change-password

## Address

POST /api/v1/users/address

GET /api/v1/users/address

PUT /api/v1/users/address/{id}

DELETE /api/v1/users/address/{id}

## Admin

GET /api/v1/admin/users

GET /api/v1/admin/users/{id}

PUT /api/v1/admin/users/{id}/role

DELETE /api/v1/admin/users/{id}
