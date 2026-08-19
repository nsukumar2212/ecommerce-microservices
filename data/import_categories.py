from services.product_service.database import SessionLocal
from services.product_service.models.category import Category
from services.product_service.database import SessionLocal

CATEGORIES = [
    "Mobiles",
    "Laptops",
    "Televisions",
    "Headphones & Speakers",
    "Tablets",
    "Wearables",
    "Cameras",
    "Gaming Consoles"
]


def import_categories():

    db = SessionLocal()

    try:

        for category_name in CATEGORIES:

            existing = (
                db.query(Category)
                .filter(
                    Category.category_name == category_name
                )
                .first()
            )

            if existing:
                print(
                    f"Already exists: {category_name}"
                )
                continue

            category = Category(
                category_name=category_name
            )

            db.add(category)

        db.commit()

        print("\nCategories imported successfully.")

    except Exception as e:

        db.rollback()

        print("Error:", e)

    finally:

        db.close()


if __name__ == "__main__":
    import_categories()