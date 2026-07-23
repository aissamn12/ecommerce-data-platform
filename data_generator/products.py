import pandas as pd
import random

CATEGORIES = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

BRANDS = {
    "Electronics": ["Apple", "Samsung", "Sony", "Dell"],
    "Clothing": ["Nike", "Adidas", "Puma", "Zara"],
    "Books": ["Penguin", "HarperCollins", "OReilly"],
    "Home": ["Ikea", "Philips", "Tefal"],
    "Sports": ["Nike", "Adidas", "Wilson"]
}


def generate_products(n=500):

    products = []

    for product_id in range(1, n + 1):

        category = random.choice(CATEGORIES)

        products.append({
            "product_id": product_id,
            "product_name": f"{category}_Product_{product_id}",
            "category": category,
            "brand": random.choice(BRANDS[category]),
            "price": round(random.uniform(10, 2000), 2)
        })

    return pd.DataFrame(products)


if __name__ == "__main__":

    df = generate_products()

    df.to_csv(
        "data/raw/products.csv",
        index=False
    )

    print(df.head())