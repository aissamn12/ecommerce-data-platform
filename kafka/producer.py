import json
import time
from pathlib import Path

import pandas as pd
from kafka import KafkaProducer


def get_latest_orders_file():

    raw_dir = Path("data/raw")

    latest_partition = max(
        raw_dir.glob("date=*"),
        key=lambda p: p.name
    )

    return latest_partition / "orders.csv"


def create_producer():

    return KafkaProducer(
        bootstrap_servers="kafka:9092",
        value_serializer=lambda value:
        json.dumps(value).encode("utf-8")
    )


def send_orders():

    orders_file = get_latest_orders_file()

    print(f"Reading data from: {orders_file}")

    orders_df = pd.read_csv(orders_file)

    producer = create_producer()

    for _, row in orders_df.iterrows():

        order = row.to_dict()

        producer.send(
            topic="orders",
            value=order
        )

        print(
            f"Sent order {order['order_id']}"
        )

        time.sleep(1)

    producer.flush()

    print("All orders sent successfully")


if __name__ == "__main__":
    send_orders()