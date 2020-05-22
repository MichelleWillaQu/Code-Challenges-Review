def three_num_sum(array, target_sum):
    mySet = set(array)
    result = []
    for num1 in mySet:
        for num2 in mySet:
            if num1 == num2:
                break
            looking_for = target_sum - num1 - num2
            if (looking_for != num1 and looking_for != num2
                    and looking_for in mySet):
                addition = sorted([num1, num2, looking_for])
                if addition not in result:
                    result.append(addition)
    return sorted(result)


# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. The function should find all triplets in
# the array that sum up to the target sum and return a two-dimensional array of
# all these triplets. The numbers in each triplet should be ordered in
# ascending order, and the triplets themselves should be ordered in ascending
# order withrespect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an
# empty array.

tests = [([12, 3, 1, 2, -6, 5, -8, 6], 0, ([[-8, 2, 6], [-8, 3, 5], [-6, 1,
                                                                     5]]))]

for num, test in enumerate(tests):
    array, target_sum, expected = test
    res = three_num_sum(array, target_sum)
    status = "SUCCESS" if res == expected else "FAILED"
    print(f"{num}) {array}, {target_sum} -> {expected}, GOT: {res} ({status})")

# Optimal time O(n^2), optimal space O(n)
