from datetime import datetime
from pathlib import Path

from customers import generate_customers
from products import generate_products
from orders import generate_orders
from order_items import generate_order_items
from payments import generate_payments


def main():

    N_CUSTOMERS = 1000
    N_PRODUCTS = 500
    N_ORDERS = 10000

    run_date = datetime.now().strftime("%Y-%m-%d")

    output_dir = Path(f"data/raw/date={run_date}")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    customers_df = generate_customers(
        N_CUSTOMERS
    )

    products_df = generate_products(
        N_PRODUCTS
    )

    orders_df = generate_orders(
        customers_df,
        N_ORDERS
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
        output_dir / "customers.csv",
        index=False
    )

    products_df.to_csv(
        output_dir / "products.csv",
        index=False
    )

    orders_df.to_csv(
        output_dir / "orders.csv",
        index=False
    )

    order_items_df.to_csv(
        output_dir / "order_items.csv",
        index=False
    )

    payments_df.to_csv(
        output_dir / "payments.csv",
        index=False
    )

    print(f"Data generated successfully in: {output_dir}")


if __name__ == "__main__":
    main()