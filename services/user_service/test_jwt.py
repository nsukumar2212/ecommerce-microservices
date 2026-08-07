from shared.auth.jwt_handler import (
    create_access_token,
    verify_access_token
)

token = create_access_token(
    {
        "sub": "admin@shop.com",
        "role": 1
    }
)

print("Generated JWT:")
print(token)

print("\nDecoded Payload:")
print(verify_access_token(token))