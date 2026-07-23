import json

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="kafka:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x:
    json.loads(x.decode("utf-8"))
)

print("Listening for messages...\n")

for message in consumer:

    order = message.value

    print(order)