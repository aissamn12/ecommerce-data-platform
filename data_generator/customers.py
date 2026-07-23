from faker import Faker
import pandas as pd

fake = Faker()

def generate_customers(n=1000):

    customers = []

    for customer_id in range(1, n + 1):

        customers.append({
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "city": fake.city(),
            "country": fake.country(),
            "signup_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        })

    return pd.DataFrame(customers)


if __name__ == "__main__":

    df = generate_customers()

    df.to_csv(
        "data/raw/customers.csv",
        index=False
    )

    print(df.head())