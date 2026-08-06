from services.user_service.schemas.user_schema import UserCreate

user = UserCreate(
    full_name="Sunny",
    email="sunny@gmail.com",
    phone="9000000002",
    password="123456",
    role_id=2
)

print(user)