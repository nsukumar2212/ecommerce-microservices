from services.user_service.schemas.auth_schema import LoginRequest

user = LoginRequest(
    email="admin@shop.com",
    password="admin123"
)

print(user)