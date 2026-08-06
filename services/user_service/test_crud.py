from services.user_service.database import SessionLocal
from services.user_service.crud.user_crud import UserCRUD

db = SessionLocal()

users = UserCRUD.get_all_users(db)

print(f"Total Users: {len(users)}")
print("-" * 50)

for user in users:
    print(
        f"ID: {user.user_id}, "
        f"Name: {user.full_name}, "
        f"Email: {user.email}"
    )

db.close()