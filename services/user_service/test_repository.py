from services.user_service.database import SessionLocal
from services.user_service.repositories.user_repository import UserRepository

db = SessionLocal()

users = UserRepository.get_all_users(db)

for user in users:
    print(user.user_id, user.full_name, user.email)

db.close()