from dataclasses import dataclass


@dataclass
class TestCase:
    input: list[str]
    expected: int


TestCases = [TestCase()]


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [item.strip("\n") for item in f.readlines()]
