def valid_subsequence(array, sequence):
    if not sequence:
        return True
    try:
        idx = array.index(sequence[0])
    except ValueError:
        return False
    else:
        return valid_subsequence(array[idx + 1:], sequence[1:])


# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily
# adjacent in the array but are in the same order as they appear in the array.

tests = [([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
         ([1, 2, 3, 4], [1, 3, 4], True), ([1, 2, 3, 4], [2, 4], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10,
                                         10], False)]

for num, test in enumerate(tests):
    array, sequence, expected = test
    res = valid_subsequence(array, sequence)
    status = "SUCCESS" if res == expected else "FAILED"
    print(f"{num}) {array}, {sequence} -> {expected}, GOT: {res} ({status})")
