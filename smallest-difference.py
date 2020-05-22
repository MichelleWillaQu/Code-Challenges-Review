def smallest_diff(array_one, array_two):
    array_one.sort()
    array_two.sort()
    min_distance = -1
    diff = -1
    result = []
    for num1 in array_one:
        for num2 in array_two:
            if diff != -1 and abs(num1 - num2) > diff:
                diff = -1
                break
            diff = abs(num2 - num1)
            if min_distance == -1 or min_distance > diff:
                min_distance = diff
                result = [num1, num2]
    return result


# Write a function that takes in two non-empty arrays of integers, finds the
# pair of numbers (one from each array) whose absolute difference is closest to
# zero, and returns an array containing these two numbers, with the number from
# the first array in the first position.
# You can assume that there will only be one pair of numbers with the smallest
# difference.

tests = [([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26])]

for num, test in enumerate(tests):
    array_one, array_two, expected = test
    res = smallest_diff(array_one, array_two)
    status = "SUCCESS" if res == expected else "FAILED"
    print(
        f"{num}) {array_one}, {array_two} -> {expected}, GOT: {res} ({status})"
    )

# Optimal time O(nlog(n)+mlog(m)), optimal space O(1)
