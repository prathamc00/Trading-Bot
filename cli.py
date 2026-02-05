import typer
from bot.client import create_client
from bot.orders import send_order
from bot.validators import check_side, check_order_type, check_qty
from bot.logging_config import init_logger

app = typer.Typer()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    init_logger()

    try:
        # Validate inputs
        side = check_side(side)
        order_type = check_order_type(order_type)
        quantity = check_qty(quantity)

        if order_type == "LIMIT" and not price:
            raise Exception("Limit order requires price")

        print("\nOrder Summary:")
        print(symbol, side, order_type, quantity, price)

        # Create client and place order
        client = create_client()
        order = send_order(client, symbol, side, order_type, quantity, price)

        print("\nOrder Response:")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\nOrder placed successfully!")

    except Exception as e:
        print("\nError:", e)


if __name__ == "__main__":
    app()
