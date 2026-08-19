import pandas as pd

from services.product_service.database import SessionLocal
from services.product_service.models.product import Product


CSV_FILE = "data/products_small.csv"

# Correct category IDs from your database
CATEGORY_MAP = {
    "Mobiles": 1,
    "Laptops": 2,
    "Televisions": 6,
    "Headphones & Speakers": 7,
    "Tablets": 8,
    "Wearables": 9,
    "Cameras": 10,
    "Gaming Consoles": 11
}


def import_products():

    db = SessionLocal()

    try:

        df = pd.read_csv(CSV_FILE)

        print(f"CSV products: {len(df)}")

        inserted = 0

        for _, row in df.iterrows():

            product_name = str(
                row["product_name"]
            ).strip()

            brand = str(
                row["brand"]
            ).strip()

            price = float(
                row["price"]
            )

            stock = int(
                row["stock"]
            )

            category_name = str(
                row["category"]
            ).strip()

            image_url = str(
                row["image_url"]
            ).strip()

            # Get correct category ID
            category_id = CATEGORY_MAP.get(
                category_name
            )

            if category_id is None:

                print(
                    f"Skipping: {product_name}"
                    f" | Unknown category: "
                    f"{category_name}"
                )

                continue

            product = Product(
                product_name=product_name,
                brand=brand,
                price=price,
                description=None,
                image=image_url,
                stock=stock,
                category_id=category_id
            )

            db.add(product)

            inserted += 1

            # Commit every 500 products
            if inserted % 500 == 0:

                db.commit()

                print(
                    f"Inserted {inserted} products..."
                )

        # Final commit
        db.commit()

        print()
        print("==============================")
        print("IMPORT COMPLETED")
        print("==============================")
        print(
            f"Inserted: {inserted}"
        )

    except Exception as e:

        db.rollback()

        print()
        print("==============================")
        print("IMPORT FAILED")
        print("==============================")

        print(
            f"{type(e).__name__}: {e}"
        )

    finally:

        db.close()


if __name__ == "__main__":
    import_products()