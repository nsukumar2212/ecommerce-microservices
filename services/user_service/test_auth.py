from shared.auth.jwt_handler import create_access_token
from shared.auth.auth_dependency import get_current_user

token = create_access_token(
    {
        "sub": "admin@shop.com",
        "role": 1
    }
)

print(token)