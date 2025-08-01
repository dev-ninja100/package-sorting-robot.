Python

from sort import sort

def run_tests():
    test_cases = [
        (100, 100, 100, 10, "SPECIAL"),
        (50, 50, 50, 25, "SPECIAL"),
        (160, 20, 20, 25, "REJECTED"),
        (10, 10, 10, 5, "STANDARD"),
        (149, 149, 149, 19.9, "STANDARD"),
        (150, 10, 10, 5, "SPECIAL"),
        (10, 10, 10, 20, "SPECIAL"),
    ]

    for i, (w, h, l, m, expected) in enumerate(test_cases, 1):
        result = sort(w, h, l, m)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
