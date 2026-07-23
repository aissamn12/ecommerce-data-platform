import pandas as pd
import random


def generate_order_items(
    orders_df,
    products_df,
    max_items_per_order=5
):

    order_items = []
    order_item_id = 1

    for _, order in orders_df.iterrows():

        num_items = random.randint(1, max_items_per_order)

        selected_products = products_df.sample(
            n=num_items,
            replace=False
        )

        for _, product in selected_products.iterrows():

            quantity = random.randint(1, 5)

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order["order_id"],
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": product["price"]
            })

            order_item_id += 1

    return pd.DataFrame(order_items)


if __name__ == "__main__":

    orders_df = pd.read_csv(
        "data/raw/orders.csv"
    )

    products_df = pd.read_csv(
        "data/raw/products.csv"
    )

    order_items_df = generate_order_items(
        orders_df,
        products_df
    )

    order_items_df.to_csv(
        "data/raw/order_items.csv",
        index=False
    )

    print(order_items_df.head())