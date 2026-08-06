from shared.security.password import (
    hash_password,
    verify_password
)

password = "123456"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print(
    verify_password(
        password,
        hashed
    )
)