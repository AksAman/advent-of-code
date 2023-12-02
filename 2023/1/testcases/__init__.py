from dataclasses import dataclass


@dataclass
class TestCase:
    input: list[str]
    expected: int


TestCases = [
    TestCase(
        input=[
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ],
        expected=142,
    ),
]


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [item.strip("\n") for item in f.readlines()]
