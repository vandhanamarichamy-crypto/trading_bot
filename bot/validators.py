def validate_order(order_type, quantity, price=None):

    valid_types = ["MARKET", "LIMIT"]

    if order_type not in valid_types:
        raise ValueError("Invalid order type.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT order.")