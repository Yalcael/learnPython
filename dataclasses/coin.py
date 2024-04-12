from dataclasses import dataclass


@dataclass
class Coin:
    name: str
    value: int
    id: str


def main() -> None:
    bitcoin: Coin = Coin("Bitcoin", 50000, "BTC")
    bitcoin2: Coin = Coin("Bitcoin", 50000, "BTC")
    ripple: Coin = Coin("Ripple", 30000, "XRP")
    print(bitcoin, bitcoin2, ripple)
    print(bitcoin == ripple)
    print(bitcoin == bitcoin2)


if __name__ == '__main__':
    main()
