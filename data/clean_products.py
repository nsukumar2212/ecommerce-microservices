import pandas as pd
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FILE = BASE_DIR / "products_cleaned.csv"


FILES = {
    "mobiles.csv": "Mobiles",
    "laptops.csv": "Laptops",
    "televisions.csv": "Televisions",
    "headphones_and_speakers.csv": "Headphones & Speakers",
    "tablets.csv": "Tablets",
    "wearables.csv": "Wearables",
    "cameras.csv": "Cameras",
    "gaming_consoles.csv": "Gaming Consoles",
}


def clean_dataset():

    all_products = []

    for filename, category in FILES.items():

        file_path = BASE_DIR / filename

        print(f"\nProcessing: {filename}")

        df = pd.read_csv(file_path)

        print(f"Original rows: {len(df)}")

        # --------------------------------
        # Keep products having name & price
        # --------------------------------

        df = df[
            df["Product Name"].notna()
            & df["Price in India"].notna()
        ].copy()

        # --------------------------------
        # Clean price
        # --------------------------------

        df["Price in India"] = (
            df["Price in India"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)
            .str.strip()
        )

        df["Price in India"] = pd.to_numeric(
            df["Price in India"],
            errors="coerce"
        )

        # Remove invalid prices

        df = df[
            df["Price in India"].notna()
        ]

        # --------------------------------
        # Create common structure
        # --------------------------------

        cleaned = pd.DataFrame()

        cleaned["product_name"] = (
            df["Product Name"]
            .astype(str)
            .str.strip()
        )

        cleaned["brand"] = (
            df["Brand"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        cleaned["model"] = (
            df["Model"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        cleaned["category"] = category

        cleaned["price"] = df["Price in India"]

        # --------------------------------
        # Image URL
        # --------------------------------

        if "Picture URL" in df.columns:

            cleaned["image_url"] = (
                df["Picture URL"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        elif "picture" in df.columns:

            cleaned["image_url"] = (
                df["picture"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        else:

            cleaned["image_url"] = ""

        # --------------------------------
        # Product URL
        # --------------------------------

        if "url" in df.columns:

            cleaned["product_url"] = (
                df["url"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        elif "link" in df.columns:

            cleaned["product_url"] = (
                df["link"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        else:

            cleaned["product_url"] = ""

        # --------------------------------
        # Generate stock
        # --------------------------------

        cleaned["stock"] = [
            random.randint(5, 50)
            for _ in range(len(cleaned))
        ]

        all_products.append(cleaned)

        print(
            f"Products kept: {len(cleaned)}"
        )

    # --------------------------------
    # Combine all datasets
    # --------------------------------

    products = pd.concat(
        all_products,
        ignore_index=True
    )

    # --------------------------------
    # Remove duplicate products
    # --------------------------------

    products = products.drop_duplicates(
        subset=[
            "product_name",
            "brand",
            "model",
            "category"
        ]
    )

    # --------------------------------
    # Generate product IDs
    # --------------------------------

    products.insert(
        0,
        "product_id",
        range(1, len(products) + 1)
    )

    # --------------------------------
    # Save cleaned dataset
    # --------------------------------

    products.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n================================")
    print("CLEANING COMPLETED")
    print("================================")

    print(
        f"Total products: {len(products)}"
    )

    print(
        f"Output file: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    clean_dataset()