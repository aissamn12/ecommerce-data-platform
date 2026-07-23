import pandas as pd

from customers import generate_customers
from products import generate_products
from orders import generate_orders
from order_items import generate_order_items
from payments import generate_payments




def main():

    customers_df = generate_customers(1000)

    products_df = generate_products(500)

    orders_df = generate_orders(
        customers_df,
        n_orders=10000
    )

    order_items_df = generate_order_items(
        orders_df,
        products_df
    )

    payments_df = generate_payments(
        orders_df,
        order_items_df
    )

    customers_df.to_csv(
        "data/raw/customers.csv",
        index=False
    )

    products_df.to_csv(
        "data/raw/products.csv",
        index=False
    )

    orders_df.to_csv(
        "data/raw/orders.csv",
        index=False
    )

    order_items_df.to_csv(
        "data/raw/order_items.csv",
        index=False
    )

    payments_df.to_csv(
        "data/raw/payments.csv",
        index=False
    )

    print("Data generated successfully")


if __name__ == "__main__":
    main()