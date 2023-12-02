digit_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_val(raw_val: str):
    numeric_values = [int(v) for v in list(raw_val) if v.isdigit()]
    calibration_val = 0
    first, last = numeric_values[0], numeric_values[-1]
    calibration_val = 10 * first + last

    return calibration_val


def solve(raw_calibration_values: list[str]):
    total = 0
    for raw_calibration_val in raw_calibration_values:
        raw_calibration_val = raw_calibration_val.strip("\n")
        calibration_val = get_calibration_val(raw_calibration_val)
        print(f"\t {raw_calibration_val}={calibration_val}")
        total += calibration_val

    return total


if __name__ == "__main__":
    from testcases import TestCases, read_input

    for test_case in TestCases:
        sol = solve(raw_calibration_values=test_case.input)
        print(f"expected={test_case.expected}, solution={sol}")
        assert sol == test_case.expected

    problem_values = read_input(filename="inputs/input.txt")

    solution = solve(raw_calibration_values=problem_values)
    print("Solution: ", solution)
