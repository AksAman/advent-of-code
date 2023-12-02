def solve(input: list[str]):
    ...


if __name__ == "__main__":
    from testcases import TestCases, read_input

    for test_case in TestCases:
        sol = solve(input=test_case.input)
        print(f"expected={test_case.expected}, solution={sol}")
        assert sol == test_case.expected

    problem_values = read_input(filename="inputs/input.txt")

    solution = solve(input=problem_values)
    print("Solution: ", solution)
