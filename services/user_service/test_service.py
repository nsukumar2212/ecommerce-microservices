from services.user_service.database import SessionLocal
from services.user_service.services.user_service import UserService

db = SessionLocal()

users = UserService.get_all_users(db)

print(f"Total Users: {len(users)}")
print("-" * 50)

for user in users:
    print(user.user_id, user.full_name, user.email)

db.close()