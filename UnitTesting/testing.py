from findSquare import square

def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Square of 2 was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Square of 3 was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("Square of -2 was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("Square of -3 was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("Square of 0 was not 0")

if __name__ == "__main__":
    main()