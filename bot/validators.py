def check_side(s):
    s = s.upper()
    if s not in ["BUY", "SELL"]:
        raise Exception("Side should be BUY or SELL")
    return s


def check_order_type(t):
    t = t.upper()
    if t not in ["MARKET", "LIMIT"]:
        raise Exception("Order type should be MARKET or LIMIT")
    return t


def check_qty(q):
    q = float(q)
    if q <= 0:
        raise Exception("Quantity must be greater than 0")
    return q
