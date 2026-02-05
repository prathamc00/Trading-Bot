import logging

def send_order(client, symbol, side, otype, qty, price=None):
    logging.info(f"Placing order: {symbol} {side} {otype} {qty}")

    if otype == "MARKET":
        order = client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )

    else: 
        order = client.create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=qty,
            price=price,
            timeInForce="GTC"
        )

    logging.info(f"Order response: {order}")
    return order
