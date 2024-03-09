from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Comment:
    id: int = field()
    text: str = field(default="")
    replies: list[int] = field(
        default_factory=list, compare=False, repr=False, hash=False
    )


def main():
    comment = Comment(1, "Hello World")
    print(comment)
    # print(astuple(comment))
    # print(asdict(comment))


if __name__ == "__main__":
    main()
