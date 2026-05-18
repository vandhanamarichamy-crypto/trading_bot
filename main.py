from bot.cli import parse_arguments
from bot.validators import validate_order
from bot.orders import place_order


def main():

    try:

        args = parse_arguments()

        validate_order(
            args.type,
            args.quantity,
            args.price
        )

        print("\nORDER REQUEST")
        print("-------------------")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        response = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nORDER SUCCESS")
        print("-------------------")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")

    except Exception as e:
        print("\nERROR")
        print("-------------------")
        print(str(e))


if __name__ == "__main__":
    main()