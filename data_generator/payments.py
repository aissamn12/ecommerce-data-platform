import pandas as pd
import random
from faker import Faker

fake = Faker()

PAYMENT_STATUS = [
    "paid",
    "failed",
    "refunded"
]


def generate_payments(
    orders_df,
    order_items_df
):

    order_totals = (
        order_items_df.assign(
            total=lambda df: df["quantity"] * df["unit_price"]
        )
        .groupby("order_id", as_index=False)["total"]
        .sum()
    )

    payments = []

    for payment_id, row in enumerate(
        order_totals.itertuples(index=False),
        start=1
    ):

        payments.append({
            "payment_id": payment_id,
            "order_id": row.order_id,
            "amount": round(row.total, 2),
            "payment_date": fake.date_time_between(
                start_date="-1y",
                end_date="now"
            ),
            "payment_status": random.choices(
                PAYMENT_STATUS,
                weights=[90, 5, 5],
                k=1
            )[0]
        })

    return pd.DataFrame(payments)


if __name__ == "__main__":

    orders_df = pd.read_csv(
        "data/raw/orders.csv"
    )

    order_items_df = pd.read_csv(
        "data/raw/order_items.csv"
    )

    payments_df = generate_payments(
        orders_df,
        order_items_df
    )

    payments_df.to_csv(
        "data/raw/payments.csv",
        index=False
    )

    print(payments_df.head())