from range_extraction import extractRange

def main():
    test = extractRange([-3, -2, -1, 0])
    test1 = extractRange([1, 2, 3, 5])
    test2 = extractRange([0, 1, 3])
    test3 = extractRange([-3, -2, -1, 0])
    test4 = extractRange([5, 6, 8, 9, 10])

    print()
if __name__ == '__main__':
    main()