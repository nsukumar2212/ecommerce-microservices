import pandas as pd


INPUT_FILE = "data/products_cleaned.csv"
OUTPUT_FILE = "data/products_small.csv"


# Maximum number of products we want per category
CATEGORY_LIMITS = {
    "Mobiles": 500,
    "Laptops": 500,
    "Televisions": 100,
    "Headphones & Speakers": 100,
    "Tablets": 100,
    "Wearables": 100,
    "Cameras": 150,
    "Gaming Consoles": 30
}


def reduce_products():

    print("Reading original dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Original products: {len(df)}")

    selected_products = []

    for category, limit in CATEGORY_LIMITS.items():

        category_products = df[
            df["category"] == category
        ]

        print(
            f"{category}: "
            f"{len(category_products)} available "
            f"→ keeping {min(len(category_products), limit)}"
        )

        # Take the first 'limit' products
        selected = category_products.head(limit)

        selected_products.append(selected)

    # Combine all categories
    result = pd.concat(
        selected_products,
        ignore_index=True
    )

    # Save the smaller dataset
    result.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print()
    print("==============================")
    print("REDUCTION COMPLETED")
    print("==============================")

    print(f"Original products : {len(df)}")
    print(f"New products      : {len(result)}")
    print(f"Output file       : {OUTPUT_FILE}")

    print()
    print("Products by category:")

    print(
        result["category"].value_counts()
    )


if __name__ == "__main__":
    reduce_products()