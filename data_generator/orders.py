import pandas as pd
import random
from faker import Faker

fake = Faker()

ORDER_STATUS = [
    "pending",
    "processing",
    "shipped",
    "delivered",
    "cancelled"
]

PAYMENT_METHODS = [
    "credit_card",
    "paypal",
    "bank_transfer"
]


def generate_orders(
    customers_df,
    n_orders=10000
):

    orders = []

    customer_ids = customers_df["customer_id"].tolist()

    for order_id in range(1, n_orders + 1):

        orders.append({
            "order_id": order_id,
            "customer_id": random.choice(customer_ids),
            "order_date": fake.date_time_between(
                start_date="-1y",
                end_date="now"
            ),
            "status": random.choice(ORDER_STATUS),
            "payment_method": random.choice(PAYMENT_METHODS)
        })

    return pd.DataFrame(orders)


if __name__ == "__main__":

    customers_df = pd.read_csv(
        "data/raw/customers.csv"
    )

    orders_df = generate_orders(
        customers_df
    )

    orders_df.to_csv(
        "data/raw/orders.csv",
        index=False
    )

    print(orders_df.head())