
def splitlist(numbers):

    minimumvalue = min(numbers)

    minIndex = numbers.index(minimumvalue)

    numbers[0], numbers[minIndex] = numbers[minIndex], numbers[0]

    first, *others = numbers

    return first, others

def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
